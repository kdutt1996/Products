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

1a. Clone the repository:  
   git clone https://github.com/kdutt1996/Products.git
   cd Products
1b. Optionally download the files from git or from the submissions page

2. Create a virtual environment
   python -m venv venv
   source venv/bin/activate        # On macOS/Linux
   venv\Scripts\activate           # On Windows
 
3. pip install -r requirements.txt #install all the dependencies
4. python manage.py migrate
5. python manage.py createsuperuser # to create an admin user or login via username: remarcable pw: admin, from the DB 
6. python manage.py runserver
7. Admin interface: http://127.0.0.1:8000/admin/ (to add categories, tags, and products)
   Search/filter page: http://127.0.0.1:8000/ (users can search and filter products)
