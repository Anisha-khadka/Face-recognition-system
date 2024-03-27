import re
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #===========variable ===========
        self.std_id=StringVar()
        self.std_roll=StringVar()
        self.std_name=StringVar()
        self.std_contact=StringVar()
        self.std_email=StringVar()
        self.std_address=StringVar()


        ##First image
        img=Image.open(r"C:\Users\ACER\Desktop\Face recognition system\img\download.jpg")
        img = img.resize((500,130),Image.ADAPTIVE)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        ##second Image
        img1=Image.open(r"C:\Users\ACER\Desktop\Face recognition system\img\download.jpg")
        img1 = img1.resize((300,130),Image.ADAPTIVE)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

        ##3rd Image
        img2=Image.open(r"C:\Users\ACER\Desktop\Face recognition system\img\download.jpg")
        img2 = img2.resize((500,130),Image.ADAPTIVE)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=130)

        ##Background image
        img3=Image.open(r"C:\Users\ACER\Desktop\Face recognition system\img\download.jpg")
        img3 = img3.resize((1530,790),Image.ADAPTIVE)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img = Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=790)
        
        title_lbl=Label(bg_img,text="Student Attendance system",font=("times new roman",35,"bold"),bg="green",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=55)

        main_frame = Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=65,width=1480,height=550)
        #Left Frame
        Left_frame = LabelFrame(main_frame,bg="white", bd=2,relief=RIDGE,text = "Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=650,height=580)


        ##Class student information
        class_student_frame = LabelFrame(Left_frame,bg="white", bd=2,relief=RIDGE,text = "Class Student Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=10,y=10,width=630,height=300)
        ##Student ID
        student_id= Label(class_student_frame,text= "Student ID",font=("times new roman",12,"bold"),bg="white")
        student_id.grid(row=0,column=0,padx=10,sticky=W)
        
        studentID_entry = ttk.Entry(class_student_frame,textvariable=self.std_id,width=20,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,sticky=W)
        
        #stundent roll
        student_roll_label= Label(class_student_frame,text= "Student Roll",font=("times new roman",12,"bold"),bg="white")
        student_roll_label.grid(row=0,column=2,padx=10,pady=10,sticky=W)
        
        student_roll_entry = ttk.Entry(class_student_frame,textvariable=self.std_roll,width=20,font=("times new roman",12,"bold"))
        student_roll_entry.grid(row=0,column=3,padx=10,pady=1,sticky=W)
        ##Student Name
        student_name_label= Label(class_student_frame,text= "Student Name",font=("times new roman",12,"bold"),bg="white")
        student_name_label.grid(row=1,column=0,padx=10,sticky=W)
        
        student_name_entry = ttk.Entry(class_student_frame,textvariable=self.std_name,width=20,font=("times new roman",12,"bold"))
        student_name_entry.grid(row=1,column=1,padx=10,sticky=W)
       
        ##contact
        contact_label= Label(class_student_frame,text= "Student Contact",font=("times new roman",12,"bold"),bg="white")
        contact_label.grid(row=1,column=2,padx=10,sticky=W)
        
        contact_entry = ttk.Entry(class_student_frame,textvariable=self.std_contact,width=20,font=("times new roman",12,"bold"))
        contact_entry.grid(row=1,column=3,padx=10,sticky=W)

        #email
        email_label= Label(class_student_frame,text= "Student email",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=2,column=0,padx=10,sticky=W)
        
        email_entry = ttk.Entry(class_student_frame,textvariable=self.std_email,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=2,column=1,padx=10,sticky=W)

        ##address
        address_label= Label(class_student_frame,text= "Student Address",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=2,column=2,padx=10,pady=10,sticky=W)
        
        address_entry = ttk.Entry(class_student_frame,textvariable=self.std_address,width=20,font=("times new roman",12,"bold"))
        address_entry.grid(row=2,column=3,padx=10,pady=10,sticky=W)



        ##button frame

        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=5,y=180,width=618,height=35)

        ##save
        save_btn = Button(btn_frame,text="Save",command=self.add_data,width=16,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        ##update
        save_btn = Button(btn_frame,text="Update",command=self.update_data,width=16,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=1)

        ##delete
        save_btn = Button(btn_frame,text="Delete",command=self.delete_data,width=16,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=2)

        ##reset
        save_btn = Button(btn_frame,text="Reset",command=self.reset_data,width=16,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=3)

        #####btn frame1
        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=150,y=215,width=300,height=35)
        
      
        ##take photo sample
        take_photo_btn = Button(btn_frame1,text="Take photo sample",command=self.generate_dataset,width=33,font=("times new roman",12,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=3)

        
          ##rignt
        right_frame = LabelFrame(main_frame,bg="white", bd=2,relief=RIDGE,text = "Student information",font=("times new roman",12,"bold"))
        right_frame.place(x=680,y=10,width=650,height=580)


        
        # =============table frame=============
        table_frame = Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=20,width=630,height=450)
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("Student_ID","Roll","Name","Contact","Email","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("Student_ID",text="Student_ID")
        self.student_table.heading("Roll",text="Roll")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Contact",text="Contact")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Address",text="Address")
        self.student_table["show"]="headings"

        self.student_table.column("Student_ID",width=100)
        self.student_table.column("Roll",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Contact",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Address",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()




    ########===============Function declaration===============
    
    def add_data(self):
        if self.std_id.get()=="" or self.std_roll.get()==""or self.std_name.get()=="" or self.std_contact.get()=="" or self.std_email.get()=="" or self.std_address.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif not self.std_id.get().isdigit():
            messagebox.showerror("Error", "Student ID must be a numeric value", parent=self.root)
        elif not self.std_roll.get().isdigit():
            messagebox.showerror("Error", "Student roll no must be a numeric value", parent=self.root)
        elif not re.match(r'^[a-zA-Z\s]+$', self.std_name.get()):
                messagebox.showerror("Error", "Student name must contain only alphabetic characters", parent=self.root)
        elif not re.match(r'^[0-9]{10}$', self.std_contact.get()):
            messagebox.showerror("Error", "Contact number must contain exactly 10 numeric digits", parent=self.root)
        elif not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', self.std_email.get()):
            messagebox.showerror("Error", "Invalid email address", parent=self.root)
        elif not re.match(r'^[a-zA-Z\s]+$', self.std_address.get()):
            messagebox.showerror("Error", "Address must contain only alphabetic characters", parent=self.root)
        
        else:
            try:
                conn = mysql.connector.connect(host="localhost",user="root",password="",database="student_db")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s)",(
                                                                                    self.std_id.get(),
                                                                                    self.std_roll.get(),
                                                                                    self.std_name.get(),
                                                                                    self.std_contact.get(),
                                                                                    self.std_email.get(),
                                                                                    self.std_address.get()
                                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details saved successfully")
            except Exception as e:
                messagebox.showerror("Error",f"Due to{str(e)}",parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",user="root",password="",database="student_db")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()


#===============get cursor============

    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data = content["values"]

        self.std_id.set(data[0]),
        self.std_roll.set(data[1]),
        self.std_name.set(data[2]),
        self.std_contact.set(data[3]),
        self.std_email.set(data[4]),
        self.std_address.set(data[5]),


    #######============update ===========
    def update_data(self):
        if self.std_id.get()=="" or self.std_roll.get()==""or self.std_name.get()=="" or self.std_contact.get()=="" or self.std_email.get()=="" or self.std_address.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif not self.std_id.get().isdigit():
            messagebox.showerror("Error", "Student ID must be a numeric value", parent=self.root)
        elif not self.std_roll.get().isdigit():
            messagebox.showerror("Error", "Student roll no must be a numeric value", parent=self.root)
        elif not re.match(r'^[a-zA-Z\s]+$', self.std_name.get()):
            messagebox.showerror("Error", "Student name must contain only alphabetic characters", parent=self.root)
        elif not re.match(r'^[0-9]{10}$', self.std_contact.get()):
            messagebox.showerror("Error", "Contact number must contain exactly 10 numeric digits", parent=self.root)
        elif not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', self.std_email.get()):
            messagebox.showerror("Error", "Invalid email address", parent=self.root)
        elif not re.match(r'^[a-zA-Z\s]+$', self.std_address.get()):
            messagebox.showerror("Error", "Address must contain only alphabetic characters", parent=self.root)
        else:
            try:
                update = messagebox.askyesno("update","Do you want to upadte student details?",parent=self.root)
                if update>0:
                    conn = mysql.connector.connect(host="localhost",user="root",password="",database="student_db")
                    my_cursor = conn.cursor()
                    sql="update student set Roll=%s,Name=%s,Contact=%s,Email=%s,Address=%s where Student_ID=%s"
                    my_cursor.execute(sql,(
                                                                                    
                                            self.std_roll.get(),
                                            self.std_name.get(),
                                            self.std_contact.get(),
                                            self.std_email.get(),
                                            self.std_address.get(),
                                            self.std_id.get(),
                                            ))
                  
                                     
                else:
                    if not update:
                        return
                messagebox.showinfo("success","Student details update successfully",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as e:
                messagebox.showerror("Error",f"Due to {str(e)}",parent=self.root)


    ######Delete function============
    def delete_data(self):
        
        if self.std_id.get()=="":
            messagebox.showerror("Error","Student id must be required ",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student delete page","Dou you want to delete this student ",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost",user="root",password="",database="student_db")
                    my_cursor = conn.cursor()
                    sql="delete from student where Student_ID=%s"
                    val=(self.std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully delted ",parent=self.root)
            except Exception as e:
                messagebox.showerror("Error",f"Due to {str(e)}",parent=self.root)           

    ######reset function
    def reset_data(self):
        self.std_id.set("")
        self.std_roll.set("")
        self.std_name.set("")
        self.std_contact.set("")
        self.std_email.set("")
        self.std_address.set("")
    # ##Generate  data set or take photo samples==========
    def generate_dataset(self):
        pass
        if self.std_id.get()=="" or self.std_roll.get()==""or self.std_name.get()=="" or self.std_contact.get()=="" or self.std_email.get()=="" or self.std_address.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",user="root",password="",database="student_db")
                my_cursor = conn.cursor()
                my_cursor.execute("select *from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                sql="update student set Roll=%s,Name=%s,Contact=%s,Email=%s,Address=%s where Student_ID=%s"
                my_cursor.execute(sql,(
                                                                                            
                                        self.std_roll.get(),
                                        self.std_name.get(),
                                        self.std_contact.get(),
                                        self.std_email.get(),
                                        self.std_address.get(),
                                        self.std_id.get()==id+1
                                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #========load predefined data on face frontal from opencv=====
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3 by default
                    #minimun neighbour=5

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data1/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(90,90),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generated data sets ")

            except Exception as e:
                messagebox.showerror("Error",f"Due to {str(e)}",parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()