# 🔧 Curl Commands để tạo records

## 👥 Tạo Customers

```bash
# Tạo customer 1
curl -X POST "http://localhost:8000/api/v1/customers" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Nguyễn Văn A",
    "email": "nguyenvana@example.com",
    "phone": "0123456789",
    "address": "123 Đường Lê Lợi, Quận 1, TP.HCM"
  }'

# Tạo customer 2
curl -X POST "http://localhost:8000/api/v1/customers" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Trần Thị B",
    "email": "tranthib@example.com",
    "phone": "0987654321",
    "address": "456 Đường Nguyễn Huệ, Quận 1, TP.HCM"
  }'
```

## 🍽️ Tạo Menu Items

```bash
# Tạo Phở Bò
curl -X POST "http://localhost:8000/api/v1/items" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Phở Bò",
    "description": "Phở bò truyền thống với nước dùng đậm đà",
    "price": 65000,
    "category": "Món chính",
    "is_available": true
  }'

# Tạo Bún Bò Huế
curl -X POST "http://localhost:8000/api/v1/items" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Bún Bò Huế",
    "description": "Bún bò Huế cay nồng đặc trưng miền Trung",
    "price": 70000,
    "category": "Món chính",
    "is_available": true
  }'

# Tạo Trà Đá
curl -X POST "http://localhost:8000/api/v1/items" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Trà Đá",
    "description": "Trà đá truyền thống",
    "price": 5000,
    "category": "Đồ uống",
    "is_available": true
  }'
```

## 🎁 Tạo Offers

```bash
# Tạo offer giảm giá 20%
curl -X POST "http://localhost:8000/api/v1/offers" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Giảm giá 20% cho khách hàng mới",
    "description": "Ưu đãi đặc biệt cho khách hàng lần đầu đến quán",
    "discount_percentage": 20.0,
    "start_date": "2024-01-01T00:00:00",
    "end_date": "2024-12-31T23:59:59",
    "is_active": true
  }'
```

## 📋 Tạo Orders (cần customer_id từ customers đã tạo)

```bash
# Tạo order (thay customer_id = 1 bằng ID thực tế)
curl -X POST "http://localhost:8000/api/v1/orders" \
  -H "Content-Type: application/json" \
  -d '{
    "customer_id": 1,
    "total_amount": 70000,
    "status": "pending",
    "notes": "Không hành"
  }'
```

## 💳 Tạo Payments (cần order_id từ orders đã tạo)

```bash
# Tạo payment (thay order_id = 1 bằng ID thực tế)
curl -X POST "http://localhost:8000/api/v1/payments" \
  -H "Content-Type: application/json" \
  -d '{
    "order_id": 1,
    "amount": 70000,
    "method": "cash",
    "status": "completed",
    "transaction_id": "TXN001"
  }'
```

## 📊 Lấy dữ liệu (GET requests)

```bash
# Lấy tất cả customers
curl -X GET "http://localhost:8000/api/v1/customers"

# Lấy tất cả items
curl -X GET "http://localhost:8000/api/v1/items"

# Lấy items theo category
curl -X GET "http://localhost:8000/api/v1/items/category/Món chính"

# Lấy tất cả orders
curl -X GET "http://localhost:8000/api/v1/orders"

# Lấy offers đang active
curl -X GET "http://localhost:8000/api/v1/offers/active/list"

# Lấy tất cả payments
curl -X GET "http://localhost:8000/api/v1/payments"
```
