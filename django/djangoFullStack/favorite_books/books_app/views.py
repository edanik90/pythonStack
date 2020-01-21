from django.shortcuts import render, redirect
from login_app.models import *
from django.contrib import messages

def main(request):
    context = {
        "books":Book.objects.all(),
        "user":User.objects.get(id = request.session['user_id'])
    }
    return render(request, "books/main.html", context)

def book_info(request, book_id):
    context = {
        "book":Book.objects.get(id = book_id),
        "users":User.objects.all()
    }
    book = Book.objects.get(id = book_id)
    user = User.objects.get(id = request.session['user_id'])
    if user != book.uploaded_by:
        return render(request, "books/book_info_view.html", context)
    return render(request, "books/book_info_edit.html", context)

def add_new_book(request):
    errors = Book.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/books")
    uploading_user = User.objects.get(id = request.session['user_id'])
    new_book = Book.objects.create(title = request.POST['title'], 
        description = request.POST['description'],
        uploaded_by = uploading_user)
    uploading_user.favorite_books.add(new_book)
    return redirect("/books")

def logout(request):
    request.session.clear()
    return redirect("/")