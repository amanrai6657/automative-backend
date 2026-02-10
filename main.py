from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Automotive App API", version="v2")

vehicles_db = [
    {"id": 1, "name": "Toyota Fortuner", "type": "SUV"},
    {"id": 2, "name": "Honda City", "type": "Sedan"},
    {"id": 3, "name": "Tata Nexon", "type": "Compact SUV"}
]

class ServiceBooking(BaseModel):
    customer_name: str
    vehicle_name: str
    service_type: str

@app.get("/")
def home():
    return {
        "message": "Welcome to Automotive Application API - v2",
        "version": "v2"
    }

@app.get("/vehicles")
def get_vehicles():
    return vehicles_db

@app.get("/health")
def health():
    return {"status": "UP"}
