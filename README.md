# Online Grocery Shopping System - Django (Starter)

This is a starter Django project for an **Online Grocery Shopping System**.
Features:
- User registration, login, logout (Django auth)
- Browse products by category
- Search products
- Add to cart (session-backed), update/remove quantity
- Place orders (simple order model)
- Admin site to manage products/categories/orders

Frontend uses **Tailwind CSS via CDN** for quick styling (no npm required).

## Quick start

1. Create venv and install:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. Run migrations and start server:
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

3. Open http://127.0.0.1:8000/

This is a starter scaffold — extend it with payment integration, order tracking, PDF invoice, and more.
