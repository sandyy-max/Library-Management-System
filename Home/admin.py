
# Register your models here.
from django.contrib import admin
from .models import Book, Transaction

admin.site.register(Book)
admin.site.register(Transaction)
