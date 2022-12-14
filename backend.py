import sqlite3


def studentData():
    con = sqlite3.connect("main.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS student (Student_Number text, Student_Name text, Student_Address text, Contact_Number text, Student_Email text, Guardian_Name text, PContact_Number text")
    con.commit()
    con.close()


def addstudent(Student_Number, Student_Name, Student_Address, Contact_Number, Student_Email, Guardian_Name, PContactNumber):
    con = sqlite3.connect("main.db")
    cur = con.cursor()
    cur.execute("INSERT INTO student VALUES (?,?,?,?,?,?,?)", (Student_Number, Student_Name, Student_Address, Contact_Number, Student_Email, Guardian_Name, PContactNumber,))
    con.commit()
    con.close()

def viewData():
    con = sqlite3.connect("main.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM student")
    rows = cur.fetchall()
    con.close()
    return rows

def deleteRec(Student_Number): 
    con = sqlite3.connect("main.db")
    cur = con.cursor()
    cur.execute("DELETE FROM student WHERE Student_Number=?", (Student_Number,))
    con.commit()
    con.close

def editRec(Student_Number, Student_Name, Student_Address, Contact_Number, Student_Email, Guardian_Name, PContactNumber,id):
    con = sqlite3.connect("main.db")
    cur = con.cursor()
    cur.execute("update student set Student_Number=?, Student_Name=?, Student_Address=?, Contact_Number=?, Student_Email=?, Guardian_Name=?, PContact_Number=? where student_number=?", (Student_Number, Student_Name, Student_Address, Contact_Number, Student_Email, Guardian_Name, PContactNumber,id))
    con.commit()
    con.close()