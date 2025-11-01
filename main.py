import streamlit as st
from prediction_helper import predict

st.set_page_config(page_title="Health Insurance Cost Predictor", layout="wide")

st.title('🏥 Health Insurance Cost Predictor')

categorical_options = {
    'Gender': ['Male', 'Female'],
    'Marital Status': ['Unmarried', 'Married'],
    'BMI Category': ['Normal', 'Obesity', 'Overweight', 'Underweight'],
    'Smoking Status': ['No Smoking', 'Regular', 'Occasional'],
    'Employment Status': ['Salaried', 'Self-Employed', 'Freelancer'],
    'Region': ['Northwest', 'Southeast', 'Northeast', 'Southwest'],
    'Medical History': [
        'No Disease', 'Diabetes', 'High blood pressure', 'Diabetes & High blood pressure',
        'Thyroid', 'Heart disease', 'High blood pressure & Heart disease',
        'Diabetes & Thyroid', 'Diabetes & Heart disease'
    ],
    'Insurance Plan': ['Bronze', 'Silver', 'Gold']
}

# Input layout
cols = st.columns(3)

age = cols[0].number_input('Age', min_value=18, step=1, max_value=100)
number_of_dependants = cols[1].number_input('Number of Dependants', min_value=0, step=1, max_value=20)
income_lakhs = cols[2].number_input('Income in Lakhs', step=1, min_value=0, max_value=200)

cols2 = st.columns(3)
genetical_risk = cols2[0].number_input('Genetical Risk (0–5)', step=1, min_value=0, max_value=5)
insurance_plan = cols2[1].selectbox('Insurance Plan', categorical_options['Insurance Plan'])
employment_status = cols2[2].selectbox('Employment Status', categorical_options['Employment Status'])

cols3 = st.columns(3)
gender = cols3[0].selectbox('Gender', categorical_options['Gender'])
marital_status = cols3[1].selectbox('Marital Status', categorical_options['Marital Status'])
bmi_category = cols3[2].selectbox('BMI Category', categorical_options['BMI Category'])

cols4 = st.columns(3)
smoking_status = cols4[0].selectbox('Smoking Status', categorical_options['Smoking Status'])
region = cols4[1].selectbox('Region', categorical_options['Region'])
medical_history = cols4[2].selectbox('Medical History', categorical_options['Medical History'])

input_dict = {
    'Age': age,
    'Number of Dependants': number_of_dependants,
    'Income in Lakhs': income_lakhs,
    'Genetical Risk': genetical_risk,
    'Insurance Plan': insurance_plan,
    'Employment Status': employment_status,
    'Gender': gender,
    'Marital Status': marital_status,
    'BMI Category': bmi_category,
    'Smoking Status': smoking_status,
    'Region': region,
    'Medical History': medical_history
}

if st.button('Predict'):
    try:
        prediction = predict(input_dict)
        st.success(f'💰 Predicted Health Insurance Cost: ₹ {prediction:,}')
    except Exception as e:
        st.error(f"⚠️ Error: {e}")
