import mysql.connector
try:
    conn = mysql.connector.connect(
        host = 'localhost',
        user = 'rooot',
        password = ''
        )
    mycur = conn.cursor()
    mycur.execute(" CREATE DATABASE MHMD")
except mysql.connector.Error as r:
    print(r)
