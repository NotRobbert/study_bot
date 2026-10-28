import sqlite3

conn = sqlite3.connect("studydb.db")

cursor =  conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS leaderboard(
    user_id INTEGER PRIMARY KEY,
    seconds INTEGER DEFAULT 0
)
""")