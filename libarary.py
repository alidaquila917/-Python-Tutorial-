class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def checkout(self):
        if self.available:
            self.available = False
            print(f"The book '{self.title}' by {self.author} has been checked out.")
        else:
            print(f"The book '{self.title}' is not available.")

    def return_book(self):
        if not self.available:
            self.available = True
            print(f"The book '{self.title}' by {self.author} has been returned.")
        else:
            print(f"The book '{self.title}' is already available.")

class LibraryCatalogue:
    def __init__(self):
        self.catalogue = []

    def add_book(self, book):
        self.catalogue.append(book)
        print(f"Added the book '{book.title}' by {book.author} to the catalogue.")

    def display_catalogue(self):
        print("Library Catalogue:")
        for book in self.catalogue:
            print(f"Title: {book.title}, Author: {book.author}, Available: {book.available}")

# Test the LibraryCatalogue System
library = LibraryCatalogue()

# Adding books to the catalogue
book1 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
library.add_book(book1)
library.add_book(book2)

# Displaying the catalogue
library.display_catalogue()

# Checking out and returning books
book1.checkout()
book2.checkout()
book1.return_book()
book2.return_book()

# Displaying the updated catalogue
library.display_catalogue()
