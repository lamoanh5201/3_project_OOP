from library_management.models import Book, User
from library_management.services import LibraryService

def main():
    # Initialize library
    library = LibraryService("Central Library")
    
    # Add sample books
    sample_books = [
        Book("B001", "Python Programming", "John Smith", "978-0123456789"),
        Book("B002", "Data Structures", "Jane Doe", "978-0987654321"),
        Book("B003", "Algorithms", "Bob Johnson", "978-0456789123")
    ]
    
    for book in sample_books:
        library.add_book(book)
    
    # Add sample users
    sample_users = [
        User("U001", "Alice Brown", "alice.brown@email.com"),
        User("U002", "Charlie Wilson", "charlie.wilson@email.com")
    ]
    
    for user in sample_users:
        library.register_user(user)
    
    # Test library operations
    print("=== Library Management System ===")
    print(f"Library: {library.name}")
    
    # Display all books
    print("\nAll books:")
    for book in library.get_all_books():
        print(book)
    
    # Display all users
    print("\nAll users:")
    for user in library.get_all_users():
        print(user)
    
    # Test borrowing
    print("\nTesting book borrowing...")
    if library.lend_book("U001", "B001"):
        print("Book borrowed successfully!")
    
    # Display books after borrowing
    print("\nBooks after borrowing:")
    for book in library.get_all_books():
        print(book)

if __name__ == "__main__":
    main()
