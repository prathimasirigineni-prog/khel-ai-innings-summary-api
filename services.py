from utils import calculate_economy, calculate_run_rate, calculate_strike_rate


INNINGS = {
    1: {
        "innings_id": 1,
        "total_runs": 142,
        "wickets": 4,
        "legal_balls": 108,
        "batters": [
            {
                "name": "Player A",
                "runs": 67,
                "balls": 48,
                "fours": 7,
                "sixes": 2
            },
            {
                "name": "Player B",
                "runs": 39,
                "balls": 32,
                "fours": 4,
                "sixes": 1
            },
            {
                "name": "Player C",
                "runs": 21,
                "balls": 18,
                "fours": 2,
                "sixes": 0
            }
        ],
        "bowlers": [
            {
                "name": "Bowler A",
                "legal_balls": 24,
                "runs_conceded": 28,
                "wickets": 2
            },
            {
                "name": "Bowler B",
                "legal_balls": 24,
                "runs_conceded": 31,
                "wickets": 1
            },
            {
                "name": "Bowler C",
                "legal_balls": 18,
                "runs_conceded": 25,
                "wickets": 1
            }
        ],
        "recent_balls": [
            "1",
            "4",
            "0",
            "W",
            "2",
            "1"
        ]
    }
}


def get_top_batter(batters):
    if not batters:
        return "N/A"

    return max(
        batters,
        key=lambda batter: batter["runs"]
    )["name"]


def get_top_bowler(bowlers):
    if not bowlers:
        return "N/A"

    return max(
        bowlers,
        key=lambda bowler: bowler["wickets"]
    )["name"]


def get_innings_summary(innings_id: int):
    innings = INNINGS.get(innings_id)

    if innings is None:
        return None

    legal_balls = innings["legal_balls"]
    overs = legal_balls / 6

    run_rate = calculate_run_rate(
        innings["total_runs"],
        overs
    )

    batters = []

    for batter in innings["batters"]:
        strike_rate = calculate_strike_rate(
            batter["runs"],
            batter["balls"]
        )

        batters.append({
            "name": batter["name"],
            "runs": batter["runs"],
            "balls": batter["balls"],
            "fours": batter["fours"],
            "sixes": batter["sixes"],
            "strike_rate": round(strike_rate, 2)
        })

    bowlers = []

    for bowler in innings["bowlers"]:
        bowler_overs = bowler["legal_balls"] / 6

        economy = calculate_economy(
            bowler["runs_conceded"],
            bowler_overs
        )

        bowlers.append({
            "name": bowler["name"],
            "overs": round(bowler_overs, 1),
            "runs_conceded": bowler["runs_conceded"],
            "wickets": bowler["wickets"],
            "economy": round(economy, 2)
        })

    return {
        "innings_id": innings["innings_id"],
        "total_runs": innings["total_runs"],
        "wickets": innings["wickets"],
        "legal_balls": legal_balls,
        "overs": round(overs, 1),
        "run_rate": round(run_rate, 2),
        "batters": batters,
        "bowlers": bowlers,
        "top_batter": get_top_batter(batters),
        "top_bowler": get_top_bowler(bowlers),
        "recent_balls": innings["recent_balls"]
    }