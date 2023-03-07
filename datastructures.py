from pickle import *
class student():
  fname = ""
  sname = ""
  #dob = ""
  #address = ""
  #other fields could be added here

class book():
  title = ""
  genre = ""
  #ISBN = ""
  #Price = ""
  #add other fields here

class loan():
  studentid = -1
  bookid = -1
  dateofloan = "NA"
  #Other fields here

def load_data():
  #Loads the data from the files, or creates blank lists
  global lst_student, lst_book,  lst_loan
  try:
    fh = open("library.data","rb")
    lst_student = load(fh)
    lst_book = load(fh)
    lst_loan = load(fh)
    fh.close()
  except:
    lst_student = []
    lst_book = []
    lst_loan = []

def save_data():
    fh = open("library.data","wb")
    dump(lst_student,fh)
    dump(lst_book,fh)
    dump(lst_loan,fh)
    fh.close()  





  
  