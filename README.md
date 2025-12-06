<<<<<<< HEAD
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
=======
# grocery_django
# 🛒 Online Grocery Store – Django Project

An online grocery shopping web application built using **Django**, where users can browse products, add items to cart, and manage purchases through a simple UI. The system includes complete product management through Django Admin and demonstrates real-world e‑commerce functionalities.

---

## ✨ Features

* 🛍️ Browse grocery products by category
* 🔍 Product detail view with image, description & price
* 🛒 Add to cart, update quantity, remove from cart
* 👤 User authentication (Register, Login, Logout)
* 🧾 Order summary and total calculation
* 🛠️ Admin panel for managing products and images
* 📦 Upload product images using Django Media
* 📱 Responsive UI design

---

## 🛠️ Tech Stack

| Layer           | Technology                |
| --------------- | ------------------------- |
| Backend         | Django, Python            |
| Frontend        | HTML, CSS, Bootstrap      |
| Database        | SQLite3                   |
| Auth            | Django Authentication     |
| Server          | Django Development Server |
| Version Control | Git & GitHub              |

---

## 📂 Project Structure

```plaintext
online_grocery_project/
│ manage.py
│ db.sqlite3
├── grocery/            # Project settings & urls
├── shop/               # Main app (products, cart logic)
├── templates/          # HTML templates
├── static/             # CSS / JS / static assets
└── media/products/     # Uploaded product images
```

---

## 🚀 How to Run the Project

```bash
git clone <your-repository-url>
cd online_grocery_project

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start server
python manage.py runserver
```

Visit: **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

---

## 📦 Requirements File

Create a file named `requirements.txt`:

```
django
djangorestframework
pillow
```

---

## 📸 Screenshots

(Add screenshots of Home Page, Cart, Product Page here)

---

## 🎯 Project Purpose

The goal of this project is to demonstrate a complete **Django-based E‑Commerce workflow** including:

* CRUD operations for product management
* Cart functionality and session handling
* MVC/MVT architecture understanding
* Real‑time image uploads via Django media

This project is great for **students, beginners, and learners** building their first Django e‑commerce app.

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License

This project is open-source and available under the **MIT License**.

---

## 💬 Contact

For any queries, feel free to connect.

**Thank you for checking out this project! 🌟**

>>>>>>> 2cd12e250d96536f1647b85dd88295a47051572b
