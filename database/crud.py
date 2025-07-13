import sqlite3

def add_transaction(amount: float, category: str, description: str, type: str):
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO transactions (amount, category, description, type) VALUES (?, ?, ?, ?)",
                   (amount, category, description, type))
    conn.commit()
    conn.close()




def get_all_transactions():
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transactions ORDER BY date DESC")
    transactions = cursor.fetchall()
    conn.close()
    return transactions