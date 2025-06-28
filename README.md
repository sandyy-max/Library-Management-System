
# 📚 Library Management System

A Django-based web application designed to manage library resources with user authentication, book catalog, and issue/return features.

---

## 🚀 Features

- ✅ User Registration & Login
- 📖 View Book Catalog
- 📦 Book Issue & Return Functionality
- 🔐 Role-based Dashboards (User/Admin)
- 🎨 Responsive UI with Pastel and White Theme

---

## 🛠️ Technologies Used

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: SQLite3
- **Authentication**: Django User Model

---

## 📂 Project Structure

```
Library-Management-System/
├── Home/
│   ├── migrations/
│   ├── static/
│   │   ├── css/
│   │   └── js/
│   ├── templates/
│   │   ├── login.html
│   │   ├── signup.html
│   │   └── dashboard.html
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── LibraryManagementSystem/
│   ├── settings.py
│   └── urls.py
├── db.sqlite3
├── manage.py
└── README.md
```

---

## 👤 User Roles

- **Admin**: Add/Edit/Delete Books, Manage Users, View Logs
- **User**: View Books, Issue/Return Books

---

## 🔐 Authentication Flow

1. Register at `/signup/`
2. Login at `/login/`
3. Redirected to a user or admin dashboard

---

## 🧩 Models Overview

```python
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    quantity = models.IntegerField()
```

```python
class Issue(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    issue_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
```

---

## 🖼️ Screenshots

> Add screenshots in a folder called `/screenshots` and display them like:

```md
![Login Page](screenshots/login.png)
![Dashboard](screenshots/dashboard.png)
```

---

## 🛠️ Setup Instructions

```bash
git clone https://github.com/sandyy-max/Library-Management-System.git
cd Library-Management-System
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---

## 🌱 Future Enhancements

- 🔎 Search/Sort Books
- 📧 Email Notifications for Due Books
- 👤 User Profile Pages
- 📊 Admin Dashboard Analytics

---

## 📄 License

Licensed under the MIT License.

---

> Created with ❤️ by Sandhya
