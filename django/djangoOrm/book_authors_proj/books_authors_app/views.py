from django.shortcuts import render, redirect
from .models import Book, Author

def index(request):
    context = {
        "books": Book.objects.all()
    }
    return render(request, "index.html", context)

def book(request, book_id):
    context = {
        "book": Book.objects.get(id=book_id),
        "all_authors": Author.objects.all(),
        "book_description": Book.objects.get(id=book_id).description,
        "authors": Book.objects.get(id=book_id).authors.all()
    }
    return render(request, "book.html", context)

def authors(request):
    context = {
        "authors": Author.objects.all()
    }
    return render(request, "authors.html", context)

def author(request, author_id):
    context = {
        "author": Author.objects.get(id=author_id),
        "all_books": Book.objects.all(),
        "author_notes": Author.objects.get(id=author_id).notes,
        "books": Author.objects.get(id=author_id).books.all()
    }
    return render(request, "author.html", context)

def add_book(request):
    Book.objects.create(title = request.POST['book_title'], description = request.POST['description'])
    return redirect("/")

def add_author(request):
    Author.objects.create(first_name = request.POST['author_first_name'], 
        last_name = request.POST['author_last_name'],
        notes = request.POST['author_notes'])
    return redirect("/authors")

def add_author_to_book(request, book_id):
    author = Author.objects.get(id = request.POST['author_id'])
    book = Book.objects.get(id = book_id)
    book.authors.add(author)
    return redirect(f"/books/{book_id}")

def add_book_to_author(request, author_id):
    book = Book.objects.get(id = request.POST['book_id'])
    author = Author.objects.get(id = author_id)
    author.books.add(book)
    return redirect(f"/authors/{author_id}")