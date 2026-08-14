# Khel AI - Innings Summary API

## Phase 2 - Integration-Ready Version

## Objective

The Innings Summary API provides a complete, integration-ready statistical summary of a cricket innings. It accepts an innings identifier together with ball-event data and calculates the innings totals, wickets, legal balls, overs, run rate, batter summaries, bowler summaries, top performers, and recent balls. The API is designed so that Khel AI backend or Django services can provide the underlying event data while the API performs the required analytics in its service and utility layers.

## Phase 1 to Phase 2 Changes

The Phase 1 implementation used hardcoded innings summary data inside the service layer.

The Phase 2 implementation removes the hardcoded summary data and accepts ball-event data through a validated request payload.

The summary values are now derived from the supplied events rather than being manually stored.

## Integration Flow

Django / Khel AI Backend
        |
        v
Innings Summary API
        |
        v
Service Layer
        |
        v
Calculated Innings Summary
        |
        v
Frontend / Orchestration / AI Agent

## Endpoint

POST /innings/{innings_id}/summary

## Example

POST /innings/1/summary

## Request Structure

The request contains:

- innings_id
- ball_events
- over_ball
- striker
- bowler
- runs
- extras
- is_legal
- extra_type
- wicket

## Response

The API returns:

- Innings ID
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

## Business Logic

The service layer:

1. Calculates total runs from ball events.
2. Counts wickets from wicket events.
3. Counts legal deliveries.
4. Calculates overs from legal deliveries.
5. Calculates innings run rate.
6. Builds batter summaries.
7. Builds bowler summaries.
8. Identifies the top batter.
9. Identifies the top bowler.
10. Extracts recent ball information.

## Integration Readiness

The API does not depend on a hardcoded innings dictionary.

The input is validated through Pydantic schemas, making the API suitable for data supplied by a Khel AI backend or Django integration layer.

The response structure is stable and can be consumed directly by frontend widgets or other Khel AI services.

## Error Handling

The API returns HTTP 400 when the path innings ID does not match the innings ID in the supplied payload.

The API returns HTTP 404 when no ball-event data is available for the requested innings.

## Run Locally

```bash
uvicorn main:app --reload
