import pandas as pd
import joblib
import os

# Use raw string or relative paths
BASE_PATH = r"C:\Users\Deepak Y\OneDrive\Documents\Pyhton Basics\ML_Premium_Prediction\artifacts"

model_young = joblib.load(os.path.join(BASE_PATH, "model_young.joblib"))
model_rest = joblib.load(os.path.join(BASE_PATH, "model_rest.joblib"))
scaler_young = joblib.load(os.path.join(BASE_PATH, "scaler_young.joblib"))
scaler_rest = joblib.load(os.path.join(BASE_PATH, "scaler_rest.joblib"))


def calculate_normalized_risk(medical_history):
    risk_scores = {
        "diabetes": 6,
        "heart disease": 8,
        "high blood pressure": 6,
        "thyroid": 5,
        "no disease": 0
    }
    diseases = medical_history.lower().split(" & ")
    total_risk_score = sum(risk_scores.get(d.strip(), 0) for d in diseases)
    normalized_risk = total_risk_score / 14  # max = 14
    return normalized_risk


def preprocess_input(input_dict):
    expected_columns = [
        'age', 'number_of_dependants', 'income_lakhs', 'insurance_plan', 'genetical_risk',
        'normalized_risk_score', 'gender_Male', 'region_Northwest', 'region_Southeast',
        'region_Southwest', 'marital_status_Unmarried', 'bmi_category_Obesity',
        'bmi_category_Overweight', 'bmi_category_Underweight', 'smoking_status_Occasional',
        'smoking_status_Regular', 'employment_status_Salaried', 'employment_status_Self-Employed'
    ]

    df = pd.DataFrame(0, columns=expected_columns, index=[0])

    insurance_plan_encoding = {'Bronze': 1, 'Silver': 2, 'Gold': 3}

    # Assign values
    df['age'] = input_dict['Age']
    df['number_of_dependants'] = input_dict['Number of Dependants']
    df['income_lakhs'] = input_dict['Income in Lakhs']
    df['genetical_risk'] = input_dict['Genetical Risk']
    df['insurance_plan'] = insurance_plan_encoding.get(input_dict['Insurance Plan'], 1)
    df['normalized_risk_score'] = calculate_normalized_risk(input_dict['Medical History'])

    if input_dict['Gender'] == 'Male':
        df['gender_Male'] = 1
    if input_dict['Region'] == 'Northwest':
        df['region_Northwest'] = 1
    elif input_dict['Region'] == 'Southeast':
        df['region_Southeast'] = 1
    elif input_dict['Region'] == 'Southwest':
        df['region_Southwest'] = 1
    if input_dict['Marital Status'] == 'Unmarried':
        df['marital_status_Unmarried'] = 1
    if input_dict['BMI Category'] == 'Obesity':
        df['bmi_category_Obesity'] = 1
    elif input_dict['BMI Category'] == 'Overweight':
        df['bmi_category_Overweight'] = 1
    elif input_dict['BMI Category'] == 'Underweight':
        df['bmi_category_Underweight'] = 1
    if input_dict['Smoking Status'] == 'Occasional':
        df['smoking_status_Occasional'] = 1
    elif input_dict['Smoking Status'] == 'Regular':
        df['smoking_status_Regular'] = 1
    if input_dict['Employment Status'] == 'Salaried':
        df['employment_status_Salaried'] = 1
    elif input_dict['Employment Status'] == 'Self-Employed':
        df['employment_status_Self-Employed'] = 1

    return handle_scaling(input_dict['Age'], df)


def handle_scaling(age, df):
    if age <= 25:
        scaler_object = scaler_young
    else:
        scaler_object = scaler_rest

    cols_to_scale = scaler_object['cols_to_scale']
    scaler = scaler_object['scaler']

    df['income_level'] = 0  # placeholder if scaler expects it
    df[cols_to_scale] = scaler.transform(df[cols_to_scale])
    df.drop('income_level', axis='columns', inplace=True)

    return df


def predict(input_dict):
    df = preprocess_input(input_dict)
    if input_dict['Age'] <= 25:
        prediction = model_young.predict(df)
    else:
        prediction = model_rest.predict(df)
    return int(prediction[0])
