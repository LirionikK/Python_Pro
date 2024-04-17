import re


class Book:
    def __init__(self, title, author, isbn, copies=0, total_copies=0):
        self.title = title
        self.author = author
        self.isbn = isbn
        self._copies = copies
        self._total_copies = total_copies

    def check_availability(self):
        return self._copies > 0

    def update_total_copies(self, new_total):
        self._total_copies = new_total

    def update_copies_count(self, new_count):
        self._copies = new_count

    @staticmethod
    def validate_isbn(isbn_code):
        check = r'ISBN [0-9]-[0-9][0-9][0-9]-[0-9]+-[0-9]'
        return bool(re.match(check, isbn_code))

    @property
    def get_total_copies(self):
        return self._total_copies

    @property
    def copies(self):
        return self._copies


class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id


class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def register_user(self, user):
        self.users.append(user)

    def find_book_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def show_availability_books(self):
        available_books  = [book for book in self.books if book.check_availability()]
        return available_books

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)


class Customer(User):
    def __init__(self, name, user_id, library):
        super().__init__(name, user_id)
        self._borrowed_books = []
        self.library = library

    def borrow_book(self, book):
        if book.check_availability():
            self._borrowed_books.append(book)

    def return_book(self, book):
        if book in self._borrowed_books:
            self._borrowed_books.remove(book)


class Employee(User):
    def __init__(self, name, user_id, salary, library):
        super().__init__(name, user_id)
        self.salary = salary
        self.library = library

    @staticmethod
    def add_book_to_library(book, library):
        library.add_book(book)

    @staticmethod
    def remove_book_from_library(book, library):
        library.remove_book(book)
