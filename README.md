<p align="center">
  <img src="https://i.imgur.com/9yYi1j6.png" width="100%" alt="Simran E-commerce Backend Banner">
</p>


<p align="center">
A complete, production-grade E-commerce Backend built using  
<b>Django, Django REST Framework, and JWT Authentication</b>.
</p>

<p align="center">
  <!-- Badges -->
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python">
  <img src="https://img.shields.io/badge/Django-REST%20Framework-red?logo=django">
  <img src="https://img.shields.io/badge/JWT-Authentication-green?logo=jsonwebtokens">
  <img src="https://img.shields.io/badge/Status-Production%20Ready-brightgreen">
</p>

---

# 🚀 Overview
This backend provides **secure authentication**, **product management**,  
**shopping cart functionality**, and **order processing**, similar to real ecommerce systems.

It is fully structured, scalable, and follows best REST API practices.

---

# ⭐ Features

## 🔐 Authentication (JWT)
- Register  
- Login  
- Access + Refresh tokens  
- Protected routes  

## 🛍 Product Features
- Product list & detail (slug-based)
- Categories  
- Multiple images  
- Price + discount price  
- Stock tracking  

## 🛒 Cart Features
- Add to cart  
- Auto-create user cart  
- Increase quantity  
- View full cart  
- JWT-secured  

## 📦 Order System
- Convert Cart → Order  
- Total amount calculation  
- Create Order Items  
- Reduce stock automatically  
- Clear cart  
- Order History API  



# 📌 API Endpoints

## 🔐 Authentication

| Method | Endpoint                | Description          |
|--------|--------------------------|----------------------|
| POST   | `/api/auth/register/`   | Register user        |
| POST   | `/api/auth/login/`      | Login + JWT tokens   |

---

## 🛍 Products

| Method | Endpoint                    | Description           |
|--------|------------------------------|-----------------------|
| GET    | `/api/products/`            | List all products     |
| GET    | `/api/products/<slug>/`     | Product detail        |

---

## 🛒 Cart APIs

| Method | Endpoint            | Description             |
|--------|----------------------|-------------------------|
| GET    | `/api/cart/`        | View cart               |
| POST   | `/api/cart/add/`    | Add product to cart     |

### Add to Cart JSON Body:
```json
{
  "product_id": 1,
  "quantity": 2
}

ecommerce-backend/
│── store/               # Project config
│── core/
│    ├── models.py       # DB Models
│    ├── views.py        # API Logic
│    ├── serializers.py  # JSON Conversion
│── manage.py
│── README.md
│── requirements.txt

▶️ Run Project Locally
1️⃣ Clone Repo
git clone https://github.com/<your-username>/ecommerce-backend.git
cd ecommerce-backend

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate

3️⃣ Install Requirements
pip install -r requirements.txt

4️⃣ Migrate Database
python manage.py migrate

5️⃣ Start Server
python manage.py runserver

