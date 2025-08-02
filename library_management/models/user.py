from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from library_management.models.book import Book

class User:
    def __init__(self, id: str, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email
        self.borrowed_books: List['Book'] = []

    def get_borrowed_count(self) -> int:
        """Get number of borrowed books"""
        return len(self.borrowed_books)

    def __str__(self):
        return f"[{self.id}] {self.name} - {self.email}"

    def __repr__(self):
        return f"User(id='{self.id}', name='{self.name}', email='{self.email}')"







