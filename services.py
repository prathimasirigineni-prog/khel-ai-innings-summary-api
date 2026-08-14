from utils import (
    calculate_economy,
    calculate_run_rate,
    calculate_strike_rate,
    get_recent_balls,
)


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


def build_batter_summaries(ball_events):
    batter_data = {}

    for ball in ball_events:
        striker = ball.striker

        if striker not in batter_data:
            batter_data[striker] = {
                "name": striker,
                "runs": 0,
                "balls": 0,
                "fours": 0,
                "sixes": 0,
            }

        batter_data[striker]["runs"] += ball.runs

        if ball.is_legal:
            batter_data[striker]["balls"] += 1

        if ball.runs == 4:
            batter_data[striker]["fours"] += 1

        if ball.runs == 6:
            batter_data[striker]["sixes"] += 1

    batters = []

    for batter in batter_data.values():
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
            "strike_rate": round(strike_rate, 2),
        })

    return batters


def build_bowler_summaries(ball_events):
    bowler_data = {}

    for ball in ball_events:
        bowler = ball.bowler

        if bowler not in bowler_data:
            bowler_data[bowler] = {
                "name": bowler,
                "legal_balls": 0,
                "runs_conceded": 0,
                "wickets": 0,
            }

        if ball.is_legal:
            bowler_data[bowler]["legal_balls"] += 1

        bowler_data[bowler]["runs_conceded"] += ball.runs

        if ball.wicket:
            bowler_data[bowler]["wickets"] += 1

    bowlers = []

    for bowler in bowler_data.values():
        overs = bowler["legal_balls"] / 6

        economy = calculate_economy(
            bowler["runs_conceded"],
            overs
        )

        bowlers.append({
            "name": bowler["name"],
            "overs": round(overs, 1),
            "runs_conceded": bowler["runs_conceded"],
            "wickets": bowler["wickets"],
            "economy": round(economy, 2),
        })

    return bowlers


def get_innings_summary(innings):
    if not innings.ball_events:
        return None

    total_runs = sum(
        ball.runs
        for ball in innings.ball_events
    )

    wickets = sum(
        1
        for ball in innings.ball_events
        if ball.wicket
    )

    legal_balls = sum(
        1
        for ball in innings.ball_events
        if ball.is_legal
    )

    overs = legal_balls / 6

    run_rate = calculate_run_rate(
        total_runs,
        overs
    )

    batters = build_batter_summaries(
        innings.ball_events
    )

    bowlers = build_bowler_summaries(
        innings.ball_events
    )

    recent_balls = get_recent_balls(
        innings.ball_events
    )

    return {
        "innings_id": innings.innings_id,
        "total_runs": total_runs,
        "wickets": wickets,
        "legal_balls": legal_balls,
        "overs": round(overs, 1),
        "run_rate": round(run_rate, 2),
        "batters": batters,
        "bowlers": bowlers,
        "top_batter": get_top_batter(batters),
        "top_bowler": get_top_bowler(bowlers),
        "recent_balls": recent_balls,
    }
