import sqlite3
from pathlib import Path

DB = Path(__file__).resolve().parent / "smartbank.db"

def get_connection():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id TEXT NOT NULL,
            amount REAL NOT NULL,
            new_device INTEGER NOT NULL,
            unusual_location INTEGER NOT NULL,
            unusual_time INTEGER NOT NULL,
            new_merchant INTEGER NOT NULL,
            transaction_count INTEGER NOT NULL,
            risk_score REAL NOT NULL,
            status TEXT NOT NULL,
            recommendation TEXT NOT NULL,
            reasons TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def add_transaction(data):
    conn = get_connection()
    cur = conn.execute("""
        INSERT INTO transactions
        (customer_id, amount, new_device, unusual_location, unusual_time,
         new_merchant, transaction_count, risk_score, status,
         recommendation, reasons)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, data)
    conn.commit()
    row_id = cur.lastrowid
    conn.close()
    return row_id

def get_transactions(limit=50):
    conn = get_connection()
    rows = conn.execute(
        "SELECT * FROM transactions ORDER BY id DESC LIMIT ?", (limit,)
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]

def get_stats():
    conn = get_connection()
    total = conn.execute("SELECT COUNT(*) FROM transactions").fetchone()[0]
    high = conn.execute("SELECT COUNT(*) FROM transactions WHERE status='HIGH RISK'").fetchone()[0]
    medium = conn.execute("SELECT COUNT(*) FROM transactions WHERE status='MEDIUM RISK'").fetchone()[0]
    low = conn.execute("SELECT COUNT(*) FROM transactions WHERE status='LOW RISK'").fetchone()[0]
    conn.close()
    return {"total": total, "high": high, "medium": medium, "low": low}
