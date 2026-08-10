from fastapi import FastAPI, HTTPException

from schemas import InningsSummaryResponse
from services import get_innings_summary


app = FastAPI(
    title="Khel AI - Innings Summary API",
    description="API for retrieving a complete innings-level statistical summary.",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "Khel AI Innings Summary API is running"
    }


@app.get(
    "/innings/{innings_id}/summary",
    response_model=InningsSummaryResponse
)
def innings_summary(innings_id: int):
    summary = get_innings_summary(innings_id)

    if summary is None:
        raise HTTPException(
            status_code=404,
            detail="Innings not found"
        )

    return summary