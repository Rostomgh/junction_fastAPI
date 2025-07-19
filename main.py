from fastapi import FastAPI
from routes.detect import router as detect_router
from routes.tips import router as tips_router

app = FastAPI(
    title="YOLOv8 FastAPI Bacteria Detection",
    version="1.0.0"
)

app.include_router(detect_router, prefix="/v1/api")
app.include_router(tips_router, prefix="/v1/api")
