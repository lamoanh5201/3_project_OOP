from typing import List, Optional
from datetime import datetime
from library_management.models.book import Book

class BookService:
    def __init__(self):
        self.books: List[Book] = []

    def add_book(self, book: Book) -> bool:
        """Add book to library"""
        if self.find_book_by_id(book.id):
            return False
        self.books.append(book)
        return True

    def remove_book(self, book_id: str) -> bool:
        """Remove book from library"""
        book = self.find_book_by_id(book_id)
        if not book or book.is_borrowed:
            return False
        self.books.remove(book)
        return True

    def find_book_by_id(self, book_id: str) -> Optional[Book]:
        """Find book by ID"""
        for book in self.books:
            if book.id == book_id:
                return book
        return None

    def search_books_by_title(self, title: str) -> List[Book]:
        """Search books by title"""
        return [book for book in self.books if title.lower() in book.title.lower()]

    def search_books_by_author(self, author: str) -> List[Book]:
        """Search books by author"""
        return [book for book in self.books if author.lower() in book.author.lower()]

    def get_all_books(self) -> List[Book]:
        """Get all books"""
        return self.books.copy()

    def get_available_books(self) -> List[Book]:
        """Get available books"""
        return [book for book in self.books if not book.is_borrowed]

    def get_borrowed_books(self) -> List[Book]:
        """Get borrowed books"""
        return [book for book in self.books if book.is_borrowed]

    def borrow_book(self, book: Book, user) -> bool:
        """Mark book as borrowed by user"""
        if book.is_borrowed:
            return False
        
        book.is_borrowed = True
        book.borrowed_by = user
        book.borrowed_date = datetime.now()
        return True

    def return_book(self, book: Book) -> bool:
        """Mark book as returned"""
        if not book.is_borrowed:
            return False
            
        book.is_borrowed = False
        book.borrowed_by = None
        book.borrowed_date = None
        return True


