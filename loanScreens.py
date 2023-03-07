import tkinter as tk
import datastructures
import datetime

def open_loanMenuWindow():
  global lstStudents,lstBooks, lstLoans
  loanMenuWindow = tk.Toplevel()
  loanMenuWindow.geometry("500x700")
  loanMenuWindow.title("Loan Menu")

  tk.Label(loanMenuWindow, text="Stored Students").pack()
  lstStudents = tk.Listbox(loanMenuWindow,exportselection=0)
  lstStudents.pack()
  refreshStudentsList()  
  
  tk.Label(loanMenuWindow, text="Stored Books").pack()
  lstBooks = tk.Listbox(loanMenuWindow,exportselection=0)
  lstBooks.pack()
  refreshBooksList()

  def loanBook():
    newloan = datastructures.loan()
    newloan.studentid = lstStudents.curselection()[0]
    newloan.bookid = lstBooks.curselection()[0]
    newloan.dateofloan = datetime.date.today()
    datastructures.lst_loan.append(newloan)
    refreshLoansList()
  tk.Button(loanMenuWindow,text="Loan Selected",command=loanBook).pack()
  
  tk.Label(loanMenuWindow, text="Stored Books").pack()
  lstLoans = tk.Listbox(loanMenuWindow,exportselection=0,width=75)
  lstLoans.pack()
  refreshLoansList()
  
  
def refreshLoansList():
  global lstLoans
  lstLoans.delete(0,tk.END)
  for loan in datastructures.lst_loan:
     name = datastructures.lst_student[loan.studentid].fname
     name += datastructures.lst_student[loan.studentid].sname
     title = datastructures.lst_book[loan.bookid].title
    
     lstLoans.insert(tk.END, name + title + str(loan.dateofloan))


def refreshStudentsList():
  global lstStudents
  lstStudents.delete(0,tk.END)
  for student in datastructures.lst_student:
     lstStudents.insert(tk.END, student.fname + student.sname)
def refreshBooksList():
  global lstBooks
  lstBooks.delete(0,tk.END)
  for book in datastructures.lst_book:
     lstBooks.insert(tk.END, book.title + book.genre)  
