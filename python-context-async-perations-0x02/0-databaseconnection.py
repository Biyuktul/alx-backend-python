import sqlite3
 
class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self.conn
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()

with DatabaseConnection('airbnb') as db:
    cursor = db.cursor()
    users = cursor.execute('SELECT * FROM users')
    for user in users:
        print(user) 