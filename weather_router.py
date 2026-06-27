from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
import httpx

from app.core.database import get_db
from app.weather.models import WeatherHistory
from app.weather.schemas import WeatherResponse, HistoryResponse

router = APIRouter(prefix="/weather", tags=["Weather"])


@router.get("/", response_model=WeatherResponse)
async def get_current_weather(city: str, db: Session = Depends(get_db)):
    url = f"https://wttr.in/{city}?format=j1"

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, timeout=5.0)
            response.raise_for_status()
            data = response.json()
        except (httpx.HTTPError, ValueError):
            raise HTTPException(status_code=503, detail="Weather service is unavailable")

    try:
        current_condition = data["current_condition"][0]
        temp_c = float(current_condition["temp_C"])
        weather_desc = current_condition["weatherDesc"][0]["value"]
    except (KeyError, IndexError, ValueError):
        raise HTTPException(status_code=404, detail="City not found or invalid data format")

    history_entry = WeatherHistory(
        city=city.capitalize(),
        temperature=temp_c,
        condition=weather_desc
    )
    db.add(history_entry)
    db.commit()

    return {
        "city": city.capitalize(),
        "temperature": temp_c,
        "condition": weather_desc
    }


@router.get("/history", response_model=list[HistoryResponse])
def get_weather_history(
        city: str = Query(None, description="Filter history by city name"),
        db: Session = Depends(get_db)
):
    query = db.query(WeatherHistory)
    if city:
        query = query.filter(WeatherHistory.city == city.capitalize())

    return query.order_by(WeatherHistory.created_at.desc()).all()