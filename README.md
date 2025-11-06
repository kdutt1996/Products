# Products
Mini Django project that lets the user search products based on descriptions and filters

## Features

- Search products by text input (description).
- Filter by category drop-down.
- Filter by multiple tags (multi-select).
- Combine search + category + tags in one query.
- Admin interface for managing categories, tags, and products.

## Tech Stack

- Python 3.x  
- Django
- SQLite 
- HTML + Django Templates  

## Setup Instructions

1. Clone the repository:  
   ```bash
   git clone https://github.com/yourusername/yourrepo.git
   cd yourrepo

2. python -m venv venv
   source venv/bin/activate        # On macOS/Linux
   venv\Scripts\activate           # On Windows
 
3. pip install -r requirements.txt
4. python manage.py migrate
5. python manage.py createsuperuser # to create an admin user. 
6. python manage.py runserver
7. Admin interface: http://127.0.0.1:8000/admin/ (to add categories, tags, and products)
   Search/filter page: http://127.0.0.1:8000/ (users can search and filter products)
