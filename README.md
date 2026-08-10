# Khel AI - Innings Summary API

## Objective

The Innings Summary API provides a complete innings-level statistical summary. It accepts an innings identifier and returns totals, wickets, legal balls, overs, run rate, batter summaries, bowler summaries, top performers, and recent balls.

## Endpoint

GET /innings/{innings_id}/summary

## Example

GET /innings/1/summary

## Response

The API returns:

- Total runs
- Wickets
- Legal balls
- Overs
- Run rate
- Batter summaries
- Bowler summaries
- Top batter
- Top bowler
- Recent balls

## Run locally

uvicorn main:app --reload

## Swagger documentation

/docs