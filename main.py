from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
from train import Train
from attendance import Attendances
from face_recognition import Face_Recognition
import os

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        img=Image.open(r"C:\Users\ACER\Desktop\Face recognition system\img\download.jpg")
        img=img.resize((500,130),Image.ADAPTIVE)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl =Label(self.root,image =self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
        img1=Image.open(r"C:\Users\ACER\Desktop\Face recognition system\img\download.jpg")
        img1 = img1.resize((500,130),Image.ADAPTIVE)
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
        img3=Image.open(r"C:\Users\ACER\Desktop\Face recognition system\img\bg.jpg")
        img3 = img3.resize((1530,790),Image.ADAPTIVE)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img = Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=790)
        ## student detail
        
        title_lbl=Label(bg_img,text="Face Recognition Attendance System",font=("times new roman",35,"bold"),bg="#008DDA",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=80)
        
       #student button 
        img4=Image.open(r"img\studentdetail.jpg")
        img4 = img4.resize((200,150),Image.ADAPTIVE)
        self.photoimg4=ImageTk.PhotoImage(img4)
     
        b1 = Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=250,y=100,width=200,height=150)

        b1_1 = Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=250,y=250,width=200,height=40)
        
        
        #Detect face button
        img5=Image.open(r"img\facedet.jpg")
        img5 = img5.resize((200,150),Image.ADAPTIVE)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1 = Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=600,y=100,width=200,height=150)

        b1_1 = Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=600,y=250,width=200,height=40) 
    
        
        #Attendance button
        img6=Image.open(r"img\Attendance.png")
        img6 = img6.resize((220,150),Image.ADAPTIVE)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1 = Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendence_data)
        b1.place(x=950,y=100,width=200,height=150)

        b1_1 = Button(bg_img,text="Attendance",cursor="hand2",command=self.attendence_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=950,y=250,width=200,height=40)
        
        #Train face button
        
        img8=Image.open(r"img\facedetect.jpg")
        img8 = img8.resize((200,150),Image.ADAPTIVE)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1 = Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=250,y=350,width=200,height=150)

        b1_1 = Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=250,y=500,width=200,height=40)
        
        #PhotosButton
        img9=Image.open(r"img\phot.png")
        img9 = img9.resize((200,150),Image.ADAPTIVE)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1 = Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=600,y=350,width=200,height=150)

        b1_1 = Button(bg_img,text="Photo",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=600,y=500,width=200,height=40)
   
    def open_img(self):
        os.startfile("data1")      
        
        
 #===================Function buttons=================
       
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
        
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
    
    def attendence_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendances(self.new_window)
        

if __name__ == "__main__":
     root=Tk()
     obj=Face_Recognition_System(root)
     root.mainloop()