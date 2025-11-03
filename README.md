# 🏥 Health Insurance Cost Predictor

A **Streamlit web app** that predicts **health insurance premium costs** based on user-provided personal and medical details.  
This project leverages **Machine Learning models**, trained separately for **younger** and **older** individuals, to estimate insurance premiums with high accuracy.  

💡 **Goal:** To simplify health insurance premium estimation using an interactive, AI-driven tool accessible to everyone.

---

## 🚀 Project Overview

The app collects various personal and medical details such as:

- 🧍‍♂️ **Age**  
- 👨‍👩‍👧‍👦 **Number of Dependents**  
- 💰 **Income (in Lakhs)**  
- 🧬 **Genetical Risk**  
- 🩺 **Insurance Plan**  
- 💼 **Employment Status**  
- 🚻 **Gender**  
- 💍 **Marital Status**  
- ⚖️ **BMI Category**  
- 🚬 **Smoking Habits**  
- 🌍 **Region**  
- 🧾 **Medical History**

It then processes these inputs, scales numerical data, encodes categorical values, and feeds them into a **trained ML model** to predict the **expected insurance premium**.

---

## 🔗 Live Demo

👉 **Try it here:** [Health Insurance Cost Predictor](https://deepak-ml-project-insurance-premium-prediction.streamlit.app/)

---

## 🖼️ App Preview

Here’s how the **Health Insurance Cost Predictor** app looks 👇  


<img width="1402" height="707" alt="image" src="https://github.com/user-attachments/assets/58109e6c-5088-475b-9c0d-e8faa310622c" />



## 🧠 How It Works

1️⃣ **Input Data** — Users enter their personal and health information through a Streamlit interface.  
2️⃣ **Preprocessing** — Data is cleaned, scaled, and encoded using trained scalers and encoders.  
3️⃣ **Model Selection** —  
   - If **Age ≤ 25** → uses `model_young`  
   - If **Age > 25** → uses `model_rest`  
4️⃣ **Prediction** — The chosen model outputs the estimated **insurance premium cost**.  
5️⃣ **Result Display** — Streamlit displays the predicted premium with a clean and simple UI.

---

## 🧩 Project Structure

```

ml-project-insurance-premium-prediction/
│
├── main.py                  # Streamlit app (frontend)
├── prediction_helper.py     # Handles preprocessing & model prediction
│
├── artifacts/               # Contains trained models & scalers
│   ├── model_young.joblib
│   ├── model_rest.joblib
│   ├── scaler_young.joblib
│   └── scaler_rest.joblib
│
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation

````

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/deepakcodes19/ml-project-insurance-premium-prediction.git
cd ml-project-insurance-premium-prediction
````

### 2️⃣ Create and Activate a Virtual Environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Streamlit App

```bash
streamlit run main.py
```

---

## 🧰 Tech Stack

| Technology          | Purpose                     |
| ------------------- | --------------------------- |
| 🐍 **Python 3.x**   | Core programming language   |
| 🖥️ **Streamlit**   | Web app framework           |
| 🤖 **scikit-learn** | Model training & prediction |
| 📊 **pandas**       | Data processing             |
| 💾 **joblib**       | Model serialization         |
| 🔢 **NumPy**        | Numerical computations      |

---

## 👨‍💻 Author

**Deepak Yadav**
🔗 [GitHub: deepakcodes19](https://github.com/deepakcodes19)

---

## ⭐ Contribute

Contributions, issues, and feature requests are welcome!
Feel free to **open a pull request** or **report an issue** on GitHub.

---

## 📜 License

This project is open-source and available under the **MIT License**.

---

✨ *Made with ❤️ and Machine Learning by Deepak Yadav*

```

