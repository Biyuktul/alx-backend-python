import mysql.connector
import csv
from mysql.connector import errorcode


def connect_db():
    try:
        connection = mysql.connector.connect(
            host = 'localhost',
            username = 'root',
            password = ''
        )
        return connection
    except mysql.connector.Error as err:
        print("Failed Connecting to DB: ", err)
        return None

def create_database(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
    finally:
        cursor.close()


def connect_to_prodev():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='your_username',
            password='your_password',
            database='ALX_prodev'
        )
        return connection
    except mysql.connector.Error as err:
        print("Failed to connect to ALX_prodev:", err)
        return None

def create_table(connection):
    cursor = connection.cursor()
    create_query = """
    CREATE TABLE IF NOT EXISTS user_data (
        user_id VARCHAR(36) PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        age DECIMAL NOT NULL,
        INDEX (user_id)
    )
    """
    try:
        cursor.execute(create_query)
    finally:
        cursor.close()

def insert_data(connection, data):
    cursor = connection.cursor()
    insert_query = """
    INSERT IGNORE INTO user_data (user_id, name, email, age)
    VALUES (%s, %s, %s, %s)
    """
    try:
        cursor.executemany(insert_query, data)
        connection.commit()
    finally:
        cursor.close()

# Utility to read CSV
def load_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return [
            (row['user_id'], row['name'], row['email'], row['age'])
            for row in reader
        ]

if __name__ == "__main__":
    base_conn = connect_db()
    if base_conn:
        create_database(base_conn)
        base_conn.close()

    db_conn = connect_to_prodev()
    if db_conn:
        create_table(db_conn)
        csv_data = load_csv('user_data.csv')
        insert_data(db_conn, csv_data)
        db_conn.close()
