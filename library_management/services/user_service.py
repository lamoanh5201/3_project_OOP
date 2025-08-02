from typing import List, Optional
from library_management.models.user import User
from library_management.models.book import Book

class UserService:
    def __init__(self):
        self.users: List[User] = []

    def register_user(self, user: User) -> bool:
        """Register new user"""
        if self.find_user_by_id(user.id):
            return False
        self.users.append(user)
        return True

    def find_user_by_id(self, user_id: str) -> Optional[User]:
        """Find user by ID"""
        for user in self.users:
            if user.id == user_id:
                return user
        return None

    def get_all_users(self) -> List[User]:
        """Get all users"""
        return self.users.copy()

    def add_borrowed_book(self, user: User, book: Book) -> bool:
        """Add book to user's borrowed books list"""
        if book not in user.borrowed_books:
            user.borrowed_books.append(book)
            return True
        return False

    def remove_borrowed_book(self, user: User, book: Book) -> bool:
        """Remove book from user's borrowed books list"""
        if book in user.borrowed_books:
            user.borrowed_books.remove(book)
            return True
        return False


