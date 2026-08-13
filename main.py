from pathlib import Path
import json
import random
from datetime import datetime
import joblib
import pandas as pd
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

from database import init_db, add_transaction, get_transactions, get_stats

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "fraud_model.pkl"
if not MODEL_PATH.exists():
    raise RuntimeError("fraud_model.pkl not found. Run: python train_model.py")

model = joblib.load(MODEL_PATH)
init_db()

app = FastAPI(
    title="SmartBank Sentinel",
    description="AI-powered banking transaction risk and fraud detection",
    version="1.0.0"
)

class Transaction(BaseModel):
    customer_id: str = Field(default="C1024", min_length=2, max_length=30)
    amount: float = Field(gt=0)
    new_device: int = Field(ge=0, le=1)
    unusual_location: int = Field(ge=0, le=1)
    unusual_time: int = Field(ge=0, le=1)
    new_merchant: int = Field(ge=0, le=1)
    transaction_count: int = Field(ge=1, le=100)

def analyze(tx):
    X = pd.DataFrame([{
        "amount": tx.amount,
        "new_device": tx.new_device,
        "unusual_location": tx.unusual_location,
        "unusual_time": tx.unusual_time,
        "new_merchant": tx.new_merchant,
        "transaction_count": tx.transaction_count
    }])

    probability = float(model.predict_proba(X)[0][1])
    score = round(probability * 100, 2)

    reasons = []
    if tx.amount > 10000:
        reasons.append("Transaction amount is unusually high")
    if tx.amount > 30000:
        reasons.append("Amount is far above the customer's normal range")
    if tx.new_device:
        reasons.append("Transaction originated from a new device")
    if tx.unusual_location:
        reasons.append("Transaction location is unusual")
    if tx.unusual_time:
        reasons.append("Transaction occurred at an unusual time")
    if tx.new_merchant:
        reasons.append("Merchant is new for this customer")
    if tx.transaction_count > 8:
        reasons.append("High transaction velocity detected")

    if score >= 70:
        status = "HIGH RISK"
        recommendation = "Additional customer verification required"
    elif score >= 40:
        status = "MEDIUM RISK"
        recommendation = "Transaction should be reviewed"
    else:
        status = "LOW RISK"
        recommendation = "Transaction appears normal"

    return score, status, recommendation, reasons

@app.get("/")
def home():
    return FileResponse(BASE_DIR / "static" / "index.html")

@app.get("/api/health")
def health():
    return {"status": "online", "service": "SmartBank Sentinel"}

@app.get("/api/stats")
def stats():
    return get_stats()

@app.get("/api/transactions")
def transactions():
    return get_transactions()


def generate_simulated_transaction():
    customer_id = random.choice(["C1024","C1088","C2041","C3055","C4112"])
    suspicious = random.random() < 0.18
    if suspicious:
        amount=random.uniform(12000,95000); new_device=random.choice([0,1,1])
        unusual_location=random.choice([0,1,1]); unusual_time=random.choice([0,1,1])
        new_merchant=random.choice([0,1]); transaction_count=random.randint(7,15)
    else:
        amount=random.uniform(100,6000); new_device=random.choice([0,0,0,1])
        unusual_location=0; unusual_time=random.choice([0,0,1])
        new_merchant=random.choice([0,0,1]); transaction_count=random.randint(1,6)
    return Transaction(customer_id=customer_id,amount=round(amount,2),
        new_device=new_device,unusual_location=unusual_location,
        unusual_time=unusual_time,new_merchant=new_merchant,
        transaction_count=transaction_count)

@app.post("/api/simulate-transaction")
def simulate_transaction():
    tx=generate_simulated_transaction()
    score,status,recommendation,reasons=analyze(tx)
    row_id=add_transaction((tx.customer_id,tx.amount,tx.new_device,
        tx.unusual_location,tx.unusual_time,tx.new_merchant,tx.transaction_count,
        score,status,recommendation,json.dumps(reasons)))
    return {"transaction_id":row_id,"customer_id":tx.customer_id,"amount":tx.amount,
        "risk_score":score,"status":status,"recommendation":recommendation,
        "reasons":reasons,"timestamp":datetime.now().strftime("%H:%M:%S")}

@app.post("/api/check-transaction")
def check_transaction(tx: Transaction):
    score, status, recommendation, reasons = analyze(tx)

    row_id = add_transaction((
        tx.customer_id, tx.amount, tx.new_device, tx.unusual_location,
        tx.unusual_time, tx.new_merchant, tx.transaction_count,
        score, status, recommendation, json.dumps(reasons)
    ))

    return {
        "transaction_id": row_id,
        "customer_id": tx.customer_id,
        "risk_score": score,
        "status": status,
        "recommendation": recommendation,
        "reasons": reasons
    }
