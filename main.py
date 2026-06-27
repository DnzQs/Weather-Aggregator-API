from fastapi import FastAPI
from app.core.database import engine, Base
from app.weather.router import router as weather_router
from app.weather.models import WeatherHistory

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(weather_router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "Welcome to Weather Aggregator API! Go to /docs for Swagger UI."}