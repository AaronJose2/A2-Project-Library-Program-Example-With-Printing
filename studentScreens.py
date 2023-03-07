import tkinter as tk
import datastructures


def open_studentMenuWindow():
  global lstStudents
  studentMenuWindow = tk.Toplevel()
  studentMenuWindow.geometry("300x300")
  studentMenuWindow.title("Student Menu")

  tk.Label(studentMenuWindow, text="Stored Students").pack()
  
  lstStudents = tk.Listbox(studentMenuWindow)
  lstStudents.pack()

  refreshStudentsList()
  tk.Button(studentMenuWindow,text="Show Selected Student", command = display_selected_student).pack()  
  tk.Button (studentMenuWindow, text="Add Student", command = open_Add_Student).pack()


def open_Add_Student():
  addStudentWindow = tk.Toplevel()
  addStudentWindow.geometry("300x300")
  addStudentWindow.title("Add Student")

  tk.Label(addStudentWindow, text="First Name").pack()
  tempfname = tk.StringVar()
  tk.Entry(addStudentWindow,textvariable = tempfname).pack()
  
  tk.Label(addStudentWindow, text="Surname").pack()
  tempsname = tk.StringVar()
  tk.Entry(addStudentWindow,textvariable = tempsname).pack()


  
  
  def Add_Student_Submit():
    #todo validation here
    valid = True
    if valid == True:
      newstudent = datastructures.student()  
      newstudent.fname = tempfname.get()
      newstudent.sname = tempsname.get()
      datastructures.lst_student.append(newstudent)
      refreshStudentsList()
      #Popup with add student????
      #close the window???
      addStudentWindow.destroy()

  tk.Button(addStudentWindow,text="Submit", command = Add_Student_Submit).pack()

def display_selected_student():
  global lstStudents
  if len(lstStudents.curselection()) > 0:
    displayStudentWindow = tk.Toplevel()
    displayStudentWindow.geometry("300x300")
    displayStudentWindow.title("Show/Edit Student")    
  
    
    
    index = lstStudents.curselection()[0]
    tk.Label(displayStudentWindow,text="First Name" + datastructures.lst_student[index].fname).pack()
    
    tk.Label(displayStudentWindow, text="Surname").pack()
    tempsname = tk.StringVar()
    tk.Entry(displayStudentWindow,textvariable = tempsname).pack()
    tempsname.set(datastructures.lst_student[index].sname)
    def Edit_Student_Submit():
      global lstStudents
      index = lstStudents.curselection()[0]
      #todo validation here
      valid = True
      if valid == True:
        #datastructures.lst_student[index].fname = tempfname.get()
        datastructures.lst_student[index].sname = tempsname.get()
        refreshStudentsList()
        #Popup with add student????
        displayStudentWindow.destroy()

  tk.Button(displayStudentWindow,text="Submit", command = Edit_Student_Submit).pack()



def refreshStudentsList():
  global lstStudents
  lstStudents.delete(0,tk.END)
  for student in datastructures.lst_student:
     lstStudents.insert(tk.END, student.fname + student.sname)