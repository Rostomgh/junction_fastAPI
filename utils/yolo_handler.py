from ultralytics import YOLO
import shutil
import os
from pathlib import Path

model = YOLO("models/best.pt")
TEMP_DIR = Path("temp")
TEMP_DIR.mkdir(exist_ok=True)

async def run_detection(file):
    file_path = TEMP_DIR / file.filename
    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    results = model(str(file_path))
    boxes = results[0].boxes

    predictions = []
    for box in boxes:
        cls = int(box.cls[0])
        conf = float(box.conf[0])
        xyxy = [float(x) for x in box.xyxy[0]]
        predictions.append({
            "class": model.names[cls],
            "confidence": conf,
            "bbox": xyxy
        })

    file_path.unlink()  
    return predictions
