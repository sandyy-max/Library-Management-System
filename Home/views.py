from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.utils import timezone
from .models import Book, Transaction
from django.contrib.auth.models import User
from django.db.models import Q

# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render (request,'books.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        



    return render (request,'signup.html')


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Username or Password is incorrect.")
            return redirect('login')  # or render to login page directly

    return render(request, 'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')
login_required
def book_list(request):
    books = Book.objects.all()
    query = request.GET.get('q')
    if query:
        books = books.filter(
            Q(title__icontains=query) |
            Q(author__icontains=query) |
            Q(genre__icontains=query)
        )
    return render(request, 'books.html', {'books': books})
@login_required
def borrow_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if book.available:
        book.available = False
        book.save()
        Transaction.objects.create(user=request.user, book=book)
        messages.success(request, f"You borrowed '{book.title}'.")
    else:
        messages.warning(request, f"'{book.title}' is not available.")
    return redirect('book_list')

@login_required
def return_book(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id, user=request.user, returned_at__isnull=True)
    transaction.returned_at = timezone.now()
    transaction.book.available = True
    transaction.book.save()
    transaction.save()
    messages.success(request, f"You returned '{transaction.book.title}'.")
    return redirect('borrowing_history')

@login_required
def borrowing_history(request):
    transactions = Transaction.objects.filter(user=request.user).order_by('-borrowed_at')
    return render(request, 'history.html', {'transactions': transactions})

def is_admin(user):
    return user.is_superuser

@user_passes_test(is_admin)
def admin_dashboard(request):
    users = User.objects.all()
    books = Book.objects.all()
    transactions = Transaction.objects.all().order_by('-borrowed_at')
    return render(request, 'admin_dashboard.html', {
        'users': users,
        'books': books,
        'transactions': transactions
    })
