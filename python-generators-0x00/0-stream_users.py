import mysql.connector

def stream_users():
    con = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database= 'ALX_prodev '
    )

    cursor = con.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data")

    for row in cursor:
        yield row
    
    cursor.close()
    con.close()
    