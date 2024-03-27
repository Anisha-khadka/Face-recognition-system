import re
from tkinter import*
from tkinter import ttk
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from login import Login_Window

def register_window(self):
        #hide login window
        self.root.withdraw()
        #open the registration window and pass the login window reference
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
class Register:
    def __init__(self,root):
        self.root=root
        self.login_window=Login_Window  #store the login
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")



        #variable
        self.admin_id=StringVar()
        self.admin_username=StringVar()
        self.admin_password=StringVar()
        self.admin_repassword=StringVar()
        self.admin_fullname=StringVar()
        self.admin_email=StringVar()
        self.admin_contact=StringVar()
        self.admin_address=StringVar()
        
        def create_gradient(canvas, width, height, colors):
    # Create a gradient using a rectangle with a vertical linear gradient
            for i in range(height):
        # Interpolate between the two colors
              r = int(colors[0][0] * (height - i) / height + colors[1][0] * i / height)
              g = int(colors[0][1] * (height - i) / height + colors[1][1] * i / height)
              b = int(colors[0][2] * (height - i) / height + colors[1][2] * i / height)
              color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
              canvas.create_line(0, i, width, i, fill=color, width=1)
    
        canvas = tk.Canvas(root, width=400, height=300)
        canvas.pack(fill=tk.BOTH, expand=True)
        
        start_color = (15, 16, 53) #white
        end_color = (54, 84, 134)     #blue
        create_gradient(canvas, 1500, 800, [start_color, end_color])
        #hover
        def onregbutton(event):
            login_btn['bg']='#008DDA'
            login_btn['fg']='#00008B'
        def leaveregbutton(event):
            login_btn['bg']='#333A73'
            login_btn['fg']='white'
            
        
        ##Background image
        
      #  bg_img = Label(self.root,image=self.photoimg)
      #  bg_img.place(x=0,y=0,width=1530,height=790)

        f_frame=Frame(self.root,bd=0,relief=RIDGE,bg="#40679E")
        f_frame.place(x=320,y=140,width=900,height=500)


        #Register Label
        Register_label= Label(f_frame,text= "Register Here",font=("Victoria",30,"bold"),fg="#7FC7D9",bg="#40679E")
        Register_label.place(x=310,y=20)

         ##admin information
        frame = LabelFrame(root,bg="#40679E",fg="white", bd=0,relief=RIDGE,font=("times new roman",12,"bold"))
        frame.place(x=340,y=240,width=860,height=200)
        ##Admin ID
        admin_id= Label(frame,text= "Admin ID",font=("Victoria",15,"bold"),bg="#40679E",fg="white")
        admin_id.grid(row=0,column=0,padx=10,sticky=W,pady=10)
        
        adminID_entry = ttk.Entry(frame,textvariable=self.admin_id,width=30,font=("times new roman",12,"bold"))
        adminID_entry.grid(row=0,column=1,padx=10,sticky=W,pady=10,)
        
        #Admin Username
        username= Label(frame,text= "Username",font=("Victoria",15,"bold"),bg="#40679E",fg="white")
        username.grid(row=0,column=2,padx=10,pady=10,sticky=W)
        
        username_entry = ttk.Entry(frame,textvariable=self.admin_username,width=30,font=("times new roman",12,"bold"))
        username_entry.grid(row=0,column=3,padx=10,pady=10,sticky=W)
        ##Full name
        fullName= Label(frame,text= "FullName",font=("Victoria",15,"bold"),bg="#40679E",fg="white")
        fullName.grid(row=1,column=0,padx=10,pady=10,sticky=W)
        
        fullName_entry = ttk.Entry(frame,textvariable=self.admin_fullname,width=30,font=("times new roman",12,"bold"))
        fullName_entry.grid(row=1,column=1,padx=10,pady=10,sticky=W)
       
        ##contact
        contact= Label(frame,text= "Contact",font=("Victoria",15,"bold"),bg="#40679E",fg="white")
        contact.grid(row=1,column=2,padx=10,sticky=W)
        
        contact_entry = ttk.Entry(frame,textvariable=self.admin_contact,width=30,font=("times new roman",12,"bold"))
        contact_entry.grid(row=1,column=3,padx=10,sticky=W)

        #email
        email_label= Label(frame,text= "Email",font=("Victoria",15,"bold"),bg="#40679E",fg="white")
        email_label.grid(row=2,column=0,padx=10,sticky=W)
        
        email_entry = ttk.Entry(frame,textvariable=self.admin_email,width=30,font=("times new roman",12,"bold"))
        email_entry.grid(row=2,column=1,padx=10,sticky=W)

        ##address
        address_label= Label(frame,text= "Address",font=("Victoria",15,"bold"),bg="#40679E",fg="white")
        address_label.grid(row=2,column=2,padx=10,pady=10,sticky=W)
        
        address_entry = ttk.Entry(frame,textvariable=self.admin_address,width=30,font=("times new roman",12,"bold"))
        address_entry.grid(row=2,column=3,padx=10,pady=10,sticky=W)


         #password
        password_label= Label(frame,text= "Password",font=("Victoria",15,"bold"),bg="#40679E",fg="white")
        password_label.grid(row=3,column=0,padx=10,sticky=W)
        
        password_entry = ttk.Entry(frame,textvariable=self.admin_password,show="*",width=30,font=("times new roman",12,"bold"))
        password_entry.grid(row=3,column=1,padx=10,sticky=W)

        ##address
        repassword_label= Label(frame,text= "Retype Password",font=("Victoria",15,"bold"),bg="#40679E",fg="white")
        repassword_label.grid(row=3,column=2,padx=10,pady=10,sticky=W)
        
        repassword_entry = ttk.Entry(frame,textvariable=self.admin_repassword,show="*",width=30,font=("times new roman",12,"bold"))
        repassword_entry.grid(row=3,column=3,padx=10,pady=10,sticky=W)




        #Register button
        login_btn = Button(f_frame,text="Register",command=self.register,width=20,font=("times new roman",16,"bold"),bg="#333A73",fg="white")
        login_btn.place(x=330,y=360)
        login_btn.bind('<Enter>',onregbutton)
        login_btn.bind('<Leave>',leaveregbutton)

    def register(self):
            # Admin ID validation
        if not self.admin_id.get().isdigit() or len(self.admin_id.get()) == 0:
            messagebox.showerror("Error", "Admin ID must be a numeric value", parent=self.root)
            return

        # Admin username validation
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'  # Regular expression pattern for email
        if not re.match(email_pattern, self.admin_username.get()):
            messagebox.showerror("Error", "Invalid username", parent=self.root)
            return

        # Admin fullname validation
        if not isinstance(self.admin_fullname.get(), str) or not re.match(r'^[a-zA-Z\s]+$', self.admin_fullname.get()):
            messagebox.showerror("Error", "Admin fullname must be a string value", parent=self.root)
            return

        # Contact validation
        contact_pattern = r'^\d{10}$'  # Regular expression pattern for a 10-digit phone number
        if not re.match(contact_pattern, self.admin_contact.get()):
            messagebox.showerror("Error", "Invalid contact number", parent=self.root)
            return

        # Email validation
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'  # Regular expression pattern for email
        if not re.match(email_pattern, self.admin_email.get()):
            messagebox.showerror("Error", "Invalid email address", parent=self.root)
            return

        # Address validation
        if not isinstance(self.admin_address.get(), str) or not re.match(r'^[a-zA-Z\s]+$', self.admin_address.get()):
            messagebox.showerror("Error", "Address must be a string value", parent=self.root)
            return

        # Checking if all fields are filled out
        if (not self.admin_username.get()) or (not self.admin_fullname.get()) or (not self.admin_contact.get()) or \
                (not self.admin_email.get()) or (not self.admin_address.get()) or (not self.admin_password.get()) or \
                (not self.admin_repassword.get()):
            messagebox.showerror("Error", "All fields are required", parent=self.root)
            return

        # Checking if password and retype password match
        if self.admin_password.get() != self.admin_repassword.get():
            messagebox.showerror("Error", "Password and retype password must match", parent=self.root)
            return
        
        try:
                    conn = mysql.connector.connect(host="localhost",user="root",passwd="",database="studentattendance")
                    my_cursor = conn.cursor()
                    my_cursor.execute("insert into useradmin values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                self.admin_id.get(),
                                                                                self.admin_username.get(),
                                                                                self.admin_fullname.get(),
                                                                                self.admin_contact.get(),
                                                                                self.admin_email.get(),
                                                                                self.admin_address.get(),
                                                                                self.admin_password.get(),
                                                                                self.admin_repassword.get()
                                                                                ))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success","Registered successfully")
                    
                    self.login_window.deiconify() #show the login window again
                    #close the register window
                    self.root.destroy()
            
                
        except Exception as e:
                    messagebox.showerror("Error",f"Due to{str(e)}",parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Register(root)
    root.mainloop()