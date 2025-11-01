import os
import joblib
import pandas as pd

# Base path for artifacts (works both locally and on Streamlit Cloud)
BASE_PATH = os.path.join(os.path.dirname(__file__), "artifacts")

# Load models and scalers safely
model_young = joblib.load(os.path.join(BASE_PATH, "model_young.joblib"))
model_rest = joblib.load(os.path.join(BASE_PATH, "model_rest.joblib"))
scaler_young = joblib.load(os.path.join(BASE_PATH, "scaler_young.joblib"))
scaler_rest = joblib.load(os.path.join(BASE_PATH, "scaler_rest.joblib"))


def preprocess_input(input_dict):
    """Convert user input into a DataFrame with appropriate scaling."""
    df = pd.DataFrame([input_dict])

    # Separate scaling based on age
    if df['Age'][0] <= 25:
        df_scaled = scaler_young.transform(df)
    else:
        df_scaled = scaler_rest.transform(df)

    return df_scaled


def predict(input_dict):
    """Predict insurance premium based on input data."""
    df = preprocess_input(input_dict)

    if input_dict['Age'] <= 25:
        prediction = model_young.predict(df)
    else:
        prediction = model_rest.predict(df)

    return int(prediction[0])
