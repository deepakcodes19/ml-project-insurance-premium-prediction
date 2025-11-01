# 🏥 Health Insurance Cost Predictor

A **Streamlit web app** that predicts **health insurance premium costs** based on user-provided personal and medical details.  
This project uses **Machine Learning models** (trained separately for young and older individuals) to estimate insurance premiums accurately.

---

## 🚀 Project Overview

The app takes multiple user inputs such as:
- Age  
- Number of dependents  
- Income (in lakhs)  
- Genetical risk  
- Insurance plan  
- Employment status  
- Gender  
- Marital status  
- BMI category  
- Smoking habits  
- Region  
- Medical history  

It then processes these inputs, scales numeric data, encodes categorical values, and passes them to the trained ML model to predict the **expected premium cost**.

---

## 🧠 How It Works

1. **Input Data** — Users fill in their personal and health information in the Streamlit interface.  
2. **Preprocessing** — The app normalizes and encodes categorical data, and scales numerical features.  
3. **Model Selection** —  
   - If age ≤ 25 → uses `model_young`  
   - Else → uses `model_rest`
4. **Prediction** — The appropriate model outputs the predicted premium amount.

---

## 🧩 Project Structure

```bash
ml-project-insurance-premium-prediction/
│
├── main.py                      # Streamlit app for user interface
├── prediction_helper.py         # Handles preprocessing and model prediction
│
├── artifacts/                   # Folder containing trained models & scalers
│   ├── model_young.joblib
│   ├── model_rest.joblib
│   ├── scaler_young.joblib
│   └── scaler_rest.joblib
│
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation


## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/deepakcodes19/ml-project-insurance-premium-prediction.git
cd ml-project-insurance-premium-prediction

python -m venv venv
venv\Scripts\activate     # On Windows
# or
source venv/bin/activate  # On Mac/Linux

pip install -r requirements.txt

streamlit run main.py
| Feature         | Example Value                  |
| --------------- | ------------------------------ |
| Age             | 30                             |
| Income in Lakhs | 12                             |
| BMI Category    | Overweight                     |
| Smoking Status  | No Smoking                     |
| Medical History | Diabetes & High blood pressure |
| Region          | Northwest                      |

Predicted Health Insurance Cost: ₹XXXXX

🧰 Tech Stack

Python 3.x

Streamlit – Web app framework

scikit-learn – Model training and prediction

pandas – Data processing

joblib – Model serialization

NumPy – Numerical computations

🧑‍💻 Author

👤 Deepak Yadav
🔗 GitHub: deepakcodes19

⭐ Contribute

Contributions, issues, and feature requests are welcome!
Feel free to open a pull request or issue.

📜 License

This project is open-source and available under the MIT License.

✨ Made with ❤️ and Machine Learning by Deepak Yadav


