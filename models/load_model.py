import joblib
import os

model_path = os.path.join(os.path.dirname(__file__), "multioutput_model.pkl")
model = joblib.load(model_path)
