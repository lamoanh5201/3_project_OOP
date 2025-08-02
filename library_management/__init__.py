"""
Library Management System
Organized with Models and Services architecture
"""

from .models import Book, User
from .services import LibraryService

__version__ = "1.0.0"
__all__ = ['Book', 'User', 'LibraryService']

