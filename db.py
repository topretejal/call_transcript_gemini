import sqlite3
import datetime

DB_FILE = "chat_history.db"

def init_db(db_file=DB_FILE):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chat_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            question TEXT,
            answer TEXT,
            language TEXT
        )
    """)
    conn.commit()

def save_chat_history(question, answer, language, db_file=DB_FILE):
    timestamp = datetime.datetime.utcnow().isoformat()
    print("in db saving a:", answer)
    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO chat_history (timestamp, question, answer, language) VALUES (?, ?, ?, ?)",
            (timestamp, question, answer, language)
        )
        conn.commit()
        # cursor.execute("SELECT question, answer FROM chat_history WHERE question = ?", (question,))
        # row = cursor.fetchone()
        # print("ROW is", row)

