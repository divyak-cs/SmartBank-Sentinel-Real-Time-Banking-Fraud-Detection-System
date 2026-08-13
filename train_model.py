import numpy as np
import pandas as pd
import joblib
from pathlib import Path
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

np.random.seed(42)

rows = []
for _ in range(15000):
    amount = np.random.exponential(2500)
    new_device = np.random.binomial(1, 0.12)
    unusual_location = np.random.binomial(1, 0.10)
    unusual_time = np.random.binomial(1, 0.15)
    new_merchant = np.random.binomial(1, 0.20)
    transaction_count = np.random.poisson(4) + 1

    risk = 0
    risk += 2 if amount > 10000 else 0
    risk += 2 if amount > 30000 else 0
    risk += 2 if new_device else 0
    risk += 2 if unusual_location else 0
    risk += 1 if unusual_time else 0
    risk += 1 if new_merchant else 0
    risk += 2 if transaction_count > 8 else 0

    fraud = int(risk >= 5)
    rows.append([amount, new_device, unusual_location, unusual_time,
                 new_merchant, transaction_count, fraud])

df = pd.DataFrame(rows, columns=[
    "amount", "new_device", "unusual_location", "unusual_time",
    "new_merchant", "transaction_count", "fraud"
])

X = df.drop(columns=["fraud"])
y = df["fraud"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = RandomForestClassifier(
    n_estimators=150,
    max_depth=10,
    random_state=42,
    class_weight="balanced"
)
model.fit(X_train, y_train)

print(classification_report(y_test, model.predict(X_test)))
joblib.dump(model, Path(__file__).resolve().parent / "fraud_model.pkl")
print("Saved fraud_model.pkl")
