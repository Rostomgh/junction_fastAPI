# 🧠 YOLOv8 Bacteria Detection API

This project provides a RESTful API using **FastAPI** to detect bacteria (or any other objects) from images using a pre-trained **YOLOv8** model.

---

## 🚀 Features

- Upload an image and detect bacteria (or objects)
- Built with FastAPI
- Uses Ultralytics YOLOv8
- Easy to test with Swagger UI or Postman

---

## 📦 Requirements

Make sure you have Python 3.9–3.11 (avoid 3.12 for now due to torch issues).

```bash
pip install fastapi uvicorn pillow python-multipart
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
pip install ultralytics
