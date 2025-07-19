# 🧬 Water Quality & Bacteria Detection API

A FastAPI project that combines:
- YOLOv8 image-based detection for bacteria
- Scikit-learn multi-output classification for water quality prediction
- Color analysis from test strips

---

## 🚀 Features

- `/v1/api/detect`: Upload an image for YOLOv8 object detection
- `/v1/api/analyze`: Upload a test strip image to extract compound levels by color
- `/v1/api/tips`: Submit water parameter values and receive bacteria level + environment quality predictions

---

## 🧱 Project Structure

├── main.py # FastAPI entry point
├── models/
│ └── load_model.py # Loads multioutput_model.pkl
├── routes/
│ ├── detect.py # YOLOv8 detection route
│ ├── get_color_route.py # Color analysis route
│ └── tips.py # Multioutput model prediction route
├── utils/
│ ├── yolo_handler.py # Runs YOLOv8
│ ├── explain.py # Provides prediction insights
│ ├── labels.py # Label mappings
│ └── label_color.py # Color zone analyzer for strips
└── models/
└── best.pt # YOLOv8 trained model
└── multioutput_model.pkl # Scikit-learn prediction model


---

## 📦 Installation

```bash
# Clone this repo
git clone https://github.com/your-repo/water-quality-api
cd water-quality-api

# Install requirements
pip install -r requirements.txt


# Start app
uvicorn main:app --reload
