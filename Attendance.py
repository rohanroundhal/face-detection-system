from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import time
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root = root
        self.root.state('zoomed')  # Maximized but keeps minimize & close buttons
        self.root.title("Attendance")
        
        # Variables
        self.var_atten_id=StringVar() 
        self.var_atten_roll=StringVar() 
        self.var_atten_name=StringVar() 
        self.var_atten_dep=StringVar() 
        self.var_atten_time=StringVar() 
        self.var_atten_date=StringVar() 
        self.var_atten_attendance=StringVar()
        
        # BACKGROUND IMAGE
        img = Image.open(r"Images\BG 2.jpg") #put image path in brackets
        img = img.resize((1920,1080)) 
        self.photoimg = ImageTk.PhotoImage(img) 

        bg_img=Label(self.root,image=self.photoimg) 
        bg_img.place(x=0, y=0, width=1920, height=1080)
        
        title_lbl=Label(bg_img,text="Attendance Management System",font=("Candara",35,"bold"),bg="white",fg="#AB274F")
        title_lbl.place(x=450,y=20,width=700,height=60)

        main_frame=Frame(bg_img, bd=2, bg="#F0F8FF")
        main_frame.place(x=16,y=100,width=1500,height=670)
        
        # Left Label Frame
        left_frame=LabelFrame(main_frame,bd=5,bg="#B9D9EB",relief=RIDGE,text="Student Attendance Details", font=("Calibri",12,"bold"))
        left_frame.place(x=20,y=10,width=700,height=640)
        
        img_left = Image.open(r"Images\Details 2.jpg") #put image path in brackets
        img_left= img_left.resize((500,200),Image.LANCZOS) 
        self.photoimg_left = ImageTk.PhotoImage(img_left) 

        bg_img=Label( left_frame,image=self.photoimg_left) 
        bg_img.place(x=95, y=10, width=500, height=150)
        
        left_inside_frame=LabelFrame(left_frame,bd=5,bg="#B9D9EB",relief=RIDGE)
        left_inside_frame.place(x=20,y=170,width=650,height=400)
        
        # Labels
        
        #Department
        Dep_label=Label(left_inside_frame,bg="#B9D9EB",text="Department",font=("Calibri",12))
        Dep_label.grid(row=0,column=0,padx=10,pady=10)
        
        Dep_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_dep,width=20,font=("Calibri",12))
        Dep_entry.grid(row=0,column=1,padx=10,pady=10)
        
        #Student ID
        StudentID_label=Label(left_inside_frame,bg="#B9D9EB",text="Student ID",font=("Calibri",12))
        StudentID_label.grid(row=1,column=0)
        
        StudentID_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_id,width=20,font=("Calibri",12))
        StudentID_entry.grid(row=1,column=1,padx=2,pady=5)
        
        #Roll No
        Rollno_label=Label(left_inside_frame,bg="#B9D9EB",text="Roll No",font=("Calibri",12))
        Rollno_label.grid(row=1,column=2)
        
        Rollno_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_roll,width=20,font=("Calibri",12))
        Rollno_entry.grid(row=1,column=3,padx=2,pady=5)
        
        #Name
        Name_label=Label(left_inside_frame,bg="#B9D9EB",text="Name",font=("Calibri",12))
        Name_label.grid(row=0,column=2,padx=10,pady=30)
        
        Name_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_name,width=20,font=("Calibri",12))
        Name_entry.grid(row=0,column=3,padx=5,pady=5)
        
        #Time
        Time_label=Label(left_inside_frame,bg="#B9D9EB",text="Time",font=("Calibri",12))
        Time_label.grid(row=2,column=0)
        
        Time_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_time,width=20,font=("Calibri",12))
        Time_entry.grid(row=2,column=1,padx=10,pady=30)
        
        #Date
        Date_label=Label(left_inside_frame,bg="#B9D9EB",text="Date",font=("Calibri",12))
        Date_label.grid(row=2,column=2)
        
        Date_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_date,width=20,font=("Calibri",12))
        Date_entry.grid(row=2,column=3,padx=10,pady=30)
        
        #Attendance Status
        Attendancestat_label=Label(left_inside_frame,bg="#B9D9EB",text="Attendance Status",font=("Calibri",12))
        Attendancestat_label.grid(row=3,column=0,padx=10)
        
        Attendancestat_combo=ttk.Combobox(left_inside_frame,width=18,textvariable=self.var_atten_attendance,font=("Calibri",12),state="readonly")
        Attendancestat_combo["values"]=("Status","Present","Abscent")
        Attendancestat_combo.current(0)
        Attendancestat_combo.grid(row=3,column=1,pady=4)
        
        #bbuttons frame 
        btn_frame=Frame (left_inside_frame, bd=2, relief=RIDGE, bg="white") 
        btn_frame.place (x=16,y=330, width=610,height=35) 
        
        Import_btn=Button(btn_frame, text="Import CSV",command=self.importCsv,width=18, font=("Calibri",12), bg="#1034A6", fg="white") 
        Import_btn.grid(row=0,column=0)
        
        Export_btn=Button(btn_frame, text="Export CSV",command=self.exportCsv,width=18, font=("Calibri",12), bg="#1034A6", fg="white") 
        Export_btn.grid(row=0,column=1)
        
        Update_btn=Button(btn_frame, text="Update",command=self.updateCsv,width=18, font=("Calibri",12), bg="#1034A6", fg="white") 
        Update_btn.grid(row=0,column=2)
        
        Reset_btn=Button(btn_frame, text="Reset",command=self.reset_data,width=17, font=("Calibri",12), bg="#1034A6", fg="white") 
        Reset_btn.grid(row=0,column=3)
        
        #Right Label Frame
        Right_frame=LabelFrame(main_frame,bd=5,bg="#B9D9EB",relief=RIDGE,text="Attendance Details", font=("Calibri",12,"bold"))
        Right_frame.place(x=772,y=10,width=700,height=640)
        
        img_right= Image.open(r"Images\Details 3.jpg") #put image path in brackets
        img_right= img_right.resize((600,150),Image.LANCZOS) 
        self.photoimg_right = ImageTk.PhotoImage(img_right) 

        bg_img=Label( Right_frame,image=self.photoimg_right) 
        bg_img.place(x=45, y=10, width=600, height=150)
        
        #Table Frame
        Table_frame=Frame(Right_frame,bd=5,bg="#B9D9EB",relief=RIDGE)
        Table_frame.place(x=20,y=170,width=650,height=400)
        
        scroll_x=ttk.Scrollbar(Table_frame, orient=HORIZONTAL) 
        scroll_y=ttk.Scrollbar(Table_frame, orient=VERTICAL)
        
        self.AttendanceReport_table=ttk.Treeview(Table_frame,column=("Dep","Name","Id","Roll","Time","Date","Attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReport_table.xview)
        scroll_y.config(command=self.AttendanceReport_table.yview)
        
        self.AttendanceReport_table.heading("Dep",text="Department")
        self.AttendanceReport_table.heading("Name", text="Name")  
        self.AttendanceReport_table.heading("Id", text="Student Id") 
        self.AttendanceReport_table.heading("Roll", text="Roll No") 
        self.AttendanceReport_table.heading("Time", text="Time")
        self.AttendanceReport_table.heading("Date", text="Date")
        self.AttendanceReport_table.heading("Attendance", text="Attendance")
        self.AttendanceReport_table["show"]="headings"
        
        self.AttendanceReport_table.column("Dep",width=100)
        self.AttendanceReport_table.column("Name",width=100)  
        self.AttendanceReport_table.column("Id",width=100 ) 
        self.AttendanceReport_table.column("Roll",width=100) 
        self.AttendanceReport_table.column("Time",width=100)
        self.AttendanceReport_table.column("Date",width=100)
        self.AttendanceReport_table.column("Attendance",width=100)
        
        self.AttendanceReport_table.pack(fill=BOTH,expand=1)
        
        self.AttendanceReport_table.bind("<ButtonRelease>",self.get_cursor)
        
    # Fetch Data
    def fetchdata(self,rows):
        try:
            self.AttendanceReport_table.delete(*self.AttendanceReport_table.get_children())  # Clear table

            for row in rows:
                self.AttendanceReport_table.insert("", "end", values=row)  # Insert updated data

        except Exception as e:
            messagebox.showerror("Error", f"Failed to load data: {str(e)}", parent=self.root)
        
    # Import CSV
    def importCsv(self):
        global mydata
        mydata.clear()
        self.csv_filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV",
                                                   filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")), parent=self.root)
        if not self.csv_filename:
            return
        
        with open(self.csv_filename) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for row in csvread:
                mydata.append(row)
            self.fetchdata(mydata)
            
    # Export CSV
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Present",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title = "Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile, delimiter=",") 
                for i in mydata: 
                    exp_write.writerow(i) 
                messagebox.showinfo("Data Export", "Your data exported to "+os.path.basename(fln)+"successfully")
        except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                
    # Update CSV
    def updateCsv(self):
        selected_item = self.AttendanceReport_table.selection()
        if not selected_item:
            messagebox.showerror("Error", "No row selected", parent=self.root)
            return

        cursor_row = self.AttendanceReport_table.focus()
        content = self.AttendanceReport_table.item(cursor_row)
        row_values = content['values']
        
        if not row_values:
            messagebox.showerror("Error", "Invalid selection", parent=self.root)
            return
        
        mydata = []
        with open("Attendance.csv", "r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            mydata = list(reader)
        
        # print("Before Update:", mydata)  # Debugging: Check current data
        
        # Update `mydata`
        for i in range(len(mydata)):
            if mydata[i][2].strip() == str(row_values[2]).strip():  # Check if ID matches (index 2 is ID)
                mydata[i] = [
                    self.var_atten_dep.get(),
                    self.var_atten_name.get(),
                    self.var_atten_id.get(),
                    self.var_atten_roll.get(),
                    self.var_atten_time.get(),
                    self.var_atten_date.get(),
                    self.var_atten_attendance.get()
                ]
                break
        
        # print("After Update:", mydata)  # Debugging: Check if data changes                            
        
        # Write updated data to CSV
        with open("Attendance.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(mydata)
        
        self.fetchdata(mydata)

        messagebox.showinfo("Success", "Attendance updated successfully!", parent=self.root)
        
    # Get Cursor
    def get_cursor(self, event=""): 
        cursor_row=self.AttendanceReport_table.focus() 
        content=self.AttendanceReport_table.item(cursor_row) 
        rows = content.get('values', [])  # Ensure rows is a list
        
        if not rows:  # If empty, do nothing
            return
        self.var_atten_dep.set(rows[0]) 
        self.var_atten_name.set(rows[1]) 
        self.var_atten_id.set(rows[2]) 
        self.var_atten_roll.set(rows[3]) 
        self.var_atten_time.set(rows[4]) 
        self.var_atten_date.set(rows[5]) 
        self.var_atten_attendance.set(rows[6])
        
    # Reset Data
    def reset_data(self):
        self.var_atten_dep.set("") 
        self.var_atten_name.set("") 
        self.var_atten_id.set("") 
        self.var_atten_roll.set("") 
        self.var_atten_time.set("") 
        self.var_atten_date.set("") 
        self.var_atten_attendance.set("")            
        
if __name__ =="__main__": 
    root=Tk()
    obj=Attendance(root)
    root.mainloop()