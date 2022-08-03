from tkinter import*
# import stdDB_BackEnd
from tkinter import ttk
import random
import tkinter.messagebox 
import datetime
# import pymysql
import time
import tempfile,os
from turtle import color, left, right, title

class Student:
  def __init__(self,root):
    self.root = root
    self.root.title("Student Identification System")
    self.root.geometry("1350x800+0+0")

    stdNo = StringVar()
    stdName = StringVar()
    stdAddress = StringVar()
    stdContact = StringVar()
    stdEmail = StringVar()
    stdGuardian = StringVar()
    stdGuardianNo = StringVar()

    MainFrame = Frame(self.root, bd=5, width=1325, height=735, relief= "sunken", bg="gray")
    MainFrame.grid()

    #Setting Frames
    lowerFrame = Frame(MainFrame,width=1315, height=50, bg="gray")
    lowerFrame.grid(row=2, column=0, pady=20)
    Title = Frame(MainFrame,width=1315, height=100, bg="gray")
    Title.grid(row=0, column=0)
    upperFrame = Frame(MainFrame,width=1315, height=500, bg="gray")
    upperFrame.grid(row=1, column=0)

    leftFrame = Frame(upperFrame, width=1340, height=400,bg="gray")
    leftFrame.pack(side = LEFT)
    leftFrameInner = Frame(leftFrame, width=600, height=200, bg="gray")
    leftFrameInner.pack(side = TOP, padx=10)
   
    rightFrame = Frame(upperFrame, width=1340, height=400,bg="gray")
    rightFrame.pack(side=RIGHT)
    rightFrameInner = Frame(rightFrame, width=600, height=400, bg="gray")
    rightFrameInner.pack(side=TOP, padx=10)


    #Label: Title
    self.lblTitle = Label(Title, font=('helvetica',56,'bold'),text="Student Identification System", bg='gray')
    self.lblTitle.grid(row=0, column=0, padx=132, pady=30)


    #Label: Input Fields
    self.lblStdNo = Label(leftFrameInner, font=('helvetica',12,'bold'),text="Student Number", anchor='w', justify=LEFT, bg='gray')
    self.lblStdNo.grid(row=0, column=0, sticky=W)
    
    self.lblStdName = Label(leftFrameInner, font=('helvetica',12,'bold'),text="Student Name", anchor='w', justify=LEFT, bg='gray')
    self.lblStdName.grid(row=1, column=0, sticky=W)
    
    self.lblStdAddress = Label(leftFrameInner, font=('helvetica',12,'bold'),text="Student Address", anchor='w', justify=LEFT, bg='gray')
    self.lblStdAddress.grid(row=2, column=0, sticky=W)
    
    self.lblStdContact = Label(leftFrameInner, font=('helvetica',12,'bold'),text="Student Contact Number", anchor='w', justify=LEFT, bg='gray')
    self.lblStdContact.grid(row=3, column=0, sticky=W)
    
    self.lblStdEmail = Label(leftFrameInner, font=('helvetica',12,'bold'),text="Student Email", anchor='w', justify=LEFT, bg='gray')
    self.lblStdEmail.grid(row=4, column=0, sticky=W)
    
    self.lblStdGuardian = Label(leftFrameInner, font=('helvetica',12,'bold'),text="Guardian Name", anchor='w', justify=LEFT, bg='gray')
    self.lblStdGuardian.grid(row=5, column=0, sticky=W)
    
    self.lblStdGuardianNo = Label(leftFrameInner, font=('helvetica',12,'bold'),text="Guardian Contact Number", anchor='w', justify=LEFT, bg='gray')
    self.lblStdGuardianNo.grid(row=6, column=0, sticky=W)


    #Input: Input Fields
    self.inpStdNo = Entry(leftFrameInner, font = ('arial',12,'bold'), bd=5, width=40, justify='left', bg='gray', textvariable=stdNo)
    self.inpStdNo.grid(row=0,column=1)
    
    self.inpStdName = Entry(leftFrameInner, font = ('arial',12,'bold'), bd=5, width=40, justify='left', bg='gray', textvariable=stdName)
    self.inpStdName.grid(row=1,column=1)
    
    self.inpStdAddress = Entry(leftFrameInner, font = ('arial',12,'bold'), bd=5, width=40, justify='left', bg='gray', textvariable=stdAddress)
    self.inpStdAddress.grid(row=2,column=1)
    
    self.inpStdContact = Entry(leftFrameInner, font = ('arial',12,'bold'), bd=5, width=40, justify='left', bg='gray', textvariable=stdContact)
    self.inpStdContact.grid(row=3,column=1)
    
    self.inpStdEmail = Entry(leftFrameInner, font = ('arial',12,'bold'), bd=5, width=40, justify='left', bg='gray', textvariable=stdEmail)
    self.inpStdEmail.grid(row=4,column=1)
    
    self.inpStdGuardian = Entry(leftFrameInner, font = ('arial',12,'bold'), bd=5, width=40, justify='left', bg='gray', textvariable=stdGuardian)
    self.inpStdGuardian.grid(row=5,column=1)
    
    self.inpStdGuardianNo = Entry(leftFrameInner, font = ('arial',12,'bold'), bd=5, width=40, justify='left', bg='gray', textvariable=stdGuardianNo)
    self.inpStdGuardianNo.grid(row=6,column=1)


    #Data
    scrollx = Scrollbar(rightFrameInner, orient = HORIZONTAL)
    scrolly = Scrollbar(rightFrameInner, orient = VERTICAL)

    self.studentlist= ttk.Treeview(rightFrameInner, height=12, columns=("stdNo", "stdName", "stdAddress", "stdContact", "stdEmail", "stdGuardian", "stdGuardianNo"),show='headings', selectmode="browse", xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)

    style = ttk.Style()
    # this is set background and foreground of the treeview
    style.configure("Treeview",
                background="#E1E1E1",
                foreground="#000000",
                rowheight=25,
                fieldbackground="#E1E1E1")

    scrollx.pack(side='bottom', fill = X)
    scrolly.pack(side='right', fill = Y)

    self.studentlist.heading("stdNo", text="Student No.")
    self.studentlist.heading("stdName", text="Name")
    self.studentlist.heading("stdAddress", text="Address")
    self.studentlist.heading("stdContact", text="Contact")
    self.studentlist.heading("stdEmail", text="Email")
    self.studentlist.heading("stdGuardian", text="Guardian")
    self.studentlist.heading("stdGuardianNo", text="Guardian No.")

    self.studentlist['show'] = 'headings'

    self.studentlist.column("stdNo", width=70)
    self.studentlist.column("stdName", width=40)
    self.studentlist.column("stdAddress", width=50)
    self.studentlist.column("stdContact", width=50)
    self.studentlist.column("stdEmail", width=40)
    self.studentlist.column("stdGuardian", width=60)
    self.studentlist.column("stdGuardianNo", width=70)

    self.studentlist.pack(fill = BOTH, expand=1)

    self.btnAdd = Button(lowerFrame, font = ('arial',20,'bold'), text="Add", width=12, height=2, bg="gray").grid(row=0,column=0,padx=10)
    self.btnEdit = Button(lowerFrame, font = ('arial',20,'bold'), text="Edit", width=12, height=2, bg="gray").grid(row=0,column=1,padx=10)
    self.btnDelete = Button(lowerFrame, font = ('arial',20,'bold'), text="Delete", width=12, height=2, bg="gray").grid(row=0,column=2,padx=10)

if __name__=='__main__':
  root = Tk()
  application = Student(root)
  root.mainloop()
      