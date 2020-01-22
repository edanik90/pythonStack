from django.shortcuts import render
from django.shortcuts import render, redirect
from login_app.models import User
from .models import Review, Book, Author
from django.contrib import messages


def books_home(request):
    context = {
        "reviews":Review.objects.all().order_by("-created_at")[0:3],
        "books_with_reviews":Book.objects.all()
    }
    return render(request, "books_home.html", context)

def page_for_adding(request):
    context = {
        "authors":Author.objects.all()
    }
    return render(request, "add_book.html", context)

def add_book(request):
    book_errors = Book.objects.basic_validator(request.POST)
    review_errors = Review.objects.basic_validator(request.POST)
    author_errors = Author.objects.basic_validator(request.POST)
    if len(book_errors) == 0 and len(review_errors) == 0 and len(author_errors) == 0:
        if request.POST['new_author'] == '':
            new_author = Author.objects.get(id = request.POST['authors_list'])
        else:
            if len(Author.objects.filter(name = request.POST['new_author'])) != 0:
                new_author = Author.objects.get(name = request.POST['new_author'])
            else:
                new_author = Author.objects.create(name = request.POST['new_author'])    
                new_book = Book.objects.create(title = request.POST['title'], author = new_author)
                Review.objects.create(content = request.POST['review'], 
                    rating = request.POST['rating'],
                    user = User.objects.get(id = request.session['user_id']), 
                    book = new_book)
        return redirect(f"/books/{new_book.id}")    
    for key, value in book_errors.items():
        messages.error(request, value)
    for key, value in author_errors.items():
        messages.error(request, value)
    for key, value in review_errors.items():
        messages.error(request, value)
    return redirect("/books/add")


def add_review(request, book_id):
    errors = Review.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f"/books/{book_id}")
    current_user = User.objects.get(id = request.session['user_id'])
    book = Book.objects.get(id = book_id)
    Review.objects.create(content = request.POST['review'], 
        rating = request.POST['rating'],
        user = current_user, book = book)
    return redirect(f"/books/{book_id}")

def delete_review(request, book_id, review_id):
    review = Review.objects.get(id = review_id)
    if review.user.id != request.session['user_id']:
        return redirect(f"/books/{book_id}")
    review.delete()
    return redirect(f"/books/{book_id}")

def user_info(request, user_id):
    context = {
        "user":User.objects.get(id = user_id)
    }
    return render(request, "user_info.html", context)

def book_info(request, book_id):
    context = {
        "book":Book.objects.get(id = book_id)
    }
    return render(request, "book_info.html", context)

def logout(request):
    del request.session['user_id']
    del request.session['first_name']
    del request.session['alias']
    return redirect("/")