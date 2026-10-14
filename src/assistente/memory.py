import sqlite3
from contextlib import closing
from pathlib import Path

class Memory:
    def __init__(self, path):
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        self.path = path
        with closing(sqlite3.connect(path)) as db, db:
            db.execute("CREATE TABLE IF NOT EXISTS facts (id INTEGER PRIMARY KEY, text TEXT NOT NULL)")

    def add(self, text):
        with closing(sqlite3.connect(self.path)) as db, db:
            db.execute("INSERT INTO facts(text) VALUES (?)", (text,))

    def list(self):
        with closing(sqlite3.connect(self.path)) as db, db:
            return db.execute("SELECT id, text FROM facts ORDER BY id").fetchall()

