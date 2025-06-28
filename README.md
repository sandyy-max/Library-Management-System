# Library Management System

A Django-based web application for managing library resources, books, and user borrowing activities.

## Features

- User registration, login, and authentication
- Admin dashboard for managing users, books, and transactions
- Add, edit, and delete books
- Borrow and return books with transaction tracking
- View borrowing history per user
- Filter and search books by title, author, or genre

## Folder Structure

The main app is `Home`, which contains:
- `models.py`: Database models for books and transactions
- `views.py`: Core logic and view functions
- `urls.py`: URL routing for the app
- `templates/`: HTML templates for rendering pages
- `admin.py`: Django admin site configuration

## Getting Started

### Prerequisites

- Python 3.x
- Django (install with `pip install django`)

### Setup

1. **Clone the repository**
    ```bash
    git clone https://github.com/sandyy-max/Library-Management-System.git
    cd Library-Management-System
    ```

2. **Install dependencies**
    ```bash
    pip install django
    ```

3. **Apply migrations**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4. **Create a superuser (for admin access)**
    ```bash
    python manage.py createsuperuser
    ```

5. **Run the server**
    ```bash
    python manage.py runserver
    ```

6. **Visit in browser**
    - User interface: [http://localhost:8000/books/](http://localhost:8000/books/)
    - Admin dashboard: [http://localhost:8000/admin-dashboard/](http://localhost:8000/admin-dashboard/)
    - Django admin: [http://localhost:8000/admin/](http://localhost:8000/admin/)

## Usage

- Register as a new user or login if you already have an account.
- Browse available books, borrow and return books.
- View your borrowing history.
- Admin users can add/edit/delete books and manage users.

## Possible Improvements

- Add book cover images and more metadata
- Email notifications for due dates and reminders
- Fine calculation for late returns
- REST API endpoints for integration

## License

This project is open source and available under the [MIT License](LICENSE).

---

*For any questions or feedback, please open an issue or pull request.*
