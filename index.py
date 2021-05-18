# This a library managment system 
# In This Library Managment System will return ,lend , borrow books
# Also data will be added in a seperate file 

# First I will discuss the logic of the code I'll write below
# Here we will make a class library that will take two arguments the booklist and name
# of the library
# Further we will make few methods 
# First method to show books available in the library
# Second method to borrow book 
# Third method to add book in library
# Fourth method to return book
# Data of each action performed will be stored in the book_data.txt file in the same folder 
# Also using datetime module we will report the user the date by which he/she must return
# the book


# Importing datetime module and further methods of the module which we will use furthee
from datetime import datetime
from datetime import timedelta
from datetime import date

# today = date.today()
# print(today)
# today2 = (today+ timedelta(days=7)).isoformat()  
# print(today2)

class Library:

    def __init__(self,list,library_name):
        self.BookList = list
        self.name = library_name
        self.borrowed_books = {}
        print(f"|| Welcome to {self.name} ||")

    def displayBooks(self):
        print("The following are the books available in our library")
        for books in self.BookList:
            print(books)
        

    def borrowBooks(self,user,book):
        if book not in self.borrowed_books.keys():
            self.borrowed_books.update({book:user})
            today = date.today()
            seven_days_after_today = (today + timedelta(days=7)).isoformat()
            print(f"Thank You {user} for borrowing book from {self.name}")
            print(f"You have borrowed book on {today} Make Sure you return the book by {seven_days_after_today}")

            with open('book_data.txt',"a") as f:
                f.write(f"{user} borrowed {book} on {today} \n")
        else:
            print(f"The book {book} is already being used by {self.borrowed_books[book]}")
    
    def addBooks(self,user,book):
        self.BookList.append(book)
        today = date.today()
        print(f"Thank you {user} for adding the book {book} in our library")
        with open('book_data.txt',"a") as f:
                f.write(f"{user} added {book} in library on {today} \n")
        
        

    def returnBooks(self,user,book):
        self.borrowed_books.pop(book)
        today = date.today()
        print(f"Thank you {user} for returning {book} to our library")
        with open('book_data.txt',"a") as f:
                f.write(f"{user} returned {book} in library on {today} \n")


if __name__ == "__main__":
    # Creating the object of the Library
    list_of_books = ['Python','Cingage','Arihant','machine Learning',"Data Science" , "Mathematics"]
    TB_Library = Library(list_of_books,'TB Library')


    while True:
        TB_Library.displayBooks()
        user_name = input("Please Type your name \n")
        print("Please Enter the input as prescribed below to perform the actions according to the keys")
        print("press 1 to borrow books")
        print("press 2 to add books")
        print("press 3 to return books")
        user_choice = int(input())

        if user_choice == 1:
            print('Please type name of the book you want to borrow as prescribed in the list')
            user_choice_book = input()
            TB_Library.borrowBooks(user_name,user_choice_book)


        elif user_choice == 2:
            print('Please type name of the book you want to add')
            user_choice_book2 = input()
            TB_Library.addBooks(user_name,user_choice_book2)
        
        elif user_choice == 3:
            print('Please type name of the book you want to return')
            user_choice_book3 = input()
            TB_Library.returnBooks(user_name,user_choice_book3)

        else:
            print("Invalid input")
        
        print("Press q to quit and c to continue")
        user_choice_12 = input()
        while user_choice_12 != 'q' and user_choice_12 != 'c':
            
            if user_choice_12 == 'q':
                exit()
            elif user_choice_12 == 'c':
                continue
        