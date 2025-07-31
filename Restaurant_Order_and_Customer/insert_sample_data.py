#!/usr/bin/env python3
"""
Insert sample data into Restaurant Order and Customer database
"""
import requests
import json
from datetime import datetime, timedelta

# API base URL
BASE_URL = "http://localhost:8000/api/v1"

def check_api_connection():
    """Check if API is running"""
    try:
        response = requests.get("http://localhost:8000/health")
        if response.status_code == 200:
            print("✅ API is running")
            return True
        else:
            print("❌ API is not responding properly")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to API. Make sure the server is running:")
        print("   uvicorn main:app --reload")
        return False

def create_customers():
    """Create sample customers"""
    print("\n👥 Creating sample customers...")
    
    customers = [
        {
            "name": "Nguyễn Văn A",
            "email": "nguyenvana@example.com",
            "phone": "0123456789",
            "address": "123 Đường Lê Lợi, Quận 1, TP.HCM"
        },
        {
            "name": "Trần Thị B",
            "email": "tranthib@example.com",
            "phone": "0987654321",
            "address": "456 Đường Nguyễn Huệ, Quận 1, TP.HCM"
        },
        {
            "name": "Lê Văn C",
            "email": "levanc@example.com",
            "phone": "0369852147",
            "address": "789 Đường Hai Bà Trưng, Quận 3, TP.HCM"
        },
        {
            "name": "Phạm Thị D",
            "email": "phamthid@example.com",
            "phone": "0147258369",
            "address": "321 Đường Cách Mạng Tháng 8, Quận 10, TP.HCM"
        }
    ]
    
    created_customers = []
    for customer in customers:
        try:
            response = requests.post(f"{BASE_URL}/customers", json=customer)
            if response.status_code == 200:
                created_customer = response.json()
                created_customers.append(created_customer)
                print(f"✅ Created customer: {customer['name']} (ID: {created_customer['id']})")
            else:
                print(f"❌ Failed to create customer {customer['name']}: {response.text}")
        except Exception as e:
            print(f"❌ Error creating customer {customer['name']}: {e}")
    
    return created_customers

def create_items():
    """Create sample menu items"""
    print("\n🍽️ Creating sample menu items...")
    
    items = [
        {
            "name": "Phở Bò",
            "description": "Phở bò truyền thống với nước dùng đậm đà",
            "price": 65000,
            "category": "Món chính",
            "is_available": True
        },
        {
            "name": "Bún Bò Huế",
            "description": "Bún bò Huế cay nồng đặc trưng miền Trung",
            "price": 70000,
            "category": "Món chính",
            "is_available": True
        },
        {
            "name": "Cơm Tấm",
            "description": "Cơm tấm sườn nướng, chả, bì",
            "price": 55000,
            "category": "Món chính",
            "is_available": True
        },
        {
            "name": "Gỏi Cuốn",
            "description": "Gỏi cuốn tôm thịt tươi ngon",
            "price": 35000,
            "category": "Khai vị",
            "is_available": True
        },
        {
            "name": "Chả Cá Lã Vọng",
            "description": "Chả cá Lã Vọng truyền thống Hà Nội",
            "price": 85000,
            "category": "Món chính",
            "is_available": True
        },
        {
            "name": "Trà Đá",
            "description": "Trà đá truyền thống",
            "price": 5000,
            "category": "Đồ uống",
            "is_available": True
        },
        {
            "name": "Nước Mía",
            "description": "Nước mía tươi mát",
            "price": 15000,
            "category": "Đồ uống",
            "is_available": True
        },
        {
            "name": "Chè Ba Màu",
            "description": "Chè ba màu truyền thống",
            "price": 25000,
            "category": "Tráng miệng",
            "is_available": True
        }
    ]
    
    created_items = []
    for item in items:
        try:
            response = requests.post(f"{BASE_URL}/items", json=item)
            if response.status_code == 200:
                created_item = response.json()
                created_items.append(created_item)
                print(f"✅ Created item: {item['name']} - {item['price']:,}đ (ID: {created_item['id']})")
            else:
                print(f"❌ Failed to create item {item['name']}: {response.text}")
        except Exception as e:
            print(f"❌ Error creating item {item['name']}: {e}")
    
    return created_items

def create_offers():
    """Create sample offers"""
    print("\n🎁 Creating sample offers...")
    
    # Calculate dates
    now = datetime.now()
    start_date = now.strftime("%Y-%m-%dT%H:%M:%S")
    end_date = (now + timedelta(days=30)).strftime("%Y-%m-%dT%H:%M:%S")
    
    offers = [
        {
            "name": "Giảm giá 20% cho khách hàng mới",
            "description": "Ưu đãi đặc biệt cho khách hàng lần đầu đến quán",
            "discount_percentage": 20.0,
            "start_date": start_date,
            "end_date": end_date,
            "is_active": True
        },
        {
            "name": "Combo Phở + Trà đá",
            "description": "Giảm 15% khi gọi combo Phở + Trà đá",
            "discount_percentage": 15.0,
            "start_date": start_date,
            "end_date": end_date,
            "is_active": True
        },
        {
            "name": "Happy Hour",
            "description": "Giảm 10% từ 14h-16h hàng ngày",
            "discount_percentage": 10.0,
            "start_date": start_date,
            "end_date": end_date,
            "is_active": True
        }
    ]
    
    created_offers = []
    for offer in offers:
        try:
            response = requests.post(f"{BASE_URL}/offers", json=offer)
            if response.status_code == 200:
                created_offer = response.json()
                created_offers.append(created_offer)
                print(f"✅ Created offer: {offer['name']} - {offer['discount_percentage']}% (ID: {created_offer['id']})")
            else:
                print(f"❌ Failed to create offer {offer['name']}: {response.text}")
        except Exception as e:
            print(f"❌ Error creating offer {offer['name']}: {e}")
    
    return created_offers

def main():
    """Main function"""
    print("🚀 Restaurant Order and Customer - Sample Data Insertion")
    print("=" * 60)
    
    # Check API connection
    if not check_api_connection():
        return
    
    # Create sample data
    customers = create_customers()
    items = create_items()
    offers = create_offers()
    
    print("\n" + "=" * 60)
    print("📊 Summary:")
    print(f"✅ Created {len(customers)} customers")
    print(f"✅ Created {len(items)} menu items")
    print(f"✅ Created {len(offers)} offers")
    
    print(f"\n🌐 You can now view the data at:")
    print(f"   • Swagger UI: http://localhost:8000/docs")
    print(f"   • API Root: http://localhost:8000/")
    
    print(f"\n💡 Next steps:")
    print(f"   • Create orders using customer and item IDs")
    print(f"   • Create payments for orders")
    print(f"   • Test the API endpoints")

if __name__ == "__main__":
    main()
