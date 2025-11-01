import os
import joblib
import pandas as pd

# Base path for artifacts (works both locally and on Streamlit Cloud)
BASE_PATH = os.path.join(os.path.dirname(__file__), "artifacts")


def load_scaler(path):
    """Load scaler safely and handle dict-based scalers."""
    obj = joblib.load(path)
    # Handle dicts that contain a scaler
    if isinstance(obj, dict):
        if "scaler" in obj:
            return obj["scaler"]
    return obj


# --- Load models and scalers safely ---
def safe_load(path):
    try:
        return joblib.load(path)
    except Exception as e:
        raise RuntimeError(f"Failed to load {path}: {e}")


model_young = safe_load(os.path.join(BASE_PATH, "model_young.joblib"))
model_rest = safe_load(os.path.join(BASE_PATH, "model_rest.joblib"))
scaler_young = load_scaler(os.path.join(BASE_PATH, "scaler_young.joblib"))
scaler_rest = load_scaler(os.path.join(BASE_PATH, "scaler_rest.joblib"))


def preprocess_input(input_dict):
    """Convert user input into a DataFrame with appropriate scaling."""
    df = pd.DataFrame([input_dict])
    df.columns = df.columns.str.lower()  # normalize

    if df["age"][0] <= 25:
        df_scaled = df.copy()
        df_scaled[df.columns] = scaler_young.transform(df[df.columns])
    else:
        df_scaled = df.copy()
        df_scaled[df.columns] = scaler_rest.transform(df[df.columns])

    return df_scaled


def predict(input_dict):
    """Predict insurance premium based on input data."""
    df = preprocess_input(input_dict)

    if df["age"][0] <= 25:
        prediction = model_young.predict(df)
    else:
        prediction = model_rest.predict(df)

    return int(prediction[0])
