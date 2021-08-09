import mysql.connector


def update_row(sno):
    conn = mysql.connector.connect(host='localhost', database='himshidb', user='root', password='9981618465')

    mycursor = conn.cursor()

    str2 = "UPDATE admin_staff SET salary = salary+1000 WHERE sno = '%d'"
    args = (sno)

    try:
        mycursor.execute(str2 % args)
        conn.commit()
        print('Row updated...!!')
    except:
        conn.rollback()

    finally:
        mycursor.close()
        conn.close()


y = int(input("Enter sno :"))
update_row(y)
