from pydantic import BaseModel
from typing import List


class BatterSummary(BaseModel):
    name: str
    runs: int
    balls: int
    fours: int
    sixes: int
    strike_rate: float


class BowlerSummary(BaseModel):
    name: str
    overs: float
    runs_conceded: int
    wickets: int
    economy: float


class InningsSummaryResponse(BaseModel):
    innings_id: int
    total_runs: int
    wickets: int
    legal_balls: int
    overs: float
    run_rate: float
    batters: List[BatterSummary]
    bowlers: List[BowlerSummary]
    top_batter: str
    top_bowler: str
    recent_balls: List[str]