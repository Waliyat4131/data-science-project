""" This project is book library management system """

books = [["The Hobbit", "J.R.R Tolkien", "Available"],    
         ["Pride and Prejudice", "Jane Austen", "Available"],
         ["1984", "George Onwell","Available"], 
         ["Harry porter and the chamber of secret", "J.K Rowling", "Available"],
         ["Atomic Habits", "James Clear", "Available"]]

# the command its must have == list, add, borrow, return, search, quit

print()


def list(books):
    """this print the books available in the library"""
    print()
    print("Libraray Books")
    print()
    for i, item in enumerate (books):
        title, author, Status = item
        print(f" {i + 1} {title} - {author} - {Status} ")


def prompt_for_book():
    Title = input("Title: ").strip().title()
    Author = input("Author: ").strip().title()
    Status= input("Status: ").strip().title()
    
    return Title, Author, Status




def add_book(book):

    """Ask for the book title and add them to the shelve """
    title, author, status = prompt_for_book()
    book.append((title,author,status))
    print(f"  {title} added to the shelve")




def borrow(book):
    """ Ask if book is available and lend"""
    book_title = input("Enter the book title? ").strip()
    
    for item in books:
        if item[0].lower() ==book_title.lower():
            if item[2] == "Available":
                item[2] ="Borrowed"
                print(f"{book_title} borrowed successfully!.")
            else:
                print("Sorry, this book is already borrowed")
           
            return
    print(f"The book is not available in the library")




def return_book(book):
    """Ask for the book to be returned"""
    book_return_title = input("Enter the book title ").strip()

    for item in books:
        if item[0].lower() == book_return_title.lower():
            if item[2] == "Borrowed":
                item[2] = "Available"
                print(f"{book_return_title} return successfully")
            else: 
                print("This book has not been borrowed")

            return
    print(f"The book  you entered is not correct")


def search_books(books):
    search_title = input("Enter the book title:  ").strip()

    for item in books:
        title, author, status = item
        print(title)
        print(title.lower() == search_title.lower())
        if title.lower() == search_title.lower():
            print(f"Title: {title}")
            print(f"Authour: {author}")
            print(f"Availability: {availability}")
            return
        
    print("Book not found")
            
        
            



def run_app(books):
    print("=" * 44)
    print("Welcome to the Book Haven") 
    print("=" * 44)
    print()
    print("Options: add / borrow / return / search / quit")

    


    is_running = True
    while is_running:

        list(books)
        
        
        command = input(">").strip().lower()
        
        if command == "quit":
            is_running = False
            print("The library is not available. Good night")
        elif command == "add":
           add_book(books)
        elif command == "borrow":
            borrow(books)
            
        elif command == "return":
            return_book(books)

        elif command == "search":
        
            search_books(books)

        else:
            print(f"Sorry, I dont know the command '{command}'")

run_app(books)
