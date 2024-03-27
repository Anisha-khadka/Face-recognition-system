import re
from tkinter import*
from tkinter import ttk
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import messagebox


from main import Face_Recognition_System
import mysql.connector

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1500x800+0+0")
        #session variable
        self.session={}
        #variable
        self.admin_id=StringVar()
        self.admin_username=StringVar()
        self.admin_password=StringVar()
        
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
        def onButton(event):
            loginbtn['bg']='#008DDA'
            loginbtn['fg']='#00008B'
        def onregbutton(event):
            registerbtn['bg']='#008DDA'
            registerbtn['fg']='#00008B'
              
        def leaveButton(event):
            loginbtn['bg']='#333A73'
            loginbtn['fg']='white'
        def leaveregbutton(event):
            registerbtn['bg']='#333A73'
            registerbtn['fg']='white'
            
        ##Background image
        #root.config(bg="#161616")
       # self.bg=ImageTk.PhotoImage(file=r"img/faced.jpg")
        
       # lbl_bg = Label(self.root,image=self.bg)
       # lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        
        frame=Frame(self.root,bd=4,relief=RAISED,bg="#40679E")
        frame.place(x=350,y=140,width=850,height=490)
        

        
        ##image
        

        #f_lbl = Label(self.root,image=self.photoimg)
        #f_lbl.place(x=670,y=170,width=100,height=90)

       

        get_str=Label(frame,text="Login", font=("Victoria",45,"bold"),fg="#7FC7D9", bg="#40679E")
        get_str.place(x=100,y=40)

        #label
        #adminid

        adminID_label= Label(frame,text= "Admin_ID",font=("times new roman",15,"bold"),fg="white",bg="#40679E")
        adminID_label.place(x=135,y=140)

        adminID_entry = ttk.Entry(frame,textvariable=self.admin_id,width=20,font=("times new roman",15,"bold"))
        adminID_entry.place(x=30,y=170,width=320)
        
        #username
        user_label=Label(frame,text="Email", font=("times new roman",15,"bold"),fg="white", bg="#40679E")
        user_label.place(x=150,y=215)

        username_entry=ttk.Entry(frame,textvariable=self.admin_username,width=20,font=("times new roman",15,"bold"))
        username_entry.place(x=30,y=245,width=320)

        #password
        password_label=Label(frame,text="Password", font=("times new roman",15,"bold"),fg="white", bg="#40679E")
        password_label.place(x=140,y=290)

        password_entry=ttk.Entry(frame,textvariable=self.admin_password,font=("times new roman",15,"bold"))
        password_entry.place(x=30,y=320,width=320)

        #LoginButton
        loginbtn=Button(frame,text="Login",command=self.login,font=("times new roman",15,"bold"),bd=0, relief=RIDGE,fg="white",bg="#333A73",activeforeground="#008DDA",activebackground="#7FC7D9")
        loginbtn.place(x=30,y=400,width=140,height=35)
        loginbtn.bind('<Enter>',onButton)
        loginbtn.bind('<Leave>',leaveButton)
        #RegisterButton
        
        registerbtn=Button(frame,text="Admin Register",command=self.register_window,font=("times new roman",14,"bold"),bd=0, relief=RIDGE,fg="white",bg="#333A73",activeforeground="#008DDA",activebackground="#7FC7D9")
        registerbtn.place(x=190,y=400,width=170,height=35)
        registerbtn.bind('<Enter>',onregbutton)
        registerbtn.bind('<Leave>',leaveregbutton)
        
        get_str1=Label(frame,text="Welcome To Face Recognition Attendance System", wraplength=300, font=("Tahoma",25,"bold"),fg="#F3D7CA", bg="#40679E")
        get_str1.place(x=500,y=170)
        #forgetpassbtn
        #forgetbtn=Button(frame,text="Forget Password",font=("times new roman",12,"bold"),borderwidth=0, relief=RIDGE,fg="green",bg="lightblue",activeforeground="green",activebackground="lightblue")
        #forgetbtn.place(x=30,y=370,width=165)
   
        
    def register_window(self):
        #hide login window
        self.root.withdraw()
        #open the registration window and pass the
        self.new_window=Toplevel()
        self.app=Register(self.new_window,self.root)

    def login(self):
        if self.admin_id.get()=="" or self.admin_username.get()=="" or self.admin_password.get()=="":
            messagebox.showerror("Error","All fields required",parent=self.root)
            

        else:
            # messagebox.showerror("Error","Invalid id username password ")
            conn = mysql.connector.connect(host="localhost",user="root",passwd="",database="studentattendance")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from useradmin where Id=%s and Email=%s and Password=%s",(
                                                                                        self.admin_id.get(),
                                                                                        self.admin_username.get(), 
                                                                                        self.admin_password.get()
                                                                                        ))
            
            row = my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid id username and password")
            else:
                open_main=messagebox.askyesno("Yes no","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()
    def open_main_page(self):
        main_page_root = Tk()
        main_page = Face_Recognition_System(main_page_root)
        main_page_root.mainloop()
class Register:
    def __init__(self, root, login_window):
        self.root = root
        self.login_window = login_window  # Store the login window reference
        self.root.geometry("1530x790+0+0")
        self.root.title("Registration")

        # Variable
        self.admin_id = StringVar()
        self.admin_username = StringVar()
        self.admin_password = StringVar()
        self.admin_repassword = StringVar()
        self.admin_fullname = StringVar()
        self.admin_email = StringVar()
        self.admin_contact = StringVar()
        self.admin_address = StringVar()
        
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

        # Background image
        

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
    main()