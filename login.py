from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox


class Login_Window:
    def __init__(self,root):
        self.root = root
        self.root.state('zoomed')  # Maximized but keeps minimize & close buttons
        self.root.title("Login")

        self.bg = ImageTk.PhotoImage(file=r"Images\BG 2.jpg")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="black")
        frame.place(relx=0.5, rely=0.5, anchor="center", width=340, height=450)

        img1 = Image.open(r"Images\user.png")  
        img1 = img1.resize((100, 100), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimg1, bg="black", borderwidth=0)
        lblimg1.place(x = 720,y=185,width=100,height=100) 

        get_str=Label(frame,text="Get Started",font=("Candara",20,"bold"),fg="white",bg="black")
        get_str.place(x=103,y=115)

        #Lables
        username = Label(frame, text="Username", font=("Candara", 15, "bold"), fg="white", bg="black") 
        username.place(x=70, y=165)  # Using absolute positioning

        self.txtuser = ttk.Entry(frame, font=("Candara", 15))  # Fixed bracket
        self.txtuser.place(x=40, y=195, width=270)  # Changed x from -40 to 40
  
        password = Label(frame, text="Password", font=("Candara", 15, "bold"), fg="white", bg="black") 
        password.place(x=70, y=235)  # Using absolute positioning

        self.txtpassword = ttk.Entry(frame, font=("Candara", 15),show="*")  # Fixed bracket
        self.txtpassword.place(x=40, y=265, width=270)  # Changed x from -40 to 40
        
        # Show/Hide Password Button
        self.show_password = False
        self.show_btn = Button(frame, text="Show", font=("Candara", 10, "bold"), command=self.toggle_password, borderwidth=0, fg="black", bg="white")
        self.show_btn.place(x=270, y=265, width=40, height= 28)
        
        #========Icon image =================================
        img2 = Image.open(r"Images\icons8-user-24.png")  
        img2= img2.resize((25, 25), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(image=self.photoimg2, bg="black", borderwidth=0)
        lblimg2.place(x= 638, y=337,width=25,height=25)

        img3 = Image.open(r"Images\icons8-lock-50.png")  
        img3 = img3.resize((22, 22), Image.LANCZOS)
        self.photoimg3= ImageTk.PhotoImage(img3)
        lblimg3 = Label(image=self.photoimg3, bg="black", borderwidth=0)
        lblimg3.place(x= 638, y=407,width=25,height=25)

        # Login button
        loginbtn=Button(frame,command=self.login,text="Login",font=("Candara",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="#3EB489",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=320,width=120,height=35)
        
        # Registerbutton
        registerbtn=Button(frame,text=" New User Register ",font=("Candara",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=11,y=380,width=160)
        
        # forgotpassword
        forgotbtn=Button(frame,text=" Forgot Password ? ",font=("Candara",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgotbtn.place(x=8,y=400,width=160)
        
    def toggle_password(self):
        if self.show_password:
            self.txtpassword.config(show="*")
            self.show_btn.config(text="Show")
        else:
            self.txtpassword.config(show="")
            self.show_btn.config(text="Hide")
        self.show_password = not self.show_password
        
    def login(self):

            if self.txtuser.get() == "" or self.txtpassword.get() == "":

                messagebox.showerror("Error","All fields are required")

            elif self.txtuser.get() == "vijay" and self.txtpassword.get() == "waghmare":

                messagebox.showinfo("Success","welcome to Facecheck") 
            else:
                messagebox.showerror("Invalid","Invalid Username & Password")
             

if __name__ == "__main__":
    root = Tk()
    app = Login_Window(root)
    root.mainloop()