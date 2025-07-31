#!/usr/bin/env python3
"""
Create database tables for Restaurant Order and Customer API
"""
import os
import sys

def main():
    """Main function to create database tables"""
    print("🚀 Restaurant Order and Customer - Database Setup")
    print("=" * 50)

    # Check if we should use SQLite for testing
    use_sqlite = "--sqlite" in sys.argv or not os.getenv('DATABASE_URL')

    if use_sqlite:
        print("📝 Using SQLite for development/testing")
        os.environ['DATABASE_URL'] = 'sqlite:///./restaurant.db'

    try:
        # Import after setting environment variable
        from app.database import create_tables, engine
        # Import all model classes so SQLModel can create tables
        from app.models import Customer, Item, Offer, Order, Payment, PaymentMethod, PaymentStatus

        print(f"🔗 Database URL: {os.getenv('DATABASE_URL')}")

        # Test database connection first
        print("🔍 Testing database connection...")
        with engine.connect() as conn:
            print("✅ Database connection successful")

        # Create tables
        print("📋 Creating database tables...")
        create_tables()
        print("✅ Tables created successfully!")

        # List created tables
        from sqlmodel import SQLModel
        tables = list(SQLModel.metadata.tables.keys())
        print(f"� Created {len(tables)} tables: {', '.join(tables)}")

        if use_sqlite and os.path.exists('./restaurant.db'):
            size = os.path.getsize('./restaurant.db')
            print(f"💾 SQLite database file: restaurant.db ({size} bytes)")

    except ImportError as e:
        print(f"❌ Import Error: {e}")
        print("\n💡 Solution: Install required packages:")
        print("   pip install -r requirements.txt")
        sys.exit(1)

    except Exception as e:
        print(f"❌ Error: {e}")
        print(f"❌ Error type: {type(e).__name__}")

        print("\n💡 Troubleshooting:")
        if "postgresql" in str(e).lower() or "psycopg" in str(e).lower():
            print("🐘 PostgreSQL Issues:")
            print("   1. Make sure PostgreSQL server is running")
            print("   2. Create database: CREATE DATABASE restaurant_db;")
            print("   3. Check credentials in .env file")
            print("   4. Or use SQLite: python create_tables.py --sqlite")
        else:
            print("   1. Check your DATABASE_URL in .env file")
            print("   2. Verify database server is running")
            print("   3. Check network connectivity")
            print("   4. Try SQLite mode: python create_tables.py --sqlite")

        sys.exit(1)

if __name__ == "__main__":
    main()