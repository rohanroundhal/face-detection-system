from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import time
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root = root
        self.root.state('zoomed')  # Maximized but keeps minimize & close buttons
        self.root.title("Training Data Set")
        
        img = Image.open(r"Images\BG 2.jpg") #put image path in brackets
        img = img.resize((1920,1080)) 
        self.photoimg = ImageTk.PhotoImage(img) 

        bg_img=Label(self.root,image=self.photoimg) 
        bg_img.place(x=0, y=0, width=1920, height=1080)
        
        title_lbl=Label(bg_img,text="Training Data Set",font=("Candara",35,"bold"),bg="white",fg="#AB274F")
        title_lbl.place(x=450,y=20,width=650,height=60)
        
        b1_1=Button(bg_img,text="TRAIN DATA",command=self.train_classifier,font=("Calibri",12,"bold"),bg="#1F305E",fg="White",cursor="hand2")
        b1_1.place(x=650,y=348,width=180,height=40)

    def train_classifier(self):
        data_dir=("Sample Images")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]        
        
        faces=[]
        ids=[]
        
        for image in path:
            img=Image.open(image).convert('L')
            imageNp=np.array(img,'uint8')
            id = int(os.path.split(image)[1].split('_')[0])  # Extracts Student ID before '_'
            
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(50)
            cv2.waitKey(1) == 13
        ids=np.array(ids)
        
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Completed")
            
if __name__ =="__main__": 
    root=Tk()
    obj=Train(root)
    root.mainloop()