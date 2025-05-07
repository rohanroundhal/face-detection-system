from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import csv
from time import strftime
from datetime import datetime
import cv2
import time
import os
import numpy as np


class Face_Recognition:
    def __init__(self,root):
        self.marked_students = set()
        self.root = root
        self.root.state('zoomed')  # Maximized but keeps minimize & close buttons
        self.root.title("Face Recognition System")
        
        img = Image.open(r"Images\Face.jpg") #put image path in brackets
        img = img.resize((1920,1080)) 
        self.photoimg = ImageTk.PhotoImage(img) 

        bg_img=Label(self.root,image=self.photoimg) 
        bg_img.place(x=0, y=0, width=1920, height=1080)
        
        # img_2 = Image.open(r"Images\Face 2.jpg") #put image path in brackets
        # img_2 = img_2.resize((358,695)) 
        # self.photoimg_2 = ImageTk.PhotoImage(img_2)
        
        # bg_img=Label(self.root,image=self.photoimg_2) 
        # bg_img.place(x=0, y=0, width=358, height=695) 
        
        title_lbl=Label(bg_img,text="FACE DETECTION",font=("Candara",35,"bold"),bg="white",fg="#AB274F")
        title_lbl.place(x=450,y=20,width=650,height=60)
        
        b1_1=Button(bg_img,text="DETECT FACE",font=("Calibri",12,"bold"),bg="#1F305E",fg="White",cursor="hand2",command=self.face_recog)
        b1_1.place(x=650,y=348,width=180,height=40)
    
    # Attendance
    marked_students = set()
    
    def mark_attendance(self, d, n, i, r):  
        global marked_students  
        filename = "Attendance.csv"  

    # Check if already marked in the current session  
        if (d, n, i, r) in self.marked_students:  
            return  # Skip if already marked in this session  

    # Read existing records to check duplicates  
        if os.path.isfile(filename) and os.stat(filename).st_size > 0:  
            with open(filename, "r", newline="\n") as f:  
                reader = csv.reader(f)  
                name_list = [row[:4] for row in reader]  

    # Check if already marked in file  
            if [d, n, i, r] in name_list:  
                return  # Skip if already marked in the file  

    # Append new attendance entry  
        now = datetime.now()  
        d1 = now.strftime(" %d/%m/%Y")  
        dtString = now.strftime(" %I:%M:%S %p")  

        with open(filename, "a", newline="\n") as f:  
            writer = csv.writer(f)  
            writer.writerow([d, n, i, r, dtString, d1, "Present"])  

        self.marked_students.add((d, n, i, r))
                 
    # Face Recognition
    def face_recog(self):
            def draw_boundry(img, classifier, scaleFactor, minNeighbors, color, text, clf): 
                gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
                features=classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors,minSize=(120, 120))
                
                coord = []

                for (x,y,w,h) in features: 
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2) 
                    id, predict=clf.predict(gray_image[y:y+h,x:x+w])
                    id = int(id)  # Ensure ID is an integer before querying 
                    confidence=int((100*(1-predict/300)))

                    conn=mysql.connector.connect(host="localhost",username="root",password="Sujal@2002",database="face_recognition")
                    my_cursor=conn.cursor()
                    
                    my_cursor.execute("SELECT Name, Roll, Dep, Student_Id FROM student WHERE Student_Id = %s", (id,)) 
                    result = my_cursor.fetchone()
                    conn.close()
                    
                    if result:
                        n, r, d,i = result
                    else:
                        n, r, d,i = "Unknown", "Unknown", "Unknown", "Unknown"
                    
                    if confidence > 77:                        
                        cv2.putText(img, f"Dep: {d}", (x, y - 75), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
                        cv2.putText(img, f"Name: {n}", (x, y - 58), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
                        cv2.putText(img, f"ID: {i}", (x, y - 40), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
                        cv2.putText(img, f"Roll No: {r}", (x, y - 22), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
                        self.mark_attendance(d,n,i,r)
                    else:
                        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
                        cv2.putText(img, "Unknown", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 255, 255), 1)
                
                    coord = [x,y,w,h]
                    
                return coord
            
            def recognize(img,clf,faceCascade):
                coord = draw_boundry(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
                return img
            
            faceCascade=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
            clf=cv2.face.LBPHFaceRecognizer_create()
            clf.read("classifier.xml")
            
            video_cap=cv2.VideoCapture(0)
            video_cap.set(cv2.CAP_PROP_FPS, 120)  # Improve FPS
            video_cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  
            video_cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
                    
            while True: 
                    ret, img = video_cap.read()
                    img = recognize(img, clf, faceCascade)
                    cv2.imshow("Welcome To Face Recognition", img) 
                
                    if cv2.waitKey(1)==13: 
                        break
                 
            video_cap.release() 
            cv2.destroyAllWindows() 
                
if __name__ =="__main__":
    root=Tk()
    obj=Face_Recognition(root) 
    root.mainloop()