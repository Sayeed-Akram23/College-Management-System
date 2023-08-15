
import sqlite3
from tkinter import BOTH, BOTTOM, END, HORIZONTAL, RIDGE, RIGHT, TOP, VERTICAL,X, Y, Scrollbar, StringVar, Tk, Toplevel, Label, Frame, Entry, Button, ttk


def teachform():
    root=Tk()
    root.title("ADD TEACHER")
    root.geometry('1200x500+40+20')

    title=Label(root,text='ADD TEACHER',font=("times new roman",20,"bold"))
    title.pack(side=TOP)

    main_frame1=Frame(root,bd=4,relief=RIDGE)
    main_frame1.place(x=30,y=50,width=500,height=400)

    main_frame2=Frame(root,bd=4,relief=RIDGE)
    main_frame2.place(x=650,y=50,width=500,height=400)

    def submit():
        con=sqlite3.connect('database_name.db')
        c=con.cursor()
        #insert_val=[teach_id.get(), teach_name.get(), dob.get(), gender.get(), teach_no.get(), teach_email.get(), courses.get(), sems.get(), sections.get(), emp_yr.get(), salary.get(), blood_grp.get(), address.get()]
        c.execute("INSERT INTO teacher_info VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(teach_id.get(), teach_name.get(), dob.get(), gender.get(),courses.get(),sems.get(),sections.get(),emp_year.get(), blood_group.get(),teach_no.get(),teach_email.get(),salary.get(),address.get(),status.get()))		
        con.commit()
        clearform2()
        return

    def clearform2():
        teach_id.set('')
        teach_name.set('')
        dob.set('')
        gender.set("")
        courses.set('')
        sems.set('')
        sections.set('')
        emp_year.set('')
        blood_group.set('')
        teach_no.set('')
        teach_email.set('')    
        salary.set('')
        address.set('')
        status.set("")
        return
    
    #for Teacher id   
    teach_idLabel=Label(main_frame1,text="Enter Teacher ID:",font=("arial",14)).grid(row=1,column=0,pady=10,sticky='w')
    teach_id=StringVar(root)
    teach_idEntry=Entry(main_frame1,textvariable=teach_id,font=(14)).grid(row=1,column=1,pady=10)
    
    #for Teacher name  
    teach_nameLabel=Label(main_frame1,text="Enter Teacher Name:",font=("arial",14)).grid(row=3,column=0,pady=10,sticky='w')
    teach_name=StringVar(root)
    teach_nameEntry=Entry(main_frame1,textvariable=teach_name,font=("arial",14)).grid(row=3,column=1,pady=10)

    #for date of birth   
    dobLabel=Label(main_frame1,text="Enter Date Of Birth:",font=("arial",14)).grid(row=5,column=0,pady=10,sticky='w')
    dob=StringVar(root)
    dobEntry=Entry(main_frame1,textvariable=dob,font=("arial",14)).grid(row=5,column=1,pady=10)
    
    #for gender 
    genderLabel=Label(main_frame1,text="Enter Gender:",font=("arial",14)).grid(row=7,column=0,pady=10,sticky='w')
    gender=StringVar(root)
    genderdrop=ttk.Combobox(main_frame1,font=("arial",13),state='readonly')
    genderdrop['values']=("Female","Male","Other")
    genderdrop.grid(row=7,column=1)
    
    #for Teacher's number   
    teach_noLabel=Label(main_frame1,text="Enter Teacher's Number:",font=("arial",14)).grid(row=9,column=0,pady=10,sticky='w')
    teach_no=StringVar(root)
    teach_noEntry=Entry(main_frame1,textvariable=teach_no,font=("arial",14)).grid(row=9,column=1,pady=10)

    #for Teacher's email id   
    teach_emailLabel=Label(main_frame1,text="Enter Teacher's Email ID:",font=("arial",14)).grid(row=11,column=0,pady=10,sticky='w')
    teach_email=StringVar(root)
    teach_emailEntry=Entry(main_frame1,textvariable=teach_email,font=("arial",14)).grid(row=11,column=1,pady=10)

    #for courses taught 
    coursesLabel=Label(main_frame2,text="Enter Course ID:",font=("arial",14)).grid(row=0,column=0,pady=10,sticky='w')
    courses=StringVar(root)
    coursesEntry=Entry(main_frame2,textvariable=courses,font=("arial",14)).grid(row=0,column=1,pady=10)

    #for semsester   
    semsLabel=Label(main_frame2,text="Enter Semester:",font=("arial",14)).grid(row=1,column=0,pady=10,sticky='w')
    sems=StringVar(root)
    semsEntry=Entry(main_frame2,textvariable=sems,font=("arial",14)).grid(row=1,column=1,pady=10)
    
    #for sections   
    sectionsLabel=Label(main_frame2,text="Enter Sections:",font=("arial",14)).grid(row=2,column=0,pady=10,sticky='w')
    sections=StringVar(root)
    sectionsEntry=Entry(main_frame2,textvariable=sections,font=("arial",14)).grid(row=2,column=1)
    
    #for Employment year   
    emp_yearLabel=Label(main_frame2,text="Enter Employment Year:",font=("arial",14)).grid(row=3,column=0,pady=10,sticky='w')
    emp_year=StringVar(root)
    emp_yearEntry=Entry(main_frame2,textvariable=emp_year,font=("arial",14)).grid(row=3,column=1)

    #for Salary  
    salaryLabel=Label(main_frame2,text="Enter Salary:",font=("arial",14)).grid(row=4,column=0,pady=10,sticky='w')
    salary=StringVar(root)
    salaryEntry=Entry(main_frame2,textvariable=salary,font=("arial",14)).grid(row=4,column=1)

    #for blood group  
    blood_groupLabel=Label(main_frame2,text="Enter Blood Group:",font=("arial",14)).grid(row=5,column=0,pady=10,sticky='w')
    blood_group=StringVar(root)
    blood_groupdrop=ttk.Combobox(main_frame2,font=("arial",13),state="readonly")
    blood_groupdrop['values']=('A+', 'A-', 'B+', 'B-', 'O+',' O-', 'AB+', 'AB-')
    blood_groupdrop.grid(row=5,column=1)

    #for address
    addressLabel=Label(main_frame1,text="Enter Address:",font=("arial",14)).grid(row=12,column=0,pady=10,sticky='w')
    address=StringVar(root)
    addressText=Entry(main_frame1,textvariable=address,font=("arial",14)).grid(row=12,column=1)

    SubmitButton=Button(root,command=submit,text="Submit",width=10,font=("arial",14,"bold")).pack(side=BOTTOM)

    #for status
    statusLabel=Label(main_frame1,text="Enter Status:",font=("arial",14)).grid(row=13,column=0,pady=10,sticky='w')
    status=StringVar(root)
    statusdrop=ttk.Combobox(main_frame1,textvariable=status,font=("arial",13),state="readonly")
    statusdrop['values']=('ACTIVE','INACTIVE')
    statusdrop.grid(row=13,column=1)

    root.mainloop()

def teachlist():
    root=Tk()
    root.title("LIST OF TEACHERS")
    root.geometry('850x750+250+10')

    title=Label(root,text='LIST OF TEACHERS',font=("times new roman",20,"bold"))
    title.pack(side=TOP)

    #SEARCH FRAME        
    search_frame=Frame(root,bd=4,relief=RIDGE)
    search_frame.place(x=30,y=50,width=800,height=60)

    search=Label(search_frame,text='Search By:   ',font=("arial",14,"bold")).grid(row=0,column=0,sticky='w')
    filtersearch=StringVar(root)
    searchEntry=Entry(search_frame,textvariable=filtersearch,font=("arial",13)).grid(row=0,column=3,pady=10)


    space=Label(search_frame,text='    ',font=("arial",14,"bold")).grid(row=0,column=2,sticky='w')

    searchdropvar=StringVar(root)
    searchdrop=ttk.Combobox(search_frame,textvariable=searchdropvar,font=("arial",13),state='readonly')
    #searchdrop['values']=("Date Of Birth","Gender","Branch ID","Teacher ID","Teacher Name")
    searchdrop['values']=("dob","gender","branch_id","teach_id","teach_name")
    searchdrop.grid(row=0,column=1,pady=10)


    def filters():
        con=sqlite3.connect('database_name.db')
        c=con.cursor()
        #d={"Teacher ID":'teach_id',"Teacher Name":'name',"Date Of Birth":'dob',"Gender":'gender',"Branch ID":'branch_id'}
        a=searchdropvar.get()
        #a=d[searchdropvar.get()]
        #print(a)
        filter_s=filtersearch.get()
        #print(search_drop,filter_s)

        flag= [False]
        b='%'+filter_s+'%'
        alldata=c.execute("SELECT * FROM teacher_info WHERE ? like ?",(a,b,))
        i=0
        for data in alldata:
            teach_table.insert('',END,values=data)
            flag[0]=[True]
            '''
            for j in range(len(data)):
                e=Entry(teach_table)
                e.pack()
                e.insert(END,data[j])
                
            i=i+1
            '''
        if flag[0]==False:
            myLabel=Label(table_frame, text="No record ").pack()
        con.close()

    def fetch_details():
        con=sqlite3.connect('database_name.db')
        c=con.cursor()
        all_data=c.execute("SELECT * FROM teacher_info")
        i=0
        for data in all_data:
            '''for j in range(len(data)):
                e=Entry(teach_table)
                e.pack(
                e.insert(END,data[j])
                flag[0]=[True]
            i=i+1
            '''
            teach_table.insert('',END,values=data)

    #DISPLAY FRAME
    table_frame=Frame(root,bd=4,relief=RIDGE)
    table_frame.place(x=30,y=130,width=800,height=500)




    scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
    scroll_y=Scrollbar(table_frame,orient=VERTICAL)
    teach_table=ttk.Treeview(table_frame,columns=("Teacher ID","Teacher Name","Date Of Birth","Gender","Branch ID"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)

    scroll_x.config(command=teach_table.xview)
    scroll_y.config(command=teach_table.yview)

    teach_table.heading("Teacher ID",text='Teacher ID')
    teach_table.heading("Teacher Name",text="Teacher Name")
    teach_table.heading("Date Of Birth",text="Date Of Birth")
    teach_table.heading("Gender",text="Gender")
    teach_table.heading("Branch ID",text="Branch ID")
    #teach_table.heading("View Profile",text="View Profile")
    teach_table['show']='headings'
    teach_table.pack(fill=BOTH,expand=1)

    searchbuttton=Button(search_frame,text='Search',width=10,font=("arial",13),command=filters).grid(row=0,column=4,padx=10,pady=10)
    viewallbuttton=Button(search_frame,text='View All',width=10,font=("arial",13),command=fetch_details).grid(row=0,column=5,padx=10,pady=10)

    root.mainloop()

def teacher_main():
    root1=Tk()
    root1.geometry('800x400+250+80')
    root1.title("ADMIN")

    def admin_action1():
        teachform()
    def admin_action2():
        teachlist()

    adminLabel=Label(root1,text='TEACHERS',font=("times new roman",20,"bold")).pack(side=TOP)
    adminframe=Frame(root1,bd=4,relief=RIDGE)
    adminframe.place(x=200,y=50,width=400,height=250)

    space=Label(adminframe,text='                      ',font=("arial",14,"bold")).pack()
    space=Label(adminframe,text='                      ',font=("arial",14,"bold")).pack()
    teachersButton=Button(adminframe,text="List of teachers",command=admin_action2,font=("arial",15,"bold"),width=20).pack()
    space=Label(adminframe,text='                      ',font=("arial",14,"bold")).pack()
    space=Label(adminframe,text='                      ',font=("arial",14,"bold")).pack()
    newteacherButton=Button(adminframe,text="Add Teacher",command=admin_action1,font=("arial",15,"bold"),width=20).pack()
    space=Label(adminframe,text='                      ',font=("arial",14,"bold")).pack()

    root1.mainloop()