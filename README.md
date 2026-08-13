# SmartBank Sentinel 🏦

AI-powered banking transaction risk and fraud detection system.

## What it does
SmartBank Sentinel learns transaction patterns and evaluates new transactions using a machine-learning model. It produces:
- Risk score (0–100)
- Low / Medium / High risk classification
- Human-readable reasons for the alert
- Transaction history
- Dashboard statistics

> This is an educational portfolio project using synthetic transaction data. It is not intended for real banking decisions.

## Tech Stack
- Python
- FastAPI
- Scikit-learn
- SQLite
- HTML/CSS/JavaScript
- Random Forest
- Synthetic data generation

## Features
1. ML-based transaction risk prediction
2. Rule-based explanation engine
3. Transaction storage
4. Dashboard with risk statistics
5. REST API
6. Responsive web interface

## Run locally

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

pip install -r requirements.txt
python train_model.py
python -m uvicorn main:app --reload
```

Open http://127.0.0.1:8000

API documentation: http://127.0.0.1:8000/docs

## Example transaction

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

## Project flow

Transaction → Feature extraction → ML risk prediction → Explanation engine → Risk score → Alert/dashboard

## Future improvements
- Real public fraud dataset
- PostgreSQL
- Isolation Forest / XGBoost comparison
- Graph-based fraud detection
- JWT authentication
- Email/SMS alert simulation
- Docker deployment
