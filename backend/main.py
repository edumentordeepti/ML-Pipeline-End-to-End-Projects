from fastapi import FastAPI
import pickle
import numpy as np
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all (for development)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

class InputData(BaseModel):
    cylinders: float
    displacement: float
    horsepower: float
    weight: float
    acceleration:float
    origin: int

@app.get("/")
def home():
    return {"message": "MPG Prediction API is Running"}

@app.post("/predict")
def predict(data: InputData):
    features = np.array([[data.cylinders, data.displacement, data.horsepower, data.weight, data.acceleration, data.origin]])
    prediction = model.predict(features)[0]

    return {"predicted_mpg": float(prediction)}