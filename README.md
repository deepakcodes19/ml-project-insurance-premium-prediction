🏥 **Health Insurance Cost Predictor**

A powerful **Streamlit web application** that predicts **health insurance premium costs** based on personal and medical details provided by the user.  
This project leverages **Machine Learning models**, trained separately for **younger** and **older** individuals, to deliver accurate and data-driven premium predictions.  

💡 Designed to make insurance cost estimation simple, transparent, and interactive — right from your browser.


---

## 🚀 Project Overview

The app takes multiple user inputs such as:

- 🧑 Age  
- 👨‍👩‍👧‍👦 Number of dependents  
- 💰 Income (in lakhs)  
- 🧬 Genetical risk  
- 🧾 Insurance plan  
- 💼 Employment status  
- 🚻 Gender  
- 💍 Marital status  
- ⚖️ BMI category  
- 🚬 Smoking habits  
- 🌍 Region  
- 🏥 Medical history  

It then processes these inputs, scales numeric data, encodes categorical values, and passes them to the trained ML model to predict the expected premium cost.

---

## 🔗 Live Demo

👉 **Deployed App:** [https://deepak-ml-project-insurance-premium-prediction.streamlit.app/](https://deepak-ml-project-insurance-premium-prediction.streamlit.app/)

---

## 🧠 How It Works

1. **Input Data** – Users fill in their personal and health information in the Streamlit interface.  
2. **Preprocessing** – The app normalizes and encodes categorical data, and scales numerical features.  
3. **Model Selection** –  
   - If **Age ≤ 25** → uses `model_young`  
   - Else → uses `model_rest`  
4. **Prediction** – The appropriate model outputs the predicted premium amount.

---

## 🔗 Live Demo

👉 **Deployed App:** [https://deepak-ml-project-insurance-premium-prediction.streamlit.app/](https://deepak-ml-project-insurance-premium-prediction.streamlit.app/)


## 🧩 Project Structure

ml-project-insurance-premium-prediction/
│
├── main.py # Streamlit app for user interface
├── prediction_helper.py # Handles preprocessing and model prediction
│
├── artifacts/ # Folder containing trained models & scalers
│ ├── model_young.joblib
│ ├── model_rest.joblib
│ ├── scaler_young.joblib
│ └── scaler_rest.joblib
│
├── requirements.txt # Python dependencies
└── README.md # Project documentation

## ⚙️ Installation & Setup

### 🧩 Prerequisites
Make sure you have **Python 3.x** installed.

### 1️⃣ Clone the repository
```bash
git clone https://github.com/deepakcodes19/ml-project-insurance-premium-prediction.git
cd ml-project-insurance-premium-prediction


## ⚙️ Installation & Setup

### 🧩 Prerequisites
Make sure you have **Python 3.x** installed.

### 1️⃣ Clone the repository
```
git clone https://github.com/deepakcodes19/ml-project-insurance-premium-prediction.git
cd ml-project-insurance-premium-prediction


---
###2️⃣ Create and activate a virtual environment
# On Windows
'''
python -m venv venv
venv\Scripts\activate
---

###3️⃣ Install dependencies
'''
pip install -r requirements.txt
---

###4️⃣ Run the Streamlit app
'''
streamlit run main.py
---

## 🧰 Tech Stack

| Technology     | Purpose                        |
|----------------|--------------------------------|
| Python 3.x     | Core programming language      |
| Streamlit      | Web app framework              |
| scikit-learn   | Model training & prediction    |
| pandas         | Data processing                |
| joblib         | Model serialization            |
| NumPy          | Numerical computations         |

---

## 👨‍💻 Author

**Deepak Yadav**  
🔗 GitHub: [deepakcodes19](https://github.com/deepakcodes19)

---

## ⭐ Contribute

Contributions, issues, and feature requests are welcome!  
Feel free to open a pull request or report an issue on GitHub.

---

## 📜 License

This project is open-source and available under the **MIT License**.

---

### ✨ Made with ❤️ and Machine Learning by Deepak Yadav
```

