from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendances:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x790+0+0")
        self.root.title("Face recognition system")

        #=====variable===
        self.var_atten_address=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()


          ##First image
        img=Image.open(r"C:\Users\ACER\Desktop\Face recognition system\img\download.jpg")
        img = img.resize((500,130),Image.ADAPTIVE)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        ##second Image
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
        img3=Image.open(r"C:\Users\ACER\Desktop\Face recognition system\img\download.jpg")
        img3 = img3.resize((1530,790),Image.ADAPTIVE)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img = Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=790)
        
        title_lbl=Label(bg_img,text="Student Attendance Records",font=("times new roman",35,"bold"),bg="green",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=55)

        main_frame = Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=65,width=1480,height=550)
        
         #Left Frame
        Left_frame = LabelFrame(main_frame,bg="white", bd=2,relief=RIDGE,font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=660,height=580)

        img_left=Image.open(r"C:\Users\ACER\Desktop\Face recognition system\img\girl.jpeg")
        img_left=img_left.resize((720,130),Image.ADAPTIVE)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=150)

        left_inside_frame = Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=10,y=160,width=640,height=150)

        #labels and entry
        
        
         ##button frame

        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=5,y=50,width=618,height=35)

        ##Import
        save_btn = Button(btn_frame,text="Import csv",command=self.importCsv,width=35,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        ##Export
        save_btn = Button(btn_frame,text="Export csv",command=self.exportCsv,width=35,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=1)

     


        #right frame label
        Right_frame = LabelFrame(main_frame,bg="white", bd=2,relief=RIDGE,text = "Attendance Detail",font=("times new roman",12,"bold"))
        Right_frame.place(x=680,y=10,width=770,height=580)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=750,height=500)

        #===scroll bar label===
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("roll","name","address","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("address",text="Address")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")
        
        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("address",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

         
      #===========fetch data ==========
    def fetchData(self,rows):
      self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
      for i in rows:
        self.AttendanceReportTable.insert("",END,values=i)



    #import csv
    def importCsv(self): 
      global mydata
      mydata.clear()
      fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
      with open(fln) as myfile:
        csvread=csv.reader(myfile,delimiter=",")
        for i in csvread:
          mydata.append(i)
        self.fetchData(mydata)
    
    #export csv
    def exportCsv(self):
      try:
        if len(mydata)<1:
          messagebox.showerror("No data ","No data found to export",parent=self.root)
          return False
        fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln,mode="w",newline="") as myfile:
          exp_write=csv.writer(myfile,delimiter=",") 
          for i in mydata:
            exp_write.writerow(i)
          messagebox.showinfo("Data Export","Your data exported to"+os.path.basename(fln)+"Successfully")
      except Exception as e:
        messagebox.showerror("Error",f"Due to{str(e)}",parent=self.root)

    def get_cursor(self,event=""):
      cursor_row=self.AttendanceReportTable.focus()
      content=self.AttendanceReportTable.item(cursor_row)
      rows=content['values']
      self.var_atten_roll.set(rows[0])
      self.var_atten_name.set(rows[1])
      self.var_atten_time.set(rows[2])
      self.var_atten_date.set(rows[3])
      self.var_atten_address.set(rows[4])
      self.var_atten_attendance.set(rows[5])



if __name__ == "__main__":
    root = Tk()
    obj = Attendances(root)
    root.mainloop()