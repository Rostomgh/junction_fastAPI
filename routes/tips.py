from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import pandas as pd

from utils.yolo_handler import run_detection
from utils.labels import env_labels, bact_labels
from models.load_model import model
from utils.explain import explain_prediction

router = APIRouter()

# 1. Define the input schema
class WaterSample(BaseModel):
    Salinity: float
    DissolvedOxygen: float
    pH: float
    SecchiDepth: float
    WaterDepth: float
    WaterTemp: float
    AirTemp: float

# 2. POST endpoint using JSON body
@router.post("/tips")
def tips_router(sample: WaterSample):
    # 3. Convert to DataFrame
    data = {
        'Salinity (ppt)': sample.Salinity,
        'DissolvedOxygen (mg/L)': sample.DissolvedOxygen,
        'pH': sample.pH,
        'SecchiDepth (m)': sample.SecchiDepth,
        'WaterDepth (m)': sample.WaterDepth,
        'WaterTemp (C)': sample.WaterTemp,
        'AirTemp (C)': sample.AirTemp
    }

    df_input = pd.DataFrame([data])

    # 4. Run prediction
    prediction = model.predict(df_input)[0]
    env_quality = env_labels[prediction[0]]
    bact_level = bact_labels[prediction[1]]
    reasons = explain_prediction(data, env_quality, bact_level)

    return {
        "Environment Quality": env_quality,
        "Bacteria Level": bact_level,
        "Explanation": reasons or ["✅ Conditions are optimal."]
    }
