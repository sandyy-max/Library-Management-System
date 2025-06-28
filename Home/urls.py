from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('borrow/<int:book_id>/', views.borrow_book, name='borrow_book'),
    path('return/<int:transaction_id>/', views.return_book, name='return_book'),
    path('history/', views.borrowing_history, name='borrowing_history'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
]
