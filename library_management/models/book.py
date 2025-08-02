from datetime import datetime
from typing import Optional

class Book:
    def __init__(self, id: str, title: str, author: str, isbn: str):
        self.id = id
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False
        self.borrowed_by = None
        self.borrowed_date = None

    def __str__(self):
        status = "Đã mượn" if self.is_borrowed else "Có sẵn"
        return f"[{self.id}] {self.title} - {self.author} ({status})"

    def __repr__(self):
        return f"Book(id='{self.id}', title='{self.title}', author='{self.author}')"




