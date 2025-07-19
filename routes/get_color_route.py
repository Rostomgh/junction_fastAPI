from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from PIL import Image
import io

from utils.label_color import analyze_strip_image 

router = APIRouter()

@router.post("/analyze")
async def analyze_image(file: UploadFile = File(...)):
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

    results = analyze_strip_image(image)
    return JSONResponse(content=results)
