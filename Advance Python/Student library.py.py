'''Implement a student library system using oops where students can borrow  a book from list of books
Create a seperate library and student class .
Your programme must be menu driven
You are free to choose methods and attributes of ur choice to implment this functionality'''


class Library :
    def __init__(self,listOfBooks) :
        self.books=listOfBooks
    def displayAvailableBooks(self):
        print("Books present in this library are: ")
        for book in self.books:
            print(" *"+book)

    def borrowBook(self,bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}.Pleasr keep it safe and return it within 30 days")
            self.books.remove(bookName)
            
        else:
            print("sorry, This book has already ben issued to someone else.Pleae wait...")
            
    
    def returnBook(self,bookName):
        self.books.append(bookName)  
        print("thanks for returnig this boook")  

class Student:

    def requestBook(self):
        self.book=input("Enter the name of book u want to borrow: ")
        return self.book

    def returnBook(self):
        self.book=input("Enter the name of book u want to return: ")
        return self.book  

if __name__ == "__main__":
    centraLibrary=Library(["Algorithm","MAchine Learning","Deep Learning","Python"])
    # centraLibrary.displayAvailableBooks()
    student=Student()
    while (True):
        WelcomeMsg=''' **************** Welcome to central Library *************** 
        Please choose an option
        1. Listing all the books
        2. Request a book 
        3. Add or Return the book 
        4. Exit the library
        '''
        print(WelcomeMsg)

        a=int(input("enter a choice:"))
        if a==1:
            centraLibrary.displayAvailableBooks()
        elif a==2:
            centraLibrary.borrowBook(student.requestBook())
        elif a==3: 
            centraLibrary.returnBook(student.returnBook())
        elif a==4:
            print("thanks for using Central Library !Have a great day")
            exit()
        
        


 
