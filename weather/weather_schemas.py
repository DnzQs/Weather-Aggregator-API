from pydantic import BaseModel, ConfigDict
from datetime import datetime


class WeatherResponse(BaseModel):
    city: str
    temperature: float
    condition: str


class HistoryResponse(WeatherResponse):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
