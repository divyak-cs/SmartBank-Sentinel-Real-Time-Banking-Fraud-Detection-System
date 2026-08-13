# 🏦 SmartBank Sentinel

### Real-Time Banking Transaction Risk & Fraud Detection System

SmartBank Sentinel is an AI-powered banking transaction monitoring system built with **Python and FastAPI**. It evaluates transaction characteristics using a **Random Forest machine-learning model** and generates a risk score, risk classification, and human-readable explanations for potentially suspicious transactions.

> **Note:** This is an educational portfolio project built using synthetic transaction data. It is not intended for real-world banking or financial decisions.

---

## 🚀 Key Features

* 🤖 **Machine-learning-based fraud risk prediction**
* 📊 **Transaction risk score from 0–100**
* 🚦 **Low / Medium / High risk classification**
* 🔍 **Human-readable explanations for suspicious transactions**
* 💾 **Transaction storage using SQLite**
* 📈 **Dashboard with transaction and risk statistics**
* 🌐 **REST API built with FastAPI**
* 🖥️ **Interactive web interface**
* ⚡ **Real-time transaction analysis**
* 🧪 **Synthetic transaction data generation for model training**

---

## 🧠 How It Works

The system analyzes transaction-related features such as:

* Transaction amount
* New device
* Unusual location
* Unusual transaction time
* New merchant
* Transaction frequency

The transaction features are passed to a trained **Random Forest classifier**, which predicts the likelihood of suspicious activity.

The system then combines the model prediction with rule-based explanations to produce an understandable risk assessment.

### Project Flow

```text
Transaction
     ↓
Feature Extraction
     ↓
Machine Learning Model
     ↓
Fraud Risk Prediction
     ↓
Risk Score Generation
     ↓
Explanation Engine
     ↓
Risk Classification
     ↓
Dashboard / Alert
```

---

## 📊 Risk Classification

| Risk Score | Classification |
| ---------- | -------------- |
| 0–39       | 🟢 Low Risk    |
| 40–69      | 🟡 Medium Risk |
| 70–100     | 🔴 High Risk   |

The risk score helps prioritize transactions that require further review.

---

## 🛠️ Technology Stack

| Technology              | Purpose                             |
| ----------------------- | ----------------------------------- |
| **Python**              | Core application and ML development |
| **FastAPI**             | Backend REST API                    |
| **Scikit-learn**        | Machine learning                    |
| **Random Forest**       | Fraud risk classification           |
| **Pandas**              | Data processing                     |
| **NumPy**               | Numerical operations                |
| **Joblib**              | Model serialization                 |
| **SQLite**              | Transaction database                |
| **HTML/CSS/JavaScript** | Web interface                       |
| **Uvicorn**             | ASGI server                         |

---

## 📁 Project Structure

```text
SmartBank-Sentinel/
│
├── main.py              # FastAPI application and API endpoints
├── database.py          # SQLite database operations
├── train_model.py       # ML model training
├── fraud_model.pkl      # Trained Random Forest model
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
│
└── static/
    └── index.html       # Web dashboard
```

---

## 🤖 Machine Learning

The project uses a **Random Forest classifier** to evaluate transaction risk.

The model is trained using **synthetically generated transaction data** containing transaction attributes and fraud labels.

The training process is implemented in:

```text
train_model.py
```

The trained model is saved using Joblib:

```text
fraud_model.pkl
```

### Example Transaction

```json
{
  "customer_id": "C1024",
  "amount": 85000,
  "new_device": 1,
  "unusual_location": 1,
  "unusual_time": 1,
  "new_merchant": 1,
  "transaction_count": 10
}
```

---

## 🔌 API

The FastAPI backend provides endpoints for transaction analysis, transaction history, statistics, and application health.

Interactive API documentation is automatically available through FastAPI's Swagger interface:

```text
http://127.0.0.1:8000/docs
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/divyak-cs/SmartBank-Sentinel-Real-Time-Banking-Fraud-Detection-System.git
```

### 2. Navigate to the project

```bash
cd SmartBank-Sentinel-Real-Time-Banking-Fraud-Detection-System
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

#### Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

#### Windows Command Prompt

```cmd
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Train the model

```bash
python train_model.py
```

### 7. Start the FastAPI server

```bash
python -m uvicorn main:app --reload
```

---

## 🌐 Run the Application

Once the server starts, open:

```text
http://127.0.0.1:8000
```

### API Documentation

```text
http://127.0.0.1:8000/docs
```

---

## 🗄️ Database

SmartBank Sentinel uses **SQLite** to store transaction information and support transaction history and dashboard statistics.

Database operations are handled through:

```text
database.py
```

---

## 🔮 Future Improvements

Possible future enhancements include:

* Training and evaluation using a real publicly available fraud dataset
* PostgreSQL database integration
* Comparison of Random Forest with Isolation Forest and XGBoost
* Graph-based fraud detection
* JWT-based authentication and authorization
* Email/SMS fraud alert simulation
* Docker containerization
* Cloud deployment
* Model monitoring and periodic retraining

---

## 🎯 Learning Outcomes

Through this project, the following concepts were explored:

* REST API development using FastAPI
* Machine learning model training and inference
* Transaction feature engineering
* Fraud-risk classification
* Rule-based explanation generation
* SQLite database integration
* Frontend-backend integration
* Model serialization and loading
* API testing with Swagger/OpenAPI
* Python virtual environment and dependency management

---

## 👩‍💻 Author

**Divya K S**

Computer Science & Engineering — AI & Data Science

### GitHub

[SmartBank Sentinel Repository](https://github.com/divyak-cs/SmartBank-Sentinel-Real-Time-Banking-Fraud-Detection-System)
