# 🏥 Health Insurance Cost Predictor

A **Streamlit web app** that predicts **health insurance premium costs** based on user-provided personal and medical details. This project uses **Machine Learning models** (trained separately for young and older individuals) to estimate insurance premiums accurately.

---

## 🚀 Project Overview

The app takes multiple user inputs such as:
* Age
* Number of dependents
* Income (in lakhs)
* Genetical risk
* Insurance plan
* Employment status
* Gender
* Marital status
* BMI category
* Smoking habits
* Region
* Medical history

It then processes these inputs, scales numeric data, encodes categorical values, and passes them to the trained ML model to predict the **expected premium cost**.

### 🔗 Live Demo
My Deployed Project link: [https://deepak-ml-project-insurance-premium-prediction.streamlit.app/](https://deepak-ml-project-insurance-premium-prediction.streamlit.app/)

---

## 🧠 How It Works

1.  **Input Data** — Users fill in their personal and health information in the Streamlit interface.
2.  **Preprocessing** — The app normalizes and encodes categorical data, and scales numerical features.
3.  **Model Selection** —
    * If age $\le 25 \rightarrow$ uses `model_young`
    * Else $\rightarrow$ uses `model_rest`
4.  **Prediction** — The appropriate model outputs the predicted premium amount.

---
## 🧩 Project Structure
ml-project-insurance-premium-prediction/
│
├── main.py                     # Streamlit app for user interface
├── prediction_helper.py        # Handles preprocessing and model prediction
│
├── artifacts/                  # Folder containing trained models & scalers
│   ├── model_young.joblib
│   ├── model_rest.joblib
│   ├── scaler_young.joblib
│   └── scaler_rest.joblib
│
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation


## ⚙️ Installation & Setup

## Prerequisites
Make sure you have Python 3.x installed.

## 1️⃣ Clone the repository
```bash
git clone [https://github.com/deepakcodes19/ml-project-insurance-premium-prediction.git](https://github.com/deepakcodes19/ml-project-insurance-premium-prediction.git)
cd ml-project-insurance-premium-prediction

# On Windows
python -m venv venv
venv\Scripts\activate

# On Mac/Linux
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

streamlit run main.py
---
---
## 🧰 Tech Stack

The project utilizes the following technologies:
* **Python 3.x**
* **Streamlit** – Web app framework
* **scikit-learn** – Model training and prediction
* **pandas** – Data processing
* **joblib** – Model serialization
* **NumPy** – Numerical computations

---

## 👨‍💻 Author

**Deepak Yadav**
* 🔗 [GitHub: deepakcodes19](https://github.com/deepakcodes19)

---

## ⭐ Contribute

Contributions, issues, and feature requests are welcome! Feel free to **open a pull request** or **report an issue** on GitHub.

---

## 📜 License

This project is open-source and available under the **MIT License**.

---

✨ *Made with ❤️ and Machine Learning by Deepak Yadav*
