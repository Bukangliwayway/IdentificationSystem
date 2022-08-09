import string
from tkinter import *
from xml.etree.ElementTree import tostring
import backend
from tkinter import ttk
import random
import tkinter.messagebox

import datetime
import pymysql
import time
import tempfile, os


class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1200x600")
        
        self.Exit_Btn = PhotoImage(file="asset/btnExit.png")
        
        
        
        Student_Number = StringVar()
        Student_Name = StringVar()
        Student_Address = StringVar()
        Contact_Number = StringVar()
        Student_Email = StringVar()
        Guardian_Name = StringVar()
        PContact_Number = StringVar()
        Student_Course = StringVar()
#---------------------------------------------------------------------------------------------------------------------#
        def iExit():
            iExit = tkinter.messagebox.askyesno("Student Management System", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return
            
        def iReset():
            #STUDENTNUMBER
            self.txtStudent_Number.delete(0, END)
            #STUDENTNAME
            self.txtStudent_Name.delete(0, END)
            #STUDENTADDRESS
            self.txtStudent_Address.delete(0, END)
            #CONTACT NUMBER
            self.txtContactNumber.delete(0, END)
            #STUDENTEMAIL
            self.txtStudent_Email.delete(0, END)
            #GUARDIAN NAME
            self.txtGuardian_Name.delete(0, END)
            #GUARDIAN NUMBER
            self.txtPContact_Number.delete(0, END)
            
        def addData():
            if Student_Number.get() == "" or Student_Name.get() == "":
                tkinter.messagebox.showerror("Error!","Every fields are required!")
            else:
                backend.addstudent(
                    Student_Number.get(),
                    Student_Name.get(),
                    Student_Address.get(),
                    Contact_Number.get(),
                    Student_Email.get(),
                    Guardian_Name.get(),
                    PContact_Number.get())
                iReset()
                displayData()
                tkinter.messagebox.showinfo("Data Entry Form", "Data Successfully Added")

                # super(self,self.studentlist).delete()
                # self.studentlist.insert(END, (
                #     Student_Number.get(),
                #     Student_Name.get(),
                #     Student_Address.get(),
                #     Contact_Number.get(),
                #     Student_Email.get(),
                #     Guardian_Name.get(),
                #     PContact_Number.get()))
        
        def editData():
            backend.editRec(
                Student_Number.get(),
                Student_Name.get(),
                Student_Address.get(),
                Contact_Number.get(),
                Student_Email.get(),
                Guardian_Name.get(),
                PContact_Number.get(),
                prevID)
            iReset()
            displayData()
            tkinter.messagebox.showinfo("Data Entry Form", "Data Successfully Updated")

        def displayData():
            result = backend.viewData()
            if len(result) != 0:
                self.studentlist.delete(*self.studentlist.get_children())
                for row in result:
                    self.studentlist.insert('', END, values=row)
        
        def deleteData():
            global sd
            if (len(Student_Number.get()) != ''):
                if(tkinter.messagebox.askyesno("Student Management System", "Are You Sure You Want To Delete\n" + str(sd[1]) + " ?")):
                    backend.deleteRec(sd[0])
                    iReset()
                    displayData()
                    tkinter.messagebox.showinfo("Data Entry Form", "Data Successfully Deleted")

        def studentRec(event):
            global sd
            iReset()
            viewInfo = self.studentlist.focus()
            learnerData = self.studentlist.item(viewInfo)
            sd = learnerData['values']
            
        def displayInfos():
            #STUDENTNUMBER
            self.txtStudent_Number.insert(END, sd[0])
            #STUDENTNAME
            self.txtStudent_Name.insert(END, sd[1])
            #STUDENTADDRESS
            self.txtStudent_Address.insert(END, sd[2])
            #CONTACT NUMBER
            self.txtContactNumber.insert(END, sd[3])
            #STUDENTEMAIL
            self.txtStudent_Email.insert(END, sd[4])
            #GUARDIAN NAME
            self.txtGuardian_Name.insert(END, sd[5])
            #GUARDIAN NUMBER
            self.txtPContact_Number.insert(END, sd[6])
            global prevID 
            prevID = sd[0] # for editing purposes
#---------------------------------------------------------------------------------------------------------------------#
        MainFrame = Frame(self.root, bd=10, bg="gray", width=1300, height=700, relief=RIDGE)
        MainFrame.grid()
        
        # Setting Frames
        lowerFrame = Frame(MainFrame,width=1300, height=50, bg="gray")
        lowerFrame.grid(row=2, column=0, pady=20)   #BOTTOM
        Title = Frame(MainFrame,width=1315, height=100, bg="gray")
        Title.grid(row=0, column=0)
        upperFrame = Frame(MainFrame,width=1315, height=500, bg="gray")
        upperFrame.grid(row=1, column=0)

        leftFrame = Frame(upperFrame, width=1300, height=400,bg="gray")
        leftFrame.pack(side = LEFT)
        leftFrameInner = Frame(leftFrame, width=600, height=200, bg="gray")
        leftFrameInner.pack(side = TOP, padx=10)
    
        rightFrame = Frame(upperFrame, width=1300, height=400,bg="gray")
        rightFrame.pack(side=RIGHT)
        rightFrameInner = Frame(rightFrame, width=600, height=400, bg="gray")
        rightFrameInner.pack(side=TOP, padx=10)

#---------------------------------------------------------------------------------------------------------------------#
        self.lblTitle = Label(Title, text="Student Information System", font=("Arial", 40, "bold"), bg="gray", fg="white")
        self.lblTitle.grid(row=0, column=0, padx=100)

#---------------------------------------------------------------------------------------------------------------------#
        #STUDENTNUMBER
        self.lblStudent_Number = Label(leftFrameInner, text="Student Number", font=("Arial", 12, "bold"), bg="gray", fg="black", anchor=W, justify=LEFT)
        self.lblStudent_Number.grid(row=0, column=0, padx=5, sticky=W)
        self.txtStudent_Number = Entry(leftFrameInner, font=("Arial", 12, "bold"), bg="white", fg="black", width = 40, justify='left', textvariable=Student_Number)
        self.txtStudent_Number.grid(row=0, column=1)
        #STUDENTNAME
        self.lblStudent_Name = Label(leftFrameInner, text="Student Name", font=("Arial", 12, "bold"), bg="gray", fg="black", anchor=W, justify=LEFT)
        self.lblStudent_Name.grid(row=1, column=0, padx=5, sticky=W)
        self.txtStudent_Name = Entry(leftFrameInner, font=("Arial", 12, "bold"), bg="white", fg="black", width = 40, justify='left', textvariable=Student_Name)
        self.txtStudent_Name.grid(row=1, column=1)
        
        #COURSE
        self.lblCourse = Label(leftFrameInner, text="Course", font=("Arial", 12, "bold"), bg="gray", fg="black", anchor=W, justify=LEFT)
        self.lblCourse.grid(row=2, column=0, padx=5, sticky=W)
        self.cbCourse = ttk.Combobox(leftFrameInner, font=("Arial", 12, "bold"), width = 38, justify='left', textvariable=Student_Course, state='readonly')
        self.cbCourse['values'] = ('','BSIT','BSEM', 'BSCS')
        self.cbCourse.current(0)
        self.cbCourse.grid(row=2, column=1)
        
        #STUDENTADDRESS 
        self.lblStudent_Address = Label(leftFrameInner, text="Student Address", font=("Arial", 12, "bold"), bg="gray", fg="black", anchor=W, justify=LEFT)
        self.lblStudent_Address.grid(row=3, column=0, padx=5, sticky=W)
        self.txtStudent_Address = Entry(leftFrameInner, font=("Arial", 12, "bold"), bg="white", fg="black", width = 40, justify='left', textvariable=Student_Address)
        self.txtStudent_Address.grid(row=3, column=1)

        #CONTACT NUMBER
        self.lblContactNumber = Label(leftFrameInner, text="Student Contact Number", font=("Arial", 12, "bold"), bg="gray", fg="black", anchor=W, justify=LEFT)
        self.lblContactNumber.grid(row=4, column=0, padx=5, sticky=W)
        self.txtContactNumber = Entry(leftFrameInner, font=("Arial", 12, "bold"), bg="white", fg="black", width = 40, justify='left', textvariable=Contact_Number)
        self.txtContactNumber.grid(row=4, column=1)
        
        #STUDENTEMAIL
        self.lblStudent_Email = Label(leftFrameInner, text="Student Email", font=("Arial", 12, "bold"), bg="gray", fg="black", anchor=W, justify=LEFT)
        self.lblStudent_Email.grid(row=5, column=0, padx=5, sticky=W)
        self.txtStudent_Email = Entry(leftFrameInner, font=("Arial", 12, "bold"), bg="white", fg="black", width = 40, justify='left', textvariable=Student_Email)
        self.txtStudent_Email.grid(row=5, column=1)
        
        #GUARDIAN NAME
        self.lblGuardian_Name = Label(leftFrameInner, text="Guardian Name", font=("Arial", 12, "bold"), bg="gray", fg="black", anchor=W, justify=LEFT)
        self.lblGuardian_Name.grid(row=6, column=0, padx=5, sticky=W)
        self.txtGuardian_Name = Entry(leftFrameInner, font=("Arial", 12, "bold"), bg="white", fg="black", width = 40, justify='left', textvariable=Guardian_Name)
        self.txtGuardian_Name.grid(row=6, column=1)
        
        #GUARDIAN NUMBER
        self.lblPContact_Number = Label(leftFrameInner, text="Guardian Number", font=("Arial", 12, "bold"), bg="gray", fg="black", anchor=W, justify=LEFT)
        self.lblPContact_Number.grid(row=7, column=0, padx=5, sticky=W)
        self.txtPContact_Number = Entry(leftFrameInner, font=("Arial", 12, "bold"), bg="white", fg="black", width = 40, justify='left', textvariable=PContact_Number)
        self.txtPContact_Number.grid(row=7, column=1)

#---------------------------------------------------------------------------------------------------------------------#
        #UI DISPLAY OF DATA
        #TREEVIEW DATA
        scrollx = Scrollbar(rightFrameInner, orient = HORIZONTAL)
        scrolly = Scrollbar(rightFrameInner, orient = VERTICAL)
        
        self.studentlist = ttk.Treeview(rightFrameInner, columns=("Student_Number", "Student_Name", "Student_Address", "Contact_Number", "Student_Email", "Guardian_Name", "Guardian_Number"), selectmode="extended", height=12, yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        
        style = ttk.Style()
        # this is set background and foreground of the treeview
        style.configure("Treeview",
                    background="#E1E1E1",
                    foreground="#000000",
                    rowheight=25,
                    fieldbackground="#E1E1E1")
        
        scrollx.pack(side='bottom', fill = X)
        scrolly.pack(side='right', fill = Y)

        self.studentlist.heading("Student_Number", text="Student No.")
        self.studentlist.heading("Student_Name", text="Name")
        self.studentlist.heading("Student_Address", text="Address")
        self.studentlist.heading("Contact_Number", text="Contact")
        self.studentlist.heading("Student_Email", text="Email")
        self.studentlist.heading("Guardian_Name", text="Guardian")
        self.studentlist.heading("Guardian_Number", text="Guardian No.")
        
        self.studentlist['show'] = 'headings'
        
        self.studentlist.column("Student_Number", width=100)
        self.studentlist.column("Student_Name", width=100)
        self.studentlist.column("Student_Address", width=70)
        self.studentlist.column("Contact_Number", width=70)
        self.studentlist.column("Student_Email", width=70)
        self.studentlist.column("Guardian_Name", width=70)
        self.studentlist.column("Guardian_Number", width=70)

        self.studentlist.pack(fill = BOTH, expand=True)
        self.studentlist.bind("<ButtonRelease-1>",studentRec)
        displayData()
        
        self.btnAdd = Button(lowerFrame, font = ('arial',20,'bold'), text="Add", width=10, height=2, bg="gray", command=addData).grid(row=0,column=0,padx=10)
        self.btnClear = Button(lowerFrame, font = ('arial',20,'bold'), text="Clear", width=10, height=2, bg="gray", command=iReset).grid(row=0,column=1,padx=10)
        self.btnDisplay = Button(lowerFrame, font = ('arial',20,'bold'), text="Display", width=10, height=2, bg="gray", command=displayInfos).grid(row=0,column=2,padx=10)
        self.btnEdit = Button(lowerFrame, font = ('arial',20,'bold'), text="Edit", width=10, height=2, bg="gray", command=editData).grid(row=0,column=3,padx=10)
        self.btnDelete = Button(lowerFrame, font = ('arial',20,'bold'), text="Delete", width=10, height=2, bg="gray", command=deleteData).grid(row=0,column=4,padx=10)
        self.btnExit = Button(lowerFrame, font = ('arial',20,'bold'), image=self.Exit_Btn, borderwidth=0, width=70, height=70, bg="gray", command=iExit).grid(row=0,column=5,padx=10)

        
if __name__=='__main__':
    root = Tk()
    application = Student(root)
    root.resizable(False, False)
    root.mainloop()
        