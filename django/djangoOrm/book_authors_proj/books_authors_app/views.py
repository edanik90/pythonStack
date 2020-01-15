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
