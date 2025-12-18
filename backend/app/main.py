from fastapi import FastAPI
from .database import engine, Base

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Cardex API")

@app.get("/")
def read_root():
    return {"message": "Welcome to Cardex API"}
