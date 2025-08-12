**📦 Inventory Management System**

A full-featured Inventory Management System built with Django and Django REST Framework.
It includes an API for CRUD operations on products, categories, suppliers, customers, purchase & sales orders, and a web-based Sales Report page with AJAX-powered filtering.

**🚀 Live Demo**

API Root: https://inventory-management-system-production-10fa.up.railway.app/api/

Sales Report Page: https://inventory-management-system-production-10fa.up.railway.app/sales_report/

**✨ Features**
**🔹 Backend (Django REST Framework)**

Category, Product, Supplier, and Customer management
Purchase Order & Purchase Item tracking
Sales Order & Sales Item tracking
Stock updates with transaction.atomic() to prevent inconsistencies
Aggregated sales data API endpoint

**🔹 Frontend (Django Template + AJAX)**

Sales Report page with date range filters
Fetch data via AJAX without reloading
Display total quantity and revenue dynamically

## 📂 API Endpoints

| Resource           | Endpoint                  |
|--------------------|---------------------------|
| **API Root**       | `/api/`                   |
| Categories         | `/api/categories/`        |
| Products           | `/api/products/`          |
| Suppliers          | `/api/suppliers/`         |
| Customers          | `/api/customers/`         |
| Purchase Orders    | `/api/purchase-orders/`   |
| Purchase Items     | `/api/purchase-items/`    |
| Sales Orders       | `/api/sales-orders/`      |
| Sales Items        | `/api/sales-items/`       |
| Sales Report API   | `/api/sales-report/`      |


**💻 Tech Stack**

Backend: Django, Django REST Framework
Frontend: Django Templates, Bootstrap, jQuery (AJAX)
Database: SQLite (can be switched to PostgreSQL/MySQL)
Deployment: Railway, Gunicorn

**⚙️ Installation (Local Setup)**

**Clone the repository**
git clone https://github.com/Alii0319/Inventory-management-system.git
cd Inventory-management-system

**Create a virtual environment**
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

**Install dependencies**
pip install -r requirements.txt


**Run migrations**
python manage.py migrate

**Create superuser**
python manage.py createsuperuser

**Start development server**
python manage.py runserver

**📊 Sales Report AJAX Workflow**

User selects a start date and end date
AJAX request is sent to /api/sales-report/
Server returns total sales quantity and revenue
Table updates without page reload
