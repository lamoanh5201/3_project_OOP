# 2. Intermediate: Library Management System
# Goal: Build a functional CLI app using multiple classes.
# Key OOP Concepts: Inheritance, composition, collections
# What to build:
# Classes: Book, User, Library
# Library manages lists of books and users, with methods like:
# add_book(), remove_book()
# register_user()
# lend_book(user, book)
# return_book(user, book)
# Use composition: Library has Books and Users.
# Add search features (e.g. by title or author), and track who’s borrowed what.
# Drawing on existing repo examples like MostafaAhmed98’s “Library Management” repo 
class Book:
    def __init__(self, book_name, book_id):
        self.book_name = book_name
        self.book_id = book_id
class User:
    def __init__(self, user_name):
        self.user_name = user_name
class Library:
    def __init__(self, inventory, list_user, lending):
        self.inventory = inventory if inventory else []     
        self.list_user = list_user if list_user else []     
        self.lending = lending if lending else {} 
    def add_book(self, book):
        self.inventory.append(book.book_id)
        print(f"Sucessfully add book: {book.book_name}")
    def remove_book(self, book):
        if book.book_id in self.inventory:
            self.inventory.remove(book.book_id)
            print(f"Removed:{book.book_name}")
        else:
            print("Có sách đâu mà xóa")
    def register_user(self, user):
        self.list_user.append(user.user_name)
        print(f"Sucessfully register user: {user.user_name}")
    def lend_book(self, user, book):
        if book.book_id in self.lending:
            print("This book was previously lent.")
        else:
            self.lending[book.book_id] = user.user_name
            return self.lending
    def return_book(self, user, book):
        if book.book_id in self.lending and self.lending[book.book_id] == user.user_name:
            del self.lending[book.book_id]
            print(f"{book.book_name} returned by {user.user_name}.")
        else:
            print(f"Return failed: Either book not lent or wrong user.")