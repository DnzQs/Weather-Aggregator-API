from fastapi import FastAPI
from app.core.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to Weather Aggregator API! Go to /docs for Swagger UI."}