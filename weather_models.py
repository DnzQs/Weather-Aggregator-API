from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from app.core.database import Base

class WeatherHistory(Base):
    __tablename__ = "weather_history"

    id = Column(Integer, primary_key=True, index=True)
    city = Column(String(100), index=True, nullable=False)
    temperature = Column(Float, nullable=False)
    condition = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)