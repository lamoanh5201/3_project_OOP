# library_cli.py

import argparse
import json
import os

class Library:
    def __init__(self, filepath="library.json"): 
        self.filepath = filepath
        self.data = {"books": [], "users": [], "lending": {}}
        self.load()

    def save(self):
        with open(self.filepath, "w") as f:
            json.dump(self.data, f, indent=4)

    def load(self):
        if os.path.exists(self.filepath):
            with open(self.filepath, "r") as f:
                self.data = json.load(f)

    def add_book(self, book_id, title):
        if book_id in [b["id"] for b in self.data["books"]]:
            print("⚠️ Book already exists.")
        else:
            self.data["books"].append({"id": book_id, "title": title})
            print(f"✅ Book '{title}' added successfully.")

    def register_user(self, name):
        if name in self.data["users"]:
            print("⚠️ User already exists.")
        else:
            self.data["users"].append(name)
            print(f"✅ User '{name}' registered successfully.")

    def lend_book(self, user, book_id):
        if book_id in self.data["lending"]:
            print("❗ Book is already lent out.")
        elif book_id not in [b["id"] for b in self.data["books"]]:
            print("❌ Book does not exist.")
        else:
            self.data["lending"][book_id] = user
            print(f"📚 '{user}' has borrowed book ID '{book_id}'.")

    def return_book(self, user, book_id):
        if self.data["lending"].get(book_id) == user:
            del self.data["lending"][book_id]
            print(f"🔁 '{user}' has returned book ID '{book_id}'.")
        else:
            print("❌ Cannot return the book.")

    def show_lending(self):
        if not self.data["lending"]:
            print("(No books are currently lent out.)")
        else:
            for book_id, user in self.data["lending"].items():
                print(f"• {book_id} → {user}")

def main():
    parser = argparse.ArgumentParser(description="📚 Library Management CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Add book
    add_book = subparsers.add_parser("add-book", help="Add a new book")
    add_book.add_argument("--id", required=True, help="Book ID")
    add_book.add_argument("--title", required=True, help="Book title")

    # Register user
    register_user = subparsers.add_parser("register-user", help="Register a new user")
    register_user.add_argument("--name", required=True, help="User name")

    # Lend book
    lend_book = subparsers.add_parser("lend-book", help="Lend a book")
    lend_book.add_argument("--user", required=True)
    lend_book.add_argument("--book-id", required=True)

    # Return book
    return_book = subparsers.add_parser("return-book", help="Return a book")
    return_book.add_argument("--user", required=True)
    return_book.add_argument("--book-id", required=True)

    # Show lending status
    subparsers.add_parser("show-lending", help="Show list of lent books")

    args = parser.parse_args()
    lib = Library()

    if args.command == "add-book":
        lib.add_book(args.id, args.title)

    elif args.command == "register-user":
        lib.register_user(args.name)

    elif args.command == "lend-book":
        lib.lend_book(args.user, args.book_id)

    elif args.command == "return-book":
        lib.return_book(args.user, args.book_id)

    elif args.command == "show-lending":
        lib.show_lending()

    else:
        parser.print_help()
        return

    lib.save()

if __name__ == "__main__":
    main()
