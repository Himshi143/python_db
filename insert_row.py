import mysql.connector

conn = mysql.connector.connect(host='localhost', database='himshidb', user='root', password='9981618465')

mycursor = conn.cursor()

str1 = "insert into  admin_staff(sno, sname, salary) values(2001, 'Rohit', 12000)"

try:
    mycursor.execute(str1)
    conn.commit()
    print('1 row inserted...!!')
except:
    conn.rollback()
finally:
    mycursor.close()
    conn.close()
