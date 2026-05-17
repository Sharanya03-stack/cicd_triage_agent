import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "metrics.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS savings_ledger (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            scenario_name TEXT,
            raw_lines_processed INTEGER,
            estimated_premium_cost REAL,
            actual_cascade_cost REAL,
            dollars_saved REAL
        )
    ''')
    conn.commit()
    conn.close()

def log_savings(scenario_name, raw_lines, premium_cost, cascade_cost):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    saved = premium_cost - cascade_cost
    cursor.execute('''
        INSERT INTO savings_ledger (scenario_name, raw_lines_processed, estimated_premium_cost, actual_cascade_cost, dollars_saved)
        VALUES (?, ?, ?, ?, ?)
    ''', (scenario_name, raw_lines, premium_cost, cascade_cost, saved))
    conn.commit()
    conn.close()

def get_total_savings():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT SUM(raw_lines_processed), SUM(dollars_saved) FROM savings_ledger')
    row = cursor.fetchone()
    conn.close()
    return (row[0] if row[0] else 0, row[1] if row[1] else 0.0)

init_db()