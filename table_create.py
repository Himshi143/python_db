import mysql.connector

conn = mysql.connector.connect(host='localhost', database='himshidb', user='root', password='9981618465')

mycursor = conn.cursor()

mycursor.execute("drop table if exists emp")

str1 = "create table admin_staff(sno int, sname char(20), salary float )"

mycursor.execute(str1)
print('Table Created....!!!')

mycursor.close()
conn.close()

