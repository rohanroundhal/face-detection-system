from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import time

class Student:
    def __init__(self,root):
        self.root = root
        self.root.state('zoomed')  # Maximized but keeps minimize & close buttons
        self.root.title("Face Recognition System")
        
        # Variables
        self.var_dep=StringVar() 
        self.var_course=StringVar() 
        self.var_year=StringVar() 
        self.var_semester=StringVar() 
        self.var_std_id=StringVar() 
        self.var_std_name=StringVar() 
        self.var_div=StringVar() 
        self.var_roll=StringVar() 
        self.var_gender=StringVar()  
        self.var_email=StringVar() 
        self.var_phone=StringVar() 
        self.var_address=StringVar() 
        
        # BACKGROUND IMAGE
        img = Image.open(r"Images\BG 2.jpg") #put image path in brackets
        img = img.resize((1920,1080)) 
        self.photoimg = ImageTk.PhotoImage(img) 

        bg_img=Label(self.root,image=self.photoimg) 
        bg_img.place(x=0, y=0, width=1920, height=1080)
        
        title_lbl=Label(bg_img,text="Student Management System",font=("Candara",35,"bold"),bg="white",fg="#AB274F")
        title_lbl.place(x=450,y=20,width=650,height=60)

        main_frame=Frame(bg_img, bd=2, bg="#F0F8FF")
        main_frame.place(x=16,y=100,width=1500,height=670)
        
        # Left Label Frame
        left_frame=LabelFrame(main_frame,bd=5,bg="#B9D9EB",relief=RIDGE,text="Student Details", font=("Calibri",12,"bold"))
        left_frame.place(x=20,y=10,width=700,height=640)
        
        img_left = Image.open(r"Images\Details 2.jpg") #put image path in brackets
        img_left= img_left.resize((500,200),Image.LANCZOS) 
        self.photoimg_left = ImageTk.PhotoImage(img_left) 

        bg_img=Label( left_frame,image=self.photoimg_left) 
        bg_img.place(x=95, y=10, width=500, height=150)
        
        # Current Course information
        current_course_frame=LabelFrame(left_frame,bd=3,bg="#B9D9EB",relief=RIDGE,text="Current Course information", font=("Calibri",12,"bold"))
        current_course_frame.place(x=20,y=170,width=650,height=100)
        
        # Department
        dep_label=Label(current_course_frame,bg="#B9D9EB",text="Department",font=("Calibri",12))
        dep_label.grid(row=0,column=0,padx=30)
        
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("Calibri",12),width=17,state="readonly")
        dep_combo["values"]=("Select Department","ECS","CSE","IT","EXTC","CS","AIDS")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=5,sticky=W)
        
        # Course
        course_label=Label(current_course_frame,bg="#B9D9EB",text="Course",font=("Calibri",12))
        course_label.grid(row=0,column=2,padx=30)
        
        Course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("Calibri",12),width=17,state="readonly")
        Course_combo["values"]=("Select Course","FE","SE","TE","BE")
        Course_combo.current(0)
        Course_combo.grid(row=0,column=3,padx=5,pady=5)
        
        # Year
        Year_label=Label(current_course_frame,bg="#B9D9EB",text="Year",font=("Calibri",12))
        Year_label.grid(row=1,column=0)
        
        Year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("Calibri",12),width=17,state="readonly")
        Year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2024-25")
        Year_combo.current(0)
        Year_combo.grid(row=1,column=1,padx=2,pady=5)
        
        # Semester
        Semester_label=Label(current_course_frame,bg="#B9D9EB",text="Semester",font=("Calibri",12))
        Semester_label.grid(row=1,column=2)
        
        Semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("Calibri",12),width=17,state="readonly")
        Semester_combo["values"]=("Select Semester","I","II","III","IV","V","VI","VII","VIII")
        Semester_combo.current(0)
        Semester_combo.grid(row=1,column=3,padx=2,pady=5)
        
        # Student Information
        Student_info_frame=LabelFrame(left_frame,bd=3,bg="#B9D9EB",relief=RIDGE,text="Student Information", font=("Calibri",12,"bold"))
        Student_info_frame.place(x=20,y=280,width=650,height=320)
        
        # Student ID
        StudentID_label=Label(Student_info_frame,bg="#B9D9EB",text="Student ID",font=("Calibri",12))
        StudentID_label.grid(row=0,column=0,padx=10,pady=10)
        
        StudentID_entry=ttk.Entry(Student_info_frame,textvariable=self.var_std_id,width=20,font=("Calibri",12))
        StudentID_entry.grid(row=0,column=1,padx=10,pady=10)
        
        # Student Name
        StudentName_label=Label(Student_info_frame,bg="#B9D9EB",text="Student Name",font=("Calibri",12))
        StudentName_label.grid(row=0,column=2,padx=10)
        
        StudentName_entry=ttk.Entry(Student_info_frame,textvariable=self.var_std_name,width=20,font=("Calibri",12))
        StudentName_entry.grid(row=0,column=3,padx=10)
        
        # Class Division
        Classdiv_label=Label(Student_info_frame,bg="#B9D9EB",text="Class Division",font=("Calibri",12))
        Classdiv_label.grid(row=1,column=0,padx=10,pady=10)
        
        Division_combo=ttk.Combobox(Student_info_frame,textvariable=self.var_div,font=("Calibri",12),width=17,state="readonly")
        Division_combo["values"]=("Select Division","BE-1","BE-2","BE-3","BE-4","BE-5","BE-6","BE-7")
        Division_combo.current(0)
        Division_combo.grid(row=1,column=1,padx=10)
        
        # Roll No
        RollNo_label=Label(Student_info_frame,bg="#B9D9EB",text="Roll No",font=("Calibri",12))
        RollNo_label.grid(row=1,column=2,padx=10,pady=10)
        
        RollNo_entry=ttk.Entry(Student_info_frame,textvariable=self.var_roll,width=20,font=("Calibri",12))
        RollNo_entry.grid(row=1,column=3,padx=10,pady=10)
        
        # Gender
        Gender_label=Label(Student_info_frame,bg="#B9D9EB",text="Gender",font=("Calibri",12))
        Gender_label.grid(row=2,column=0,padx=10,pady=10)
        
        Gender_combo=ttk.Combobox(Student_info_frame,textvariable=self.var_gender,font=("Calibri",12),width=17,state="readonly")
        Gender_combo["values"]=("Select Gender","Male","Female")
        Gender_combo.current(0)
        Gender_combo.grid(row=2,column=1,padx=10)
        
        # Address
        Address_label=Label(Student_info_frame,bg="#B9D9EB",text="Address",font=("Calibri",12))
        Address_label.grid(row=2,column=2,padx=10,pady=10)
        
        Address_entry=ttk.Entry(Student_info_frame,textvariable=self.var_address,width=20,font=("Calibri",12))
        Address_entry.grid(row=2,column=3,padx=10,pady=10)
        
        # Email
        Email_label=Label(Student_info_frame,bg="#B9D9EB",text="Email",font=("Calibri",12))
        Email_label.grid(row=3,column=0,padx=10,pady=10)
        
        Email_entry=ttk.Entry(Student_info_frame,textvariable=self.var_email,width=20,font=("Calibri",12))
        Email_entry.grid(row=3,column=1,padx=10)
        
        # Phone No
        Phone_label=Label(Student_info_frame,bg="#B9D9EB",text="Phone No",font=("Calibri",12))
        Phone_label.grid(row=3,column=2,padx=10)
        
        Phone_entry=ttk.Entry(Student_info_frame,textvariable=self.var_phone,width=20,font=("Calibri",12))
        Phone_entry.grid(row=3,column=3,padx=10)
          
        # radio Buttons
        self.var_radio1=StringVar()
        radionbtn1=ttk.Radiobutton(Student_info_frame,variable=self.var_radio1,text="Take Photo Sample", value="Yes") 
        radionbtn1.grid(row=6,column=0,padx=17) 
        
        radionbtn2=ttk.Radiobutton(Student_info_frame,variable=self.var_radio1,text="No Photo Sample", value="No") 
        radionbtn2.grid(row=6,column=1) 
        
        #bbuttons frame 
        btn_frame=Frame (Student_info_frame, bd=2, relief=RIDGE, bg="white") 
        btn_frame.place (x=16,y=210, width=610,height=35) 
        
        save_btn=Button(btn_frame, text="Save",command=self.add_data,width=18, font=("Calibri",12), bg="#1034A6", fg="white") 
        save_btn.grid(row=0,column=0)
        
        Update_btn=Button(btn_frame, text="Update",command=self.update_data,width=18, font=("Calibri",12), bg="#1034A6", fg="white") 
        Update_btn.grid(row=0,column=1)
        
        Delete_btn=Button(btn_frame, text="Delete",command=self.delete_data,width=18, font=("Calibri",12), bg="#1034A6", fg="white") 
        Delete_btn.grid(row=0,column=2)
        
        Reset_btn=Button(btn_frame, text="Reset",command=self.reset_data,width=17, font=("Calibri",12), bg="#1034A6", fg="white") 
        Reset_btn.grid(row=0,column=3)
        
        btn_frame1=Frame (Student_info_frame, bd=2, relief=RIDGE, bg="white") 
        btn_frame1.place (x=16,y=245, width=610,height=35) 
        
        take_photo_btn=Button(btn_frame1, text="Take Photo Sample",command=self.generate_dataset,width=37, font=("Calibri",12), bg="#1034A6", fg="white") 
        take_photo_btn.grid(row=0,column=0)
        
        Update_photo_btn=Button(btn_frame1, text="Update Photo Sample",width=37, font=("Calibri",12), bg="#1034A6", fg="white") 
        Update_photo_btn.grid(row=0,column=1)
        
        #Right Label Frame
        Right_frame=LabelFrame(main_frame,bd=5,bg="#B9D9EB",relief=RIDGE,text="Student Details", font=("Calibri",12,"bold"))
        Right_frame.place(x=772,y=10,width=700,height=640)
        
        img_right= Image.open(r"Images\Details 3.jpg") #put image path in brackets
        img_right= img_right.resize((600,150),Image.LANCZOS) 
        self.photoimg_right = ImageTk.PhotoImage(img_right) 

        bg_img=Label( Right_frame,image=self.photoimg_right) 
        bg_img.place(x=45, y=10, width=600, height=150)
        
        # Search System
        Search_frame=LabelFrame(Right_frame,bd=3,bg="#B9D9EB",relief=RIDGE,text="Search System", font=("Calibri",12,"bold"))
        Search_frame.place(x=20,y=170,width=650,height=100)
        
        Search_label=Label(Search_frame,bg="#B9D9EB",text="Search By",font=("Calibri",12))
        Search_label.grid(row=0,column=0,padx=10,pady=20)
        
        self.var_com_search=StringVar()
        Search_combo=ttk.Combobox(Search_frame,textvariable=self.var_com_search,font=("Calibri",12),width=17,state="readonly")
        Search_combo["values"]=("Select","Roll","Phone","Student_Id")
        Search_combo.current(0)
        Search_combo.grid(row=0,column=1,padx=2,pady=5)
        
        self.var_search=StringVar()
        Search_entry=ttk.Entry(Search_frame,textvariable=self.var_search,width=20,font=("Calibri",12))
        Search_entry.grid(row=0,column=2,padx=10,pady=10)
        
        Search_btn=Button(Search_frame,command=self.search_data, text="Search",width=10, font=("Calibri",12), bg="#1034A6", fg="white") 
        Search_btn.grid(row=0,column=3,padx=5)
        
        ShowAll_btn=Button(Search_frame,command=self.fetch_data,text="Show All",width=10, font=("Calibri",12), bg="#1034A6", fg="white") 
        ShowAll_btn.grid(row=0,column=4,padx=5)
        
        #Table Frame
        Table_frame=Frame(Right_frame,bd=3,bg="#B9D9EB",relief=RIDGE)
        Table_frame.place(x=20,y=290,width=650,height=310)
        
        scroll_x=ttk.Scrollbar (Table_frame, orient=HORIZONTAL) 
        scroll_y=ttk.Scrollbar (Table_frame, orient=VERTICAL)
        
        self.student_table=ttk.Treeview(Table_frame,column=("Dep","Course", "Year", "Sem", "Id", "Name","Div", "Roll", "Gender","Email","Phone","Address","Photo" ),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("Dep",text="Department")
        self.student_table.heading("Course", text="Course") 
        self.student_table.heading("Year", text="Year") 
        self.student_table.heading("Sem", text="Semester") 
        self.student_table.heading("Id", text="Student Id") 
        self.student_table.heading("Name", text="Name") 
        self.student_table.heading("Div", text="Division") 
        self.student_table.heading("Roll", text="Roll No") 
        self.student_table.heading("Gender", text="Gender") 
        self.student_table.heading("Email", text="Email") 
        self.student_table.heading("Phone", text="Phone") 
        self.student_table.heading("Address", text="Address") 
        self.student_table.heading("Photo", text="PhotoSampleStatus") 
        self.student_table["show"]="headings"
        
        self.student_table.column("Dep",width=100)
        self.student_table.column("Course",width=100) 
        self.student_table.column("Year",width=100) 
        self.student_table.column("Sem",width=100) 
        self.student_table.column("Id",width=100) 
        self.student_table.column("Name",width=100) 
        self.student_table.column("Div",width=100) 
        self.student_table.column("Roll",width=100) 
        self.student_table.column("Gender",width=100) 
        self.student_table.column("Email",width=100) 
        self.student_table.column("Phone",width=100) 
        self.student_table.column("Address",width=100) 
        self.student_table.column("Photo",width=140)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
    # Function Decleration
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Sujal@2002",database="face_recognition")
                    my_cursor=conn.cursor()
                    my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_id.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_radio1.get()    
                    ))

                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success","Student details has been added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
                
    # Fetch Data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Sujal@2002",database="face_recognition")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
    # Get Cursor
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        
        self.var_dep.set(data[0]), 
        self.var_course.set(data[1]), 
        self.var_year.set(data[2]), 
        self.var_semester.set(data[3]), 
        self.var_std_id.set(data[4]), 
        self.var_std_name.set(data[5]), 
        self.var_div.set(data[6]), 
        self.var_roll.set(data[7]), 
        self.var_gender.set(data[8]), 
        self.var_email.set(data[9]), 
        self.var_phone.set(data[10]), 
        self.var_address.set(data[11]), 
        self.var_radio1.set(data[12])
        
    # Update Function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root) 
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want update student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Sujal@2002",database="face_recognition")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Email=%s,Phone=%s,Address=%s,PhotoSample=%s where Student_Id=%s",( 
                                                                                                                                                                                                       
                                                        self.var_dep.get(),
                                                        self.var_course.get(),
                                                        self.var_year.get(),
                                                        self.var_semester.get(),
                                                        self.var_std_name.get(),
                                                        self.var_div.get(),
                                                        self.var_roll.get(),
                                                        self.var_gender.get(),
                                                        self.var_email.get(),
                                                        self.var_phone.get(),
                                                        self.var_address.get(),
                                                        self.var_radio1.get(),
                                                        self.var_std_id.get()
                                                        ))
                else:  
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details updated successfully",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()    
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                
    # Delete Function
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student Id Required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Sujal@2002",database="face_recognition")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_Id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
    
    # Reset Data
    def reset_data(self):
        self.var_dep.set("Select Department")       
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_std_name.set(""),
        self.var_div.set("Select Division"),
        self.var_roll.set(""),
        self.var_gender.set("Select Gender"),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_radio1.set(""),
        self.var_std_id.set("")
        
    # Search Data
    def search_data(self):
        if self.var_com_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error","Please select an option")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Sujal@2002",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student where " +str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get()) +"%'")
                data=my_cursor.fetchall()
                
                if len(data)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("",END,values=i)
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                
    # Generate Data set
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root) 
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Sujal@2002",database="face_recognition")
                my_cursor=conn.cursor()
                
                my_cursor.execute("SELECT Student_Id FROM student WHERE Name=%s AND Roll=%s", (self.var_std_name.get(), self.var_roll.get()))
                student_data = my_cursor.fetchone()
                
                if student_data is None:
                    messagebox.showerror("Error", "Student not found in database", parent=self.root)
                    return
            
                student_id = student_data[0]
                
                my_cursor.execute(
                    "UPDATE student SET Dep=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, Email=%s, Phone=%s, Address=%s, PhotoSample=%s WHERE Student_Id=%s",
                    (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_radio1.get(),
                        student_id  # Use the fetched student ID
                    )
                )
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                
                # Opencv
                face_classifier=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
                
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=8, minSize=(100, 100))
                    
                    for (x,y,w,h) in faces:
                        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                        return img[y:y+h, x:x+w]
                    return None
                    
                cap=cv2.VideoCapture(0)
                cap.set(3, 1280)
                cap.set(4, 720)
                img_id=0
                
                while True:
                    ret,my_frame=cap.read()
                    if not ret:
                        break
                    face = face_cropped(my_frame)
                    if face is not None:
                        img_id+=1
                        file_name_path = f"Sample Images/{student_id}_{img_id}.jpg"
                        cv2.imwrite(file_name_path, face, [cv2.IMWRITE_JPEG_QUALITY, 100])
                        cv2.putText(face,str(img_id),(40,40),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,255),2)
                    small_frame = cv2.resize(my_frame, (640, 360))
                    cv2.imshow("Capture Window",small_frame)
                    
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                
                messagebox.showinfo("Result","Data Sets Generated Sucessfully!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                                                    
if __name__ =="__main__": 
    root=Tk()
    obj=Student(root)
    root.mainloop()