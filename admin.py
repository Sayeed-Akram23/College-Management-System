import sqlite3
from tkinter import Tk, RIDGE, Label, Frame, Entry, Button
from student import student_main
from teacher import teacher_main
def adminprof():
    root = Tk()
    root.title("MY PROFILE")
    root.geometry('800x400+250+10')

    def change_pwd():
        frame = Frame(root, bd=4, relief=RIDGE)
        frame.place(x=200, y=50, width=400, height=300)

        Label(frame, text="New password", font=('arial', 14)).pack(pady=10)
        e = Entry(frame)
        e.pack()

        Label(frame, text="Re-enter password", font=('arial', 14)).pack(pady=10)
        f = Entry(frame)
        f.pack()

        def submit():
            if e.get() == f.get():
                c.execute("UPDATE login_details SET pwd=?", (e.get(),))
                con.commit()
                Label(root, text="Password changed", font=('arial', 14)).pack()
            else:
                Label(root, text="Passwords don't match", font=('arial', 14)).pack()

        Button(frame, text='Submit', command=submit, font=('arial', 12), width=10).pack(pady=10)

    con = sqlite3.connect('database_name.db')
    c = con.cursor()
    change_pwd()
    root.mainloop()

def admin_main():
    root1 = Tk()
    root1.geometry('800x450+250+10')
    root1.title("ADMIN")

    def action1():
        student_main()

    def action2():
        teacher_main()

    def action3():
        adminprof()

    Label(root1, text='WELCOME ADMIN!', font=("times new roman", 20, "bold")).pack(side='top', pady=10)
    adminframe = Frame(root1, bd=4, relief=RIDGE)
    adminframe.place(x=200, y=50, width=400, height=350)

    Button(adminframe, text="Student Info", command=action1, font=("arial", 15, "bold"), width=20).pack(pady=10)
    Button(adminframe, text="Teacher Info", command=action2, font=("arial", 15, "bold"), width=20).pack(pady=10)
    Button(adminframe, text="My Profile", command=action3, font=("arial", 15, "bold"), width=20).pack(pady=10)

    root1.mainloop()
