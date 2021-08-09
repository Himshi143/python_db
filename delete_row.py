import mysql.connector


def delete_row(sname):
    conn = mysql.connector.connect(host='localhost', database='himshidb', user='root', password='9981618465')

    mycursor = conn.cursor()

    str1 = "delete from admin_staff where sname = '%s'"
    args = (sname)

    try:
        mycursor.execute(str1 % args)
        conn.commit()
        print('1 row deleted...!!')
    except:
        conn.rollback()

    finally:
        mycursor.close()
        conn.close()


y = input("Enter sname :")
delete_row(y)
