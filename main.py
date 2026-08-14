from fastapi import FastAPI, HTTPException

from schemas import (
    InningsSummaryRequest,
    InningsSummaryResponse,
)
from services import get_innings_summary


app = FastAPI(
    title="Khel AI - Innings Summary API",
    description=(
        "Integration-ready API for generating a complete innings-level "
        "statistical summary from ball-event data."
    ),
    version="2.0.0",
)


@app.get("/")
def root():
    return {
        "message": "Khel AI Innings Summary API is running",
        "version": "2.0.0"
    }


@app.post(
    "/innings/{innings_id}/summary",
    response_model=InningsSummaryResponse
)
def innings_summary(
    innings_id: int,
    innings_data: InningsSummaryRequest
):
    if innings_data.innings_id != innings_id:
        raise HTTPException(
            status_code=400,
            detail="Innings ID does not match the supplied data"
        )

    summary = get_innings_summary(innings_data)

    if summary is None:
        raise HTTPException(
            status_code=404,
            detail="No ball-event data available for this innings"
        )

    return summary
