import os
import joblib
import pandas as pd

# Base path for artifacts (works both locally and on Streamlit Cloud)
BASE_PATH = os.path.join(os.path.dirname(__file__), "artifacts")

# Load models and scalers safely
model_young = joblib.load(os.path.join(BASE_PATH, "model_young.joblib"))
model_rest = joblib.load(os.path.join(BASE_PATH, "model_rest.joblib"))
scaler_young_info = joblib.load(os.path.join(BASE_PATH, "scaler_young.joblib"))
scaler_rest_info = joblib.load(os.path.join(BASE_PATH, "scaler_rest.joblib"))


def preprocess_input(input_dict):
    """Convert user input into a DataFrame with appropriate scaling."""
    df = pd.DataFrame([input_dict])

    # Select scaler dict based on age
    if df["Age"][0] <= 25:
        scaler_info = scaler_young_info
    else:
        scaler_info = scaler_rest_info

    # Extract real scaler object and column names
    scaler = scaler_info["scaler"]
    cols_to_scale = scaler_info["cols_to_scale"]

    # Apply transformation only on numeric columns
    df[cols_to_scale] = scaler.transform(df[cols_to_scale])

    return df


def predict(input_dict):
    """Predict insurance premium based on input data."""
    df = preprocess_input(input_dict)

    if input_dict["Age"] <= 25:
        prediction = model_young.predict(df)
    else:
        prediction = model_rest.predict(df)

    return int(prediction[0])
