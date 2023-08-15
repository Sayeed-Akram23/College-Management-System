from tkinter import Tk, Label, Entry, Button, StringVar
import sqlite3
from admin import admin_main

def loginpage():
    con = sqlite3.connect('database_name.db')
    c = con.cursor()

    root = Tk()
    root.geometry('380x250+480+120')
    root.title("LOGIN PAGE")
    title = Label(root, text='   LOGIN  PAGE', font=("times new roman", 20, "bold"))
    title.grid(row=0, column=0, columnspan=2)

    usernamelabel = Label(root, text="  Enter Username:", font=("arial", 13))
    usernamelabel.grid(row=1, column=0)
    username = StringVar()
    usernameEntry = Entry(root, textvariable=username, font=("arial", 13))
    usernameEntry.grid(row=1, column=1)

    passwordlabel = Label(root, text="  Enter Password:", font=("arial", 13))
    passwordlabel.grid(row=2, column=0)
    password = StringVar()
    passwordEntry = Entry(root, textvariable=password, show='*', font=("arial", 13))
    passwordEntry.grid(row=2, column=1, columnspan=2)

    def submit():
        submit_win = root
        alldata = c.execute("SELECT * FROM login_details")
        for data in alldata:
            if username.get() == data[1] and password.get() == data[2]:
                admin_main()
            else:
                myLabel = Label(submit_win, text="Incorrect username or password", font=('arial', 13))
                myLabel.grid(row=3, column=0, columnspan=2)

    sub_btn = Button(root, text='Submit', command=submit, font=("arial", 13))
    sub_btn.grid(row=5, column=1)
    root.mainloop()

def main():
    loginpage()

if __name__ == "__main__":
    main()
