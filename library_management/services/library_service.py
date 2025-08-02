from library_management.services.book_service import BookService
from library_management.services.user_service import UserService

class LibraryService:
    def __init__(self, name: str):
        self.name = name
        self.book_service = BookService()
        self.user_service = UserService()

    # Delegate book operations
    def add_book(self, book):
        return self.book_service.add_book(book)

    def remove_book(self, book_id: str):
        return self.book_service.remove_book(book_id)

    def find_book_by_id(self, book_id: str):
        return self.book_service.find_book_by_id(book_id)

    def search_books_by_title(self, title: str):
        return self.book_service.search_books_by_title(title)

    def search_books_by_author(self, author: str):
        return self.book_service.search_books_by_author(author)

    def get_all_books(self):
        return self.book_service.get_all_books()

    def get_available_books(self):
        return self.book_service.get_available_books()

    def get_borrowed_books(self):
        return self.book_service.get_borrowed_books()

    # Delegate user operations
    def register_user(self, user):
        return self.user_service.register_user(user)

    def find_user_by_id(self, user_id: str):
        return self.user_service.find_user_by_id(user_id)

    def get_all_users(self):
        return self.user_service.get_all_users()

    # Library-specific operations
    def lend_book(self, user_id: str, book_id: str) -> bool:
        """Lend book to user"""
        user = self.find_user_by_id(user_id)
        book = self.find_book_by_id(book_id)
        
        if not user or not book or book.is_borrowed:
            return False
        
        if self.book_service.borrow_book(book, user):
            self.user_service.add_borrowed_book(user, book)
            return True
        return False

    def return_book(self, user_id: str, book_id: str) -> bool:
        """Return book from user"""
        user = self.find_user_by_id(user_id)
        book = self.find_book_by_id(book_id)
        
        if not user or not book or not book.is_borrowed:
            return False
        
        if book.borrowed_by != user:
            return False
        
        if self.book_service.return_book(book):
            self.user_service.remove_borrowed_book(user, book)
            return True
        return False





