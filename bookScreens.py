import tkinter as tk
import datastructures

def open_bookMenuWindow():
  global lstBooks
  bookMenuWindow = tk.Toplevel()
  bookMenuWindow.geometry("300x300")
  bookMenuWindow.title("Book Menu")

  tk.Label(bookMenuWindow, text="Stored Books").pack()
  
  lstBooks = tk.Listbox(bookMenuWindow)
  lstBooks.pack()

  refreshBooksList()
  tk.Button(bookMenuWindow,text="Show Selected Book", command = display_selected_book).pack()  
  tk.Button (bookMenuWindow, text="Add Book", command = open_Add_Book).pack()


def open_Add_Book():
  addBookWindow = tk.Toplevel()
  addBookWindow.geometry("300x300")
  addBookWindow.title("Add Book")

  tk.Label(addBookWindow, text="Title").pack()
  temptitle = tk.StringVar()
  tk.Entry(addBookWindow,textvariable = temptitle).pack()
  
  tk.Label(addBookWindow, text="Genre").pack()
  tempgenre = tk.StringVar()
  tk.Entry(addBookWindow,textvariable = tempgenre).pack()


  
  
  def Add_Book_Submit():
    #todo validation here
    valid = True
    if valid == True:
      newbook = datastructures.book()  
      newbook.title = temptitle.get()
      newbook.genre = tempgenre.get()
      datastructures.lst_book.append(newbook)
      refreshBooksList()
      #Popup with add book????
      #close the window???
      addBookWindow.destroy()

  tk.Button(addBookWindow,text="Submit", command = Add_Book_Submit).pack()

def display_selected_book():
  global lstBooks
  if len(lstBooks.curselection()) > 0:
    displayBookWindow = tk.Toplevel()
    displayBookWindow.geometry("300x300")
    displayBookWindow.title("Show/Edit Book")    
  
    
    
    index = lstBooks.curselection()[0]
    tk.Label(displayBookWindow,text="Title" + datastructures.lst_book[index].title).pack()
    
    tk.Label(displayBookWindow, text="Genre").pack()
    tempgenre = tk.StringVar()
    tk.Entry(displayBookWindow,textvariable = tempgenre).pack()
    tempgenre.set(datastructures.lst_book[index].genre)
    def Edit_Book_Submit():
      global lstBooks
      index = lstBooks.curselection()[0]
      #todo validation here
      valid = True
      if valid == True:
        #datastructures.lst_book[index].fname = tempfname.get()
        datastructures.lst_book[index].genre = tempgenre.get()
        refreshBooksList()
        #Popup with add book????
        displayBookWindow.destroy()

  tk.Button(displayBookWindow,text="Submit", command = Edit_Book_Submit).pack()



def refreshBooksList():
  global lstBooks
  lstBooks.delete(0,tk.END)
  for book in datastructures.lst_book:
     lstBooks.insert(tk.END, book.title + book.genre)