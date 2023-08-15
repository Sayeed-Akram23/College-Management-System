import sqlite3


con=sqlite3.connect('database_name.db')
c=con.cursor()


c.execute(""" CREATE TABLE stud_info
		   (stud_id TEXT PRIMARY KEY,
		    name TEXT NOT NULL,
		    dob TEXT NOT NULL,
		    gender TEXT NOT NULL,
		    name_father TEXT NOT NULL,
		    name_mother TEXT NOT NULL,
		    branch_id INT NOT NULL,
		    sem INT NOT NULL,
		    sec TEXT NOT NULL,
		    admn_date TEXT NOT NULL,
		    grad_yr INT NOT NULL,
		    course_dur INT NOT NULL,
		    blood_grp TEXT NOT NULL,
		    stud_no TEXT NOT NULL,
		    no_father TEXT NOT NULL,
		    no_mother TEXT NOT NULL,
		    stud_email TEXT NOT NULL,
		    email_father TEXT NOT NULL,
		    email_mother TEXT NOT NULL,
		    address TEXT NOT NULL,
		    status TEXT NOT NULL)
		""")
con.commit()


c.execute("""CREATE TABLE branch_info
			(branch_id INT PRIMARY KEY,
			 branch_abb TEXT NOT NULL,
			 branch_full TEXT NOT NULL)
		  """)
con.commit()


c.execute("""CREATE TABLE subject_info
			(sub_id TEXT PRIMARY KEY,
			 sub_abb TEXT NOT NULL,
			 sub_full TEXT NOT NULL,
			 sem INT NOT NULL)
		  """)
con.commit()


c.execute("""CREATE TABLE marks_entry
			(stud_id TEXT PRIMARY KEY,
			 sem INT NOT NULL,
			 sub_id TEXT NOT NULL UNIQUE,
			 marks REAL)
			""")
con.commit()


c.execute("""CREATE TABLE login_details
			(access TEXT PRIMARY KEY UNIQUE,
			 user_name TEXT NOT NULL,
			 pwd TEXT NOT NULL)
			""")
con.commit()


c.execute("""CREATE TABLE teacher_info
			(teach_id TEXT PRIMARY KEY,
		    name TEXT NOT NULL,
		    dob TEXT NOT NULL,
		    gender TEXT NOT NULL,
		    branch_id INT NOT NULL,
		    sem INT NOT NULL,
		    sec TEXT NOT NULL,
		    date_employed TEXT NOT NULL,
		    blood_grp TEXT NOT NULL,
		    teach_no TEXT NOT NULL,
		    teach_email TEXT NOT NULL,
		    salary TEXT NOT NULL,
		    address TEXT NOT NULL,
		    status TEXT NOT NULL)
		""")

con.commit()
c.execute("INSERT INTO stud_info VALUES('UGCS101','AADITYA GUPTA ','25/5/2002','M','HARIPRASAD GUPTA','SHREELAXMI',1,1,'A','2020',2024,4,'A+ve','9345672826','8926438564','6958456971','aaditya.gupta@gmail.com','hari2310@gmail.com','shreelaxmi75@gmail.com','KORMANGALA','ACTIVE')")


con.commit()

c.execute("INSERT INTO teacher_info VALUES('UGCS101','SUJATHA','12/3/1992','F',101,1,'A','12/5/2015','B+','7583292012','sujatha24@gmail.com','80000','KORMANGALA','ACTIVE')")

con.commit()


c.execute("INSERT INTO subject_info VALUES('UGMA101','EMA-I','ENGINEERING MATHEMATICS-I',1)")
c.execute("INSERT INTO subject_info VALUES('UGPH101','EPH','ENGINEERING PHYSICS',1)")
c.execute("INSERT INTO subject_info VALUES('UGME101','MES','MECHANICAL ENGINEERING SCIENCES',1)")

con.commit()



c.execute("INSERT INTO branch_info VALUES(1,'CSE','COMPUTER SCIENCE AND ENGINEERING')")
c.execute("INSERT INTO branch_info VALUES(2,'ECE','ELECTRONICS AND COMMUNICATION AND ENGINEERING')")
c.execute("INSERT INTO branch_info VALUES(3,'ME','MECHANICAL ENGINEERING')")
con.commit()



c.execute("INSERT INTO marks_entry VALUES('UGCS101',1,'CS101',85)")
c.execute("INSERT INTO marks_entry VALUES('UGME101',1,'ME101',87)")

con.commit()

c.execute("INSERT INTO login_details VALUES('1','admin','password')")
con.commit()