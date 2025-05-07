from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import customtkinter as ctk
import mysql.connector

# Set appearance mode
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

class Register:
    def __init__(self, root):
        self.root = root
        self.root.state('zoomed')
        self.root.title("Register")

        # Variables
        self.var_fname = StringVar()
        self.var_contact = StringVar()
        self.var_lname = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_SecurityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        # Background Image
        self.bg = ImageTk.PhotoImage(file=r"Images\BG 2.jpg")
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        # Main Frame
        main_frame = Frame(self.root, bg="white")
        main_frame.place(x=220, y=140, width=1120, height=532)

        # Left Image
        img = Image.open(r"Images\Register 1.jpg").resize((470, 532), Image.Resampling.LANCZOS)
        self.bg1 = ImageTk.PhotoImage(img)
        left_lbl = Label(main_frame, image=self.bg1)
        left_lbl.place(x=0, y=0, width=470, height=532)

        # Registration Frame
        frame = Frame(main_frame, bg="white")
        frame.place(x=480, y=0, width=640, height=532)

        # Register Label
        img_register = Image.open(r"Images\Register Now.png").resize((220, 50), Image.Resampling.LANCZOS)
        self.register_btn = ImageTk.PhotoImage(img_register)
        register_lbl = Label(frame, image=self.register_btn, bg="white")
        register_lbl.place(x=210, y=20)

        # Labels and Entry Fields
        ctk.CTkLabel(frame, text="First Name", font=("candara", 17, "bold")).place(x=50, y=100)
        self.fname_entry = ctk.CTkEntry(frame, width=250, corner_radius=30, textvariable=self.var_fname)
        self.fname_entry.place(x=50, y=130)
        
        ctk.CTkLabel(frame, text="Last Name", font=("candara", 17, "bold")).place(x=370, y=100)
        self.lname_entry = ctk.CTkEntry(frame, width=250, corner_radius=30, textvariable=self.var_lname)
        self.lname_entry.place(x=370, y=130)

        ctk.CTkLabel(frame, text="Contact", font=("candara", 17, "bold")).place(x=50, y=170)
        self.contact_entry = ctk.CTkEntry(frame, width=250, corner_radius=30, textvariable=self.var_contact)
        self.contact_entry.place(x=50, y=200)

        ctk.CTkLabel(frame, text="Email", font=("candara", 17, "bold")).place(x=370, y=170)
        self.email_entry = ctk.CTkEntry(frame, width=250, corner_radius=30, textvariable=self.var_email)
        self.email_entry.place(x=370, y=200)

        ctk.CTkLabel(frame, text="Security Question", font=("candara", 17, "bold")).place(x=50, y=250)
        self.combo_security_Q = ctk.CTkComboBox(frame, corner_radius=30, width=250, values=["Your Birth Place", "Your Favourite Sport", "Your Pet's Name"], variable=self.var_securityQ)
        self.combo_security_Q.place(x=50, y=280)

        ctk.CTkLabel(frame, text="Security Answer", font=("candara", 17, "bold")).place(x=370, y=250)
        self.security_answer_entry = ctk.CTkEntry(frame, width=250, corner_radius=30, textvariable=self.var_SecurityA)
        self.security_answer_entry.place(x=370, y=280)

        ctk.CTkLabel(frame, text="Password", font=("candara", 17, "bold")).place(x=50, y=320)
        self.password_entry = ctk.CTkEntry(frame, width=250, show="*", corner_radius=30, textvariable=self.var_pass)
        self.password_entry.place(x=50, y=350)

        ctk.CTkLabel(frame, text="Confirm Password", font=("candara", 17, "bold")).place(x=370, y=320)
        self.confirm_password_entry = ctk.CTkEntry(frame, width=250, show="*", corner_radius=30, textvariable=self.var_confpass)
        self.confirm_password_entry.place(x=370, y=350)
        
        # Check Button
        self.var_checkbtn = IntVar()
        self.check_btn = ctk.CTkCheckBox(frame, text="I Agree The Terms & Conditions", variable=self.var_checkbtn, 
                                 checkbox_height=17, checkbox_width=17, font=("candara", 13))
        self.check_btn.place(x=45, y=390)

        # Register Button
        self.register_button = ctk.CTkButton(
            frame, 
            text="REGISTER", 
            font=("candara", 15, "bold"), 
            corner_radius=30, 
            fg_color="#3a57a5", 
            hover_color="#0056b3", 
            text_color="white", 
            width=150, 
            height=40, 
            command=self.register_data
        )
        self.register_button.place(x=50, y=430)
        
        # Login Button
        self.login_button = ctk.CTkButton(
            frame, 
            text="LOGIN", 
            font=("candara", 15, "bold"), 
            corner_radius=30, 
            fg_color="#3a57a5",
            hover_color="#0056b3",
            text_color="white", 
            width=150, 
            height=40, 
            command=self.login
        )
        self.login_button.place(x=250, y=430)

    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select":
            messagebox.showerror("Error", "All fields are required!!")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Password & Confirm Password must be the same!!")
        elif self.var_checkbtn.get() == 0:
            messagebox.showerror("Error", "Please agree to our terms and conditions")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Sujal@2002",database="face_recognition")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query, value) 
            row=my_cursor.fetchone() 
            if row!=None: 
                messagebox.showerror("Error", "User already exist, plaese try another email") 
            else: 
                my_cursor.execute("insert into register values (%s, %s, %s, %s, %s, %s, %s)",( 
                    self.var_fname.get(), 
                    self.var_lname.get(), 
                    self.var_contact.get(), 
                    self.var_email.get(), 
                    self.var_securityQ.get(), 
                    self.var_SecurityA.get(), 
                    self.var_pass.get()
                ))
            
            conn.commit()
            messagebox.showinfo("Success","Registered Successfully")
            conn.close()
            
    def login(self):
        # Implement login functionality here
        messagebox.showinfo("Info", "Login functionality is not yet implemented.")

if __name__ == "__main__":
    root = Tk()
    obj = Register(root)
    root.mainloop()
