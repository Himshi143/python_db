import mysql.connector


def insert_row(sno, sname, salary):
    conn = mysql.connector.connect(host='localhost', database='himshidb', user='root', password='9981618465')

    mycursor = conn.cursor()

    str1 = "insert into  admin_staff(sno, sname, salary) values('%d', '%s', '%f')"
    args = (sno, sname, salary)

    try:
        mycursor.execute(str1 % args)
        conn.commit()
        print('1 row inserted...!!')
    except:
        conn.rollback()

    finally:
        mycursor.close()
        conn.close()


n = int(input("Enter no. of rows :"))

for i in range(n):
    x = int(input("Enter sno :"))
    y = input("Enter sname :")
    z = float(input("enter salary :"))
    insert_row(x, y, z)
    print("------------------------------")
