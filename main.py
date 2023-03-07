import datastructures
import webbrowser
from studentScreens import *
from loanScreens import *
from bookScreens import *
import tkinter as tk



datastructures.load_data() #loads file data

mainWindow = tk.Tk()
mainWindow.geometry("200x200")
mainWindow.title("Main Menu")

tk.Button(mainWindow,text="Student Menu",command = open_studentMenuWindow).pack()
tk.Button(mainWindow,text="Book Menu",command = open_bookMenuWindow).pack()
tk.Button(mainWindow,text="Loan Menu",command = open_loanMenuWindow).pack()

tk.Button(mainWindow,text="Save Data",command = datastructures.save_data).pack()

def printLoans():
  htmlinsert = ""
  htmlrecordtemplate = "<tr><td>#student</td><td>#book</td><td>#date</td></tr>\n"
  for loan in datastructures.lst_loan:
    temp = ""
    temp = htmlrecordtemplate.replace("#student",datastructures.lst_student[loan.studentid].fname)
    temp = temp.replace("#book",datastructures.lst_book[loan.bookid].title)
    temp = temp.replace("#date",str(loan.dateofloan))
    htmlinsert += temp
  fh = open("calendarprintingtemplate.html","r")
  template = fh.read()
  fh.close()

  htmloutput = template.replace("##REPEATROWSHERE##",htmlinsert)

  fh = open("report.html","w")
  fh.write(htmloutput)
  fh.close()
  
  webbrowser.open("calendarprintintemplate.html") 
  #Unfortunately this doesn't work in replit!!!!

tk.Button(mainWindow,text="Print Loans",command = printLoans).pack()







mainWindow.mainloop()
