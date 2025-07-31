from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.database import create_tables
from app.routers import customer_router, item_router, offer_router, order_router, payment_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("🚀 Starting Restaurant Order and Customer API...")
    try:
        create_tables()
        print("✅ Database tables created/verified")
    except Exception as e:
        print(f"⚠️  Database setup warning: {e}")

    yield

    # Shutdown
    print("🛑 Shutting down Restaurant Order and Customer API...")

app = FastAPI(
    title="Restaurant Order and Customer API",
    version="1.0.0",
    description="A comprehensive API for managing restaurant orders, customers, items, offers, and payments",
    lifespan=lifespan
)

# Include routers
app.include_router(customer_router.router, prefix="/api/v1/customers", tags=["customers"])
app.include_router(item_router.router, prefix="/api/v1/items", tags=["items"])
app.include_router(offer_router.router, prefix="/api/v1/offers", tags=["offers"])
app.include_router(order_router.router, prefix="/api/v1/orders", tags=["orders"])
app.include_router(payment_router.router, prefix="/api/v1/payments", tags=["payments"])

@app.get("/", tags=["root"])
def read_root():
    """Root endpoint - API health check"""
    return {
        "message": "Restaurant Order and Customer API",
        "status": "running",
        "version": "1.0.0",
        "docs": "/docs",
        "redoc": "/redoc"
    }

@app.get("/health", tags=["health"])
def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}