import mysql.connector
from tkinter import *
root = Tk()    # create root window


def retrieve_rows(eno):  # A function that takes employee number & displays the row
    conn = mysql.connector.connect(host='localhost', database='himshidb', user='root', password='9981618465')
    mycursor = conn.cursor()   # prepare a cursor object using cursor() method
    str1 = "select * from emptab where eno = '%d'"  # SQL query to retrieve a row
    args = eno
    mycursor.execute(str1 % args)  # execute query using execute method()
    row = mycursor.fetchone()  # get only one row
    if row is not None:  # if the row exists display it using a label
        lbl = Label(text=row, font=('Arial', 14)).place(x=50, y=200)
    mycursor.close()  # close connection
    conn.close()


def display(self):  # function that takes input from entry widget
    str1 = e1.get()  # retrieve the value from the entry widget
    lbl = Label(text='You entered:' + str1, font=('Arial', 14)).place(x=50, y=150)  # display a value using label
    retrieve_rows(int(str1))  # call the function that retrieves the row


f = Frame(root, height=350, width=600)   # create a frame as child to root window
f.propagate(0)  # let the frame will not shrink
f.pack()  # attach the frame to root window
l1 = Label(text='Enter Employee number:', font=('Arial', 14))  # label

# create entry widget for accepting employee number
e1 = Entry(f, width=15, fg='red', bg='yellow', font=('Arial', 14))

e1.bind("<Return>", display)  # when user presses Enter, bind that event to display method

# place label and entry widgets in the frame
l1.place(x=50, y=100)
e1.place(x=300, y=100)

# handle the events
root.mainloop()
