
import sqlite3
from tkinter import BOTH, BOTTOM, END, HORIZONTAL, RIDGE, RIGHT, TOP, VERTICAL, X, Y, Scrollbar, StringVar, Tk, Toplevel, Label, Frame, Entry, Button, ttk


def stuform():
    def submit():
        con = sqlite3.connect('database_name.db')
        c = con.cursor()
        #insert_val=[stud_id.get(), name.get(), dob.get(), gender.get(), name_father.get(),name_mother.get(),branch_id.get(), sem.get(), sec.get(), admn_date.get(),grad_yr.get(), course_dur.get(),blood_grp.get(), stud_no.get(), no_father.get(), no_mother.get(), stud_email.get(), email_father.get(), email_mother.get(), address.get('1.0',END),status.get()]
        c.execute("INSERT INTO stud_info VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (stud_id.get(), name.get(), dob.get(), gender.get(), name_father.get(), name_mother.get(), branch_id.get(), sem.get(), sec.get(
        ), admn_date.get(), grad_yr.get(), course_dur.get(), blood_grp.get(), stud_no.get(), no_father.get(), no_mother.get(), stud_email.get(), email_father.get(), email_mother.get(), address.get(), status.get()))
        con.commit()
        clearform()
        return

    def clearform():
        stud_id.set("")
        name.set("")
        dob.set("")
        gender.set("")
        name_father.set("")
        name_mother.set("")
        branch_id.set("")
        sem.set("")
        sec.set("")
        admn_date.set("")
        course_dur.set("")
        grad_yr.set("")
        course_dur.set("")
        blood_grp.set("")
        stud_no.set("")
        no_father.set("")
        no_mother.set("")
        stud_email.set("")
        email_father.set("")
        email_mother.set("")
        address.set("")
        status.set("")

    root = Tk()
    root.title("ADD STUDENT")
    root.geometry('1230x640+20+10')

    title = Label(root, text='ADD STUDENT', font=(
        "times new roman", 20, "bold"))
    title.pack(side=TOP)

    main_frame1 = Frame(root, bd=4, relief=RIDGE)
    main_frame1.place(x=30, y=50, width=550, height=570)
    title = Label(main_frame1, text='BASIC INFORMATION',
                  font=("arial", 15, "bold"))
    title.grid(row=0, column=0, sticky='w')

    main_frame2 = Frame(root, bd=4, relief=RIDGE)
    main_frame2.place(x=650, y=50, width=550, height=300)
    title = Label(main_frame2, text='PARENT DETAILS',
                  font=("arial", 15, "bold"))
    title.grid(row=0, column=0, sticky='w')

    main_frame3 = Frame(root, bd=4, relief=RIDGE)
    main_frame3.place(x=650, y=360, width=550, height=260)
    title = Label(main_frame3, text='ACADEMIC DETAILS',
                  font=("arial", 15, "bold"))
    title.grid(row=0, column=0, sticky='w')

    # for student id
    stud_idLabel = Label(main_frame1, text="Enter Student ID:", font=(
        "arial", 13)).grid(row=1, column=0, pady=10, sticky='w')
    stud_id = StringVar(root)
    stud_idEntry = Entry(main_frame1, textvariable=stud_id, font=("arial", 13))
    stud_idEntry.grid(row=1, column=1, pady=10)

    # for student name
    nameLabel = Label(main_frame1, text="Enter Student Name:", font=(
        "arial", 13)).grid(row=2, column=0, pady=10, sticky='w')
    name = StringVar(root)
    nameEntry = Entry(main_frame1, textvariable=name, font=("arial", 13))
    nameEntry.grid(row=2, column=1, pady=10)

    # for date of birth
    dobLabel = Label(main_frame1, text="Enter Date Of Birth:", font=(
        "arial", 13)).grid(row=3, column=0, pady=10, sticky='w')
    dob = StringVar(root)
    dobEntry = Entry(main_frame1, textvariable=dob, font=("arial", 13))
    dobEntry.grid(row=3, column=1, pady=10)

    # for gender
    genLabel = Label(main_frame1, text="Enter Gender:", font=(
        "arial", 13)).grid(row=4, column=0, pady=10, sticky='w')
    gender = StringVar(root)
    gendrop = ttk.Combobox(main_frame1, textvariable=gender,
                           font=("arial", 11), state='readonly')
    gendrop['values'] = ("Female", "Male", "Other")
    gendrop.grid(row=4, column=1, pady=10)

    # for blood group
    blood_grpLabel = Label(main_frame1, text="Enter Blood Group:", font=(
        "arial", 13)).grid(row=6, column=0, pady=10, sticky='w')
    blood_grp = StringVar(root)
    blood_grpdrop = ttk.Combobox(
        main_frame1, textvariable=blood_grp, font=("arial", 11), state='readonly')
    blood_grpdrop['values'] = (
        'A+', 'A-', 'B+', 'B-', 'O+', ' O-', 'AB+', 'AB-')
    blood_grpdrop.grid(row=6, column=1, pady=10)

    # for address
    addressLabel = Label(main_frame1, text="Enter Address:", font=(
        "arial", 13)).grid(row=7, column=0, pady=10, sticky='w')
    address = StringVar(root)
    addressEntry = Entry(main_frame1, textvariable=address, font=("arial", 13))
    addressEntry.grid(row=7, column=1, pady=10)

    # for student's number
    stu_noLabel = Label(main_frame1, text="Enter Student's Number:", font=(
        "arial", 13)).grid(row=8, column=0, pady=10, sticky='w')
    stud_no = StringVar(root)
    stu_noEntry = Entry(main_frame1, textvariable=stud_no, font=("arial", 13))
    stu_noEntry.grid(row=8, column=1, pady=10)

    # for student's email id
    stu_emailLabel = Label(main_frame1, text="Enter Student's Email ID:", font=(
        "arial", 13)).grid(row=9, column=0, pady=10, sticky='w')
    stud_email = StringVar(root)
    stu_emailEntry = Entry(
        main_frame1, textvariable=stud_email, font=("arial", 13))
    stu_emailEntry.grid(row=9, column=1, pady=10)

    # for branch id
    branch_idLabel = Label(main_frame1, text="Enter Branch ID:", font=(
        "arial", 13)).grid(row=10, column=0, pady=10, sticky='w')
    branch_id = StringVar(root)
    branch_idEntry = Entry(
        main_frame1, textvariable=branch_id, font=("arial", 13))
    branch_idEntry.grid(row=10, column=1, pady=10)

    # for admission year
    admn_dateLabel = Label(main_frame1, text="Enter Admission Date:", font=(
        "arial", 13)).grid(row=11, column=0, pady=10, sticky='w')
    admn_date = StringVar(root)
    admn_dateEntry = Entry(
        main_frame1, textvariable=admn_date, font=("arial", 13))
    admn_dateEntry.grid(row=11, column=1)

    # --------------------------------------------------------------------------------------------------------------------

    # for father's name
    name_fatherLabel = Label(main_frame2, text="Enter Father's name:", font=(
        "arial", 13)).grid(row=1, column=0, pady=10, sticky='w')
    name_father = StringVar(root)
    name_fatherEntry = Entry(
        main_frame2, textvariable=name_father, font=("arial", 13))
    name_fatherEntry.grid(row=1, column=1, pady=10)

    # for father's number
    no_fatherLabel = Label(main_frame2, text="Enter Father's number:", font=(
        "arial", 13)).grid(row=2, column=0, pady=10, sticky='w')
    no_father = StringVar(root)
    no_fatherEnrty = Entry(
        main_frame2, textvariable=no_father, font=("arial", 13))
    no_fatherEnrty.grid(row=2, column=1, pady=10)

    # for father's email id
    email_fatherLabel = Label(main_frame2, text="Enter Father's Email ID:", font=(
        "arial", 13)).grid(row=3, column=0, pady=10, sticky='w')
    email_father = StringVar(root)
    email_fatherEntry = Entry(
        main_frame2, textvariable=email_father, font=("arial", 13))
    email_fatherEntry.grid(row=3, column=1, pady=10)

    # for mother's name
    name_motherLabel = Label(main_frame2, text="Enter Mother's name:", font=(
        "arial", 13)).grid(row=4, column=0, pady=10, sticky='w')
    name_mother = StringVar(root)
    name_motherEntry = Entry(
        main_frame2, textvariable=name_mother, font=("arial", 13))
    name_motherEntry.grid(row=4, column=1, pady=10)

    # for mother's number
    no_motherLabel = Label(main_frame2, text="Enter Mother's number:", font=(
        "arial", 13)).grid(row=5, column=0, pady=10, sticky='w')
    no_mother = StringVar(root)
    no_motherEntry = Entry(
        main_frame2, textvariable=no_mother, font=("arial", 13))
    no_motherEntry.grid(row=5, column=1, pady=10)

    # for mother's email id
    email_motherLabel = Label(main_frame2, text="Enter Mother's Email ID:", font=(
        "arial", 13)).grid(row=6, column=0, pady=10, sticky='w')
    email_mother = StringVar(root)
    email_motherEntry = Entry(
        main_frame2, textvariable=email_mother, font=("arial", 13))
    email_motherEntry.grid(row=6, column=1, pady=10)

    # for semester
    semLabel = Label(main_frame3, text="Enter Semester:", font=(
        "arial", 13)).grid(row=1, column=0, pady=10, sticky='w')
    sem = StringVar(root)
    semEntry = Entry(main_frame3, textvariable=sem, font=("arial", 13))
    semEntry.grid(row=1, column=1, pady=10)

    # for section
    secLabel = Label(main_frame3, text="Enter Section:", font=(
        "arial", 13)).grid(row=2, column=0, pady=10, sticky='w')
    sec = StringVar(root)
    secEntry = Entry(main_frame3, textvariable=sec, font=("arial", 13))
    secEntry.grid(row=2, column=1)

    # for branch duration
    course_durLabel = Label(main_frame3, text="Enter Course Duration:", font=(
        "arial", 13)).grid(row=9, column=0, pady=10, sticky='w')
    course_dur = StringVar(root)
    course_durEntry = Entry(
        main_frame3, textvariable=course_dur, font=("arial", 13))
    course_durEntry.grid(row=9, column=1)

    # for graduation year
    grad_yrLabel = Label(main_frame3, text="Enter Graduation Year:", font=(
        "arial", 13)).grid(row=10, column=0, pady=10, sticky='w')
    grad_yr = StringVar(root)
    grad_yrEntry = Entry(main_frame3, textvariable=grad_yr, font=("arial", 13))
    grad_yrEntry.grid(row=10, column=1)

    # for status
    statusLabel = Label(main_frame3, text="Enter Status:", font=(
        "arial", 13)).grid(row=11, column=0, pady=10, sticky='w')
    status = StringVar(root)
    statusdrop = ttk.Combobox(
        main_frame3, textvariable=status, font=("arial", 11), state="readonly")
    statusdrop['values'] = ('ACTIVE', 'INACTIVE')
    statusdrop.grid(row=11, column=1)

    SubmitButton = Button(main_frame1, command=submit, text="Submit", width=10, font=(
        "arial", 14, "bold")).grid(row=17, column=0, pady=20, columnspan=2)

    root.mainloop()


def stulist():
    con = sqlite3.connect('database_name.db')
    c = con.cursor()

    root = Tk()
    root.title("LIST OF STUDENTS")
    root.geometry('850x650+250+10')

    title = Label(root, text='LIST OF STUDENTS',
                  font=("times new roman", 20, "bold"))
    title.pack(side=TOP)

    # SEARCH FRAME
    search_frame = Frame(root, bd=4, relief=RIDGE)
    search_frame.place(x=30, y=50, width=780, height=60)

    search = Label(search_frame, text='Search By:   ', font=(
        "arial", 14, "bold")).grid(row=0, column=0, sticky='w')

    space = Label(search_frame, text='  ', font=(
        "arial", 14, "bold")).grid(row=0, column=2, sticky='w')

    searchdropvar = StringVar()
    searchdrop = ttk.Combobox(
        search_frame, textvariable=searchdropvar, font=("arial", 13), state='readonly')
    searchdrop['values'] = ('stud_id', 'name', 'sec', 'sem', 'branch_id')
    searchdrop.grid(row=0, column=1, pady=10)

    filtersearch = StringVar()
    searchEntry = Entry(search_frame, textvariable=filtersearch, font=(
        "arial", 13)).grid(row=0, column=3, pady=10)

    space = Label(search_frame, text='      ', font=(
        "arial", 14, "bold")).grid(row=0, column=4, sticky='w')

    def filters():
        con = sqlite3.connect('database_name.db')
        c = con.cursor()
        a = str(searchdropvar.get())
        filter_s = str(filtersearch.get())
        flag = [False]
        b = '%' + filter_s + '%'
        
        query = f"SELECT * FROM stud_info WHERE {a} LIKE ?"
        alldata = c.execute(query, (b,))
        
        for data in alldata:
            stu_table.insert('', END, values=data)
            flag[0] = [True]
        if flag[0] == False:
            myLabel = Label(table_frame, text="No record ").pack()
    con.close()


    def fetch_details():
        con = sqlite3.connect('database_name.db')
        c = con.cursor()
        all_data = c.execute("SELECT * FROM stud_info")
        i = 0
        for data in all_data:
            '''for j in range(len(data)):
                e=Entry(stu_table)
                e.pack(
                e.insert(END,data[j])
                flag[0]=[True]
            i=i+1
            '''
            stu_table.insert('', END, values=data)

    searchbuttton = Button(search_frame, text='Search', width=10, font=(
        "arial", 13), command=filters).grid(row=0, column=4, padx=10, pady=10)
    viewallbuttton = Button(search_frame, text='View All', width=10, font=(
        "arial", 13), command=fetch_details).grid(row=0, column=5, padx=10, pady=10)

    # DISPLAY FRAME
    table_frame = Frame(root, bd=4, relief=RIDGE)
    table_frame.place(x=30, y=130, width=780, height=500)

    scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
    scroll_y = Scrollbar(table_frame, orient=VERTICAL)
    stu_table = ttk.Treeview(table_frame, columns=("Student ID", "Student Name", "Date Of Birth", "Gender", "Father's Name", "Mother's Name", "Branch ID", "Semester", "Section", "Admission Date", "Graduation Year", "Course Duration",
                             "Blood Group", "Student Number", "Father's Number", "Mother's Number", "Student Email ID", "Father's Email ID", "Mother's Email ID", "Address", "Status"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM, fill=X)  # Fixed line
    scroll_y.pack(side=RIGHT, fill=Y)
    scroll_x.config(command=stu_table.xview)
    scroll_y.config(command=stu_table.yview)

    stu_table.heading("Student ID", text='Student ID')
    stu_table.heading("Student Name", text="Student Name")
    stu_table.heading("Date Of Birth", text="Date Of Birth")
    stu_table.heading("Gender", text="Gender")
    stu_table.heading("Father's Name", text="Father's Name")
    stu_table.heading("Mother's Name", text="Mother's Name")
    stu_table.heading("Branch ID", text="Branch ID")
    stu_table.heading("Semester", text="Semester")
    stu_table.heading("Section", text="Section")
    stu_table.heading("Admission Date", text="Admission Date")
    stu_table.heading("Graduation Year", text="Graduation Year")
    stu_table.heading("Course Duration", text="Course Duration")
    stu_table.heading("Blood Group", text="Blood Group")
    stu_table.heading("Student Number", text="Student Number")
    stu_table.heading("Father's Number", text="Father's Number")
    stu_table.heading("Mother's Number", text="Mother's Number")
    stu_table.heading("Student Email ID", text="Student Email ID")
    stu_table.heading("Father's Email ID", text="Father's Email ID")
    stu_table.heading("Mother's Email ID", text="Mother's Email ID")
    stu_table.heading("Address", text="Address")
    stu_table.heading("Status", text="Status")

    #stu_table.heading("View Profile",text="View Profile")
    stu_table['show'] = 'headings'

    stu_table.column("Student ID", width=80)
    stu_table.column("Date Of Birth", width=80)
    stu_table.column("Gender", width=80)
    stu_table.column("Branch ID", width=80)
    stu_table.column("Semester", width=80)
    stu_table.column("Section", width=80)
    stu_table.column("Admission Date", width=80)
    stu_table.column("Graduation Year", width=80)
    stu_table.column("Course Duration", width=80)
    stu_table.column("Blood Group", width=80)
    stu_table.column("Status", width=80)

    # stu_table.column("Course",width=80)
    #stu_table.column("View Profile",width=80)
    stu_table.pack(fill=BOTH, expand=1)


def student_main():
    root1 = Tk()
    root1.geometry('800x400+250+80')
    root1.title("ADMIN")

    def admin_action1():
        stuform()

    def admin_action2():
        stulist()

    adminLabel = Label(root1, text='STUDENTS', font=(
        "times new roman", 20, "bold")).pack(side=TOP)
    adminframe = Frame(root1, bd=4, relief=RIDGE)
    adminframe.place(x=200, y=50, width=400, height=250)

    space = Label(adminframe, text='                      ',
                  font=("arial", 14, "bold")).pack()
    space = Label(adminframe, text='                      ',
                  font=("arial", 14, "bold")).pack()
    studentsButton = Button(adminframe, text="List of Students", command=admin_action2, font=(
        "arial", 15, "bold"), width=20).pack()
    space = Label(adminframe, text='                      ',
                  font=("arial", 14, "bold")).pack()
    space = Label(adminframe, text='                      ',
                  font=("arial", 14, "bold")).pack()
    newstudentButton = Button(adminframe, text="Add Student", command=admin_action1, font=(
        "arial", 15, "bold"), width=20).pack()
    space = Label(adminframe, text='                      ',
                  font=("arial", 14, "bold")).pack()

    root1.mainloop()
