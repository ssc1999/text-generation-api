import sqlite3
from typing import List, Tuple

DB_NAME = "history.db"

def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                prompt TEXT NOT NULL,
                generated_text TEXT NOT NULL
            )
        """)
        conn.commit()

def save_request(prompt: str, generated_text: str):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO history (prompt, generated_text)
            VALUES (?, ?)
        """, (prompt, generated_text))
        conn.commit()

def fetch_history() -> List[Tuple[int, str, str]]:
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id, prompt, generated_text FROM history
            ORDER BY id DESC
        """)
        return cursor.fetchall()