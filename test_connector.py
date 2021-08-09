import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    database='himshidb',
    user='root',
    password='9981618465'
)

mycursor = mydb.cursor()

mycursor.execute("select * from stud")

row = mycursor.fetchall()

print(row)

mycursor.execute("select * from stud")

rows = mycursor.fetchone()

print(rows)


