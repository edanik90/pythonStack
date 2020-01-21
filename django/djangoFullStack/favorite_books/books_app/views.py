from django.shortcuts import render, redirect
from login_app.models import *
from django.contrib import messages

def main(request):
    context = {
        "books":Book.objects.all(),
        "user":User.objects.get(id = request.session['user_id'])
    }
    return render(request, "books/main.html", context)

def my_favorite_books(request):
    context = {
        "books":User.objects.get(id = request.session['user_id']).favorite_books.all()
    }
    return render(request, "books/favorite_books.html", context)

def book_info(request, book_id):
    context = {
        "book":Book.objects.get(id = book_id),
        "users":User.objects.all(),
        "user":User.objects.get(id = request.session['user_id'])
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

def edit_book(request, book_id):
    book = Book.objects.get(id = book_id)
    if "update" in request.POST:
        book.title = request.POST['title']
        book.description = request.POST['description']
        book.save()
        return redirect(f"/books/{book_id}")
    if "delete" in request.POST:
        book.delete()
        return redirect("/books")

def add_to_favorite(request, book_id):
    book = Book.objects.get(id = book_id)
    user = User.objects.get(id = request.session['user_id'])
    user.favorite_books.add(book)
    return redirect(f"/books/{book_id}")

def unfavorite(request, book_id):
    book = Book.objects.get(id = book_id)
    user = User.objects.get(id = request.session['user_id'])
    user.favorite_books.remove(book)
    return redirect(f"/books/{book_id}")

def logout(request):
    request.session.clear()
    return redirect("/")