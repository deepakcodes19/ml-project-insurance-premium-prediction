import os
import joblib
import pandas as pd

# Base path for artifacts (works both locally and on Streamlit Cloud)
BASE_PATH = os.path.join(os.path.dirname(__file__), "artifacts")

# --- Load models and scalers safely ---
def safe_load(path):
    """Helper to safely load joblib files."""
    try:
        return joblib.load(path)
    except Exception as e:
        raise RuntimeError(f"Failed to load {path}: {e}")

model_young = safe_load(os.path.join(BASE_PATH, "model_young.joblib"))
model_rest = safe_load(os.path.join(BASE_PATH, "model_rest.joblib"))
scaler_young = safe_load(os.path.join(BASE_PATH, "scaler_young.joblib"))
scaler_rest = safe_load(os.path.join(BASE_PATH, "scaler_rest.joblib"))

# --- Define expected scaler info (columns it was trained on) ---
# ✅ Adjust these names if your training notebook used slightly different column names
scaler_young_info = {
    "scaler": scaler_young,
    "cols_to_scale": ["age", "number_of_dependants", "income_level", "income_lakhs", "insurance_plan"],
}

scaler_rest_info = {
    "scaler": scaler_rest,
    "cols_to_scale": ["age", "number_of_dependants", "income_level", "income_lakhs", "insurance_plan"],
}


def preprocess_input(input_dict):
    """Convert user input into a DataFrame and scale it properly."""
    # Convert to DataFrame
    df = pd.DataFrame([input_dict])

    # 🔠 Normalize column names to lowercase (important!)
    df.columns = df.columns.str.lower()

    # Pick scaler based on age
    if df["age"][0] <= 25:
        scaler_info = scaler_young_info
    else:
        scaler_info = scaler_rest_info

    scaler = scaler_info["scaler"]
    cols_to_scale = scaler_info["cols_to_scale"]

    # ✅ Only scale columns that exist
    common_cols = [c for c in cols_to_scale if c in df.columns]
    df[common_cols] = scaler.transform(df[common_cols])

    return df


def predict(input_dict):
    """Predict insurance premium based on input data."""
    df = preprocess_input(input_dict)

    if df["age"][0] <= 25:
        prediction = model_young.predict(df)
    else:
        prediction = model_rest.predict(df)

    return int(prediction[0])
