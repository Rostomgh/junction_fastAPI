from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from utils.yolo_handler import run_detection
import pandas as pd 
from fastapi import APIRouter, Query
from utils.labels import env_labels, bact_labels
from utils.explain import explain_prediction

router = APIRouter()

def tips_router(
    Salinity: float = Query(...),
    DissolvedOxygen: float = Query(...),
    pH: float = Query(...),
    SecchiDepth: float = Query(...),
    WaterDepth: float = Query(...),
    WaterTemp: float = Query(...),
    AirTemp: float = Query(...)
):
    sample = {
        'Salinity (ppt)': Salinity,
        'DissolvedOxygen (mg/L)': DissolvedOxygen,
        'pH': pH,
        'SecchiDepth (m)': SecchiDepth,
        'WaterDepth (m)': WaterDepth,
        'WaterTemp (C)': WaterTemp,
        'AirTemp (C)': AirTemp
    }

    df_input = pd.DataFrame([sample])
    prediction = model.predict(df_input)[0]

    env_quality = env_labels[prediction[0]]
    bact_level = bact_labels[prediction[1]]
    reasons = explain_prediction(sample, env_quality, bact_level)

    return {
        "Environment Quality": env_quality,
        "Bacteria Level": bact_level,
        "Explanation": reasons or ["✅ Conditions are optimal."]
    }
