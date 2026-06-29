# Weather-Aggregator-API

A REST API to fetch, aggregate, and store weather data from external public services.

# Description:
This project is a clean, lightweight backend service built with FastAPI that allows users to:
* Fetch live weather forecasts (temperature and conditions) for any city worldwide
* Integrate with public weather service data using asynchronous HTTP clients
* Automatically cache and log search queries into a persistent history database
* Retrieve and filter search history logs by city name

# Tech Stack:
* FastAPI
* PostgreSQL
* SQLAlchemy
* Pydantic (Pydantic Settings)
* HTTPX (Async HTTP client)
* Docker

# Features:
* Weather Forecasts
  * Live city weather retrieval via non-blocking external API requests
  * Automatic logging of queries with conditions and temperature values
* History
  * Access full log history sorted by query time
  * Query parameter filters to search history data for specific cities

Project structure:
weather_api/
.env
docker-compose.yml
requirements.txt
app/
main.py
core/
config.py
database.py
weather/
models.py
schemas.py
router.py

# Run the Project

* Locally
pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic-settings httpx
uvicorn app.main:app --reload

* Using Docker
docker-compose up --build

# API Documentation
After running the server: http://localhost:8000/docs

# Environment Variables
Create a .env file:
DATABASE_URL=postgresql://postgres:postgres@db:5432/weather_db
