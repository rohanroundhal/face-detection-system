from tkinter import*
from tkinter import ttk
import tkinter
import tkinter.messagebox
from PIL import Image,ImageTk
from Student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from Attendance import Attendance

class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.state('zoomed')  # Maximized but keeps minimize & close buttons
        self.root.title("Face Recognition System")
        
        # BACKGROUND IMAGE
        
        img3 = Image.open(r"Images\BG 2.jpg") #put image path in brackets
        img3 = img3.resize((1920,1080)) 
        self.photoimg3 = ImageTk.PhotoImage(img3) 

        bg_img=Label(self.root,image=self.photoimg3) 
        bg_img.place(x=0, y=0, width=1920, height=1080)
        
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("Candara",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=50,width=1533,height=45)
        
        # Student Button
        
        img4 = Image.open(r"Images\Student.png") #put image path in brackets
        img4 = img4.resize((150,150)) 
        self.photoimg4 = ImageTk.PhotoImage(img4)
        
        b1=Button(bg_img,image=self.photoimg4,command=self.Student_details,cursor="hand2")
        b1.place(x=200,y=180,width=180,height=180)
        
        b1_1=Button(bg_img,text="Student Details",command=self.Student_details,font=("Calibri",12,"bold"),bg="#1F305E",fg="White",cursor="hand2")
        b1_1.place(x=200,y=348,width=180,height=40)
        
        # Detect Face Button
        
        img5 = Image.open(r"Images\Detect.png") #put image path in brackets
        img5 = img5.resize((150,150)) 
        self.photoimg5 = ImageTk.PhotoImage(img5)
        
        b2=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b2.place(x=670,y=180,width=180,height=180)
        
        b2_2=Button(bg_img,text="Detect face",font=("Calibri",12,"bold"),bg="#1F305E",fg="White",cursor="hand2",command=self.face_data)
        b2_2.place(x=670,y=348,width=180,height=40)
        
        # Attendance Button
        
        img6 = Image.open(r"Images\Attendance.png") #put image path in brackets
        img6 = img6.resize((150,150)) 
        self.photoimg6 = ImageTk.PhotoImage(img6)
        
        b3=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b3.place(x=1150,y=180,width=180,height=180)
        
        b3_3=Button(bg_img,text="Attendance",font=("Calibri",12,"bold"),bg="#1F305E",fg="White",cursor="hand2",command=self.attendance_data)
        b3_3.place(x=1150,y=348,width=180,height=40)
        
        # # Help Button
        
        # img7 = Image.open(r"Images\Help.png") #put image path in brackets
        # img7 = img7.resize((150,150)) 
        # self.photoimg7 = ImageTk.PhotoImage(img7)
        
        # b4=Button(bg_img,image=self.photoimg7,cursor="hand2")
        # b4.place(x=1152,y=180,width=180,height=180)
        
        # b4_4=Button(bg_img,text="Help Desk",font=("Calibri",12,"bold"),bg="#1F305E",fg="White",cursor="hand2")
        # b4_4.place(x=1152,y=348,width=180,height=40)
        
        # Train Data Button
        
        img8 = Image.open(r"Images\Data.png") #put image path in brackets
        img8 = img8.resize((150,150)) 
        self.photoimg8 = ImageTk.PhotoImage(img8)
        
        b5=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b5.place(x=200,y=480,width=180,height=180)
        
        b5_5=Button(bg_img,text="Train Data",command=self.train_data,font=("Calibri",12,"bold"),bg="#1F305E",fg="White",cursor="hand2")
        b5_5.place(x=200,y=648,width=180,height=40)
        
        # Photos Button
        
        img9 = Image.open(r"Images\Photos.png") #put image path in brackets
        img9 = img9.resize((150,150)) 
        self.photoimg9 = ImageTk.PhotoImage(img9)
        
        b6=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_image)
        b6.place(x=670,y=480,width=180,height=180)
        
        b6_6=Button(bg_img,text="Photos",command=self.open_image,font=("Calibri",12,"bold"),bg="#1F305E",fg="White",cursor="hand2")
        b6_6.place(x=670,y=648,width=180,height=40)
        
        # # Developer Button
        
        # img10 = Image.open(r"Images\Developer.png") #put image path in brackets
        # img10 = img10.resize((150,150)) 
        # self.photoimg10 = ImageTk.PhotoImage(img10)
        
        # b7=Button(bg_img,image=self.photoimg10,cursor="hand2")
        # b7.place(x=840,y=480,width=180,height=180)
        
        # b7_7=Button(bg_img,text="Developer",font=("Calibri",12,"bold"),bg="#1F305E",fg="White",cursor="hand2")
        # b7_7.place(x=840,y=648,width=180,height=40)
        
        # Exit Button
        
        img11 = Image.open(r"Images\Exit.png") #put image path in brackets
        img11 = img11.resize((130,130)) 
        self.photoimg11 = ImageTk.PhotoImage(img11)
        
        b8=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.exit)
        b8.place(x=1152,y=480,width=180,height=180)
        
        b8_8=Button(bg_img,text="Exit",font=("Calibri",12,"bold"),bg="#1F305E",fg="White",cursor="hand2",command=self.exit)
        b8_8.place(x=1152,y=648,width=180,height=40)
    
    def open_image(self):
        os.startfile("Sample Images")    
        
    # Funtion Buttons
    
    def Student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
        
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
        
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
            
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
        
    def exit(self):
        self.exit=tkinter.messagebox.askyesno("Face Recognition","Are you sure you want to exit ?",parent=self.root)
        if self.exit >0:
            self.root.destroy()
        else:
            return
        
if __name__ =="__main__":
    root=Tk()
    obj=Face_Recognition_System(root) 
    root.mainloop()