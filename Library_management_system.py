class Library:
    def __init__(self, listofbooks):
        self.books=listofbooks

    def displayAvailablebooks(self):
        print("Books present in this Library are: ")
        for i,book in enumerate(self.books):
            print(i+1,book)
    
    def borrowBook(self,bookName):
        if bookName in self.books:
            print(f'You have been issued {bookName} book. Please keep it safe and return it after 30 days.')
            self.books.remove(bookName)
            return True
        else:
            print(f'Book is already issued to someone else. Please wait until the book is returned.')
            return False
    
    def returnBook(self,returnbook):
        self.books.append(returnbook)
        print(f'Your book named {returnbook} is successfully returned.')

class Student:
    def reqbook(self):
        self.book=input("Enter name of book you want to borrow: ")
        return self.book
    def returnbook(self):
        self.book=input("Enter name of book you want to return: ")
        return self.book


central_Library=Library(["Python","Data Science","Machine Learning","Deep Learning","Data Analysis"])
student=Student()
while True:
    print('''
     ===============Welcome to the Central Library=============
    Please choose an option--
    1. Listing all the books
    2. Issue a book
    3. Return a Book
    4. Exit Library
    ''')
    a=int(input("Enter your choice: "))
    if a==1:
        central_Library.displayAvailablebooks()
    elif a==2:
        central_Library.borrowBook(student.reqbook())
    elif a==3:
        central_Library.returnBook(student.returnbook())
    elif a==4:
        print("Thanks for using the Library.Do visit us again!")
        break
    else:
        print("Invalid choice")
