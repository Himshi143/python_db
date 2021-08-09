import mysql.connector

conn = mysql.connector.connect(host='localhost', database='himshidb', user='root', password='9981618465')

mycursor = conn.cursor()

mycursor.execute("select * from admin_staff")

# row = mycursor.fetchone()
# while row is not None:
#   print(row)
#   row = mycursor.fetchone()

rows = mycursor.fetchall()
print('Total no. of rows', mycursor.rowcount)
print('------------------------------------')
print('\tSNo.', '\tSNAME', '\t\tSALARY')
print('------------------------------------')
for r in rows:
    sno = r[0]
    sname = r[1]
    salary = r[2]
    print('| %-6d | %-10s | %-10.2f |' % (sno, sname, salary))

print('------------------------------------')

mycursor.close()
conn.close()
