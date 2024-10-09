class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        return f"'{self.title}' by {self.author} - {'Borrowed' if self.is_borrowed else 'Available'}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and not book.is_borrowed:
                book.is_borrowed = True
                print(f"You have borrowed: {book}")
                return
        print(f"The book '{title}' is either not available or already borrowed.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title and book.is_borrowed:
                book.is_borrowed = False
                print(f"You have returned: {book}")
                return
        print(f"The book '{title}' was not borrowed.")

    def display_books(self):
        print("Available Books in the Library:")
        for book in self.books:
            print(book)


# Example usage
if __name__ == "__main__":
    library = Library()

   # Adding books to the library
    library.add_book(Book("Java", "Scott"))
    library.add_book(Book("Python", "George"))
    library.add_book(Book("Html", "Harper"))

    # Displaying books
    library.display_books()

    # Borrowing a book
    library.borrow_book("1984")
    
    # Displaying books again to see the updated status
    library.display_books()

    # Returning a book
    library.return_book("1984")
    
    # Displaying books again to see the updated status
    library.display_books()