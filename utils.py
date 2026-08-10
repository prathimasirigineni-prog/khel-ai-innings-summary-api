def calculate_run_rate(runs: int, overs: float) -> float:
    if overs <= 0:
        return 0.0

    return runs / overs


def calculate_strike_rate(runs: int, balls: int) -> float:
    if balls <= 0:
        return 0.0

    return (runs / balls) * 100


def calculate_economy(runs_conceded: int, overs: float) -> float:
    if overs <= 0:
        return 0.0

    return runs_conceded / overs