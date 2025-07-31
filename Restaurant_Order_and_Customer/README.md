# Restaurant Order and Customer API

A FastAPI-based REST API for managing restaurant orders and customers.

## 🚀 Quick Start

### Option 1: Automatic Setup
```bash
python setup.py
```

### Option 2: Manual Setup

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```

2. **Create database tables:**
```bash
# Using SQLite (recommended for development)
python create_tables.py --sqlite

# Or using your configured database
python create_tables.py
```

3. **Run the API:**
```bash
uvicorn main:app --reload
```

## 🗄️ Database Configuration

### SQLite (Default)
No additional setup required. Database file will be created automatically.

### PostgreSQL
1. Install and start PostgreSQL
2. Create database:
```sql
CREATE DATABASE restaurant_db;
```
3. Update `.env` file:
```env
DATABASE_URL=postgresql://username:password@localhost:5432/restaurant_db
```

## 📁 Project Structure

```
Restaurant_Order_and_Customer/
├── main.py                 # FastAPI application
├── create_tables.py        # Database setup script
├── requirements.txt        # Python dependencies
├── .env                   # Environment variables
└── app/
    ├── database.py        # Database configuration
    ├── models/           # Database models
    │   ├── customer_model.py
    │   ├── item_model.py
    │   ├── offer_model.py
    │   ├── order_model.py
    │   └── payment_model.py
    ├── routers/          # API endpoints
    │   ├── customer_router.py
    │   ├── item_router.py
    │   ├── offer_router.py
    │   ├── order_router.py
    │   └── payment_router.py
    ├── schemas/          # Pydantic schemas
    │   ├── customer_schema.py
    │   ├── item_schema.py
    │   ├── offer_schema.py
    │   ├── order_schema.py
    │   └── payment_schema.py
    └── services/         # Business logic
        ├── customer_service.py
        ├── item_service.py
        ├── offer_service.py
        ├── order_service.py
        └── payment_service.py
```

## 🔧 Troubleshooting

### Import Errors
```bash
pip install -r requirements.txt
```

### Database Connection Issues
- **PostgreSQL**: Make sure server is running and database exists
- **SQLite**: Use `python create_tables.py --sqlite`

### Port Already in Use
```bash
uvicorn main:app --reload --port 8001
```

## 📚 API Documentation

Once running, visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
