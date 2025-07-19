from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from utils.yolo_handler import run_detection

router = APIRouter()

@router.post("/detect")
async def detect(file: UploadFile = File(...)):
    predictions = await run_detection(file)
    return JSONResponse(content={"detections": predictions})
