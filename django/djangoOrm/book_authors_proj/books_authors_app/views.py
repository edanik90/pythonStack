from django.shortcuts import render, redirect
from .models import Book

def index(request):
    context = {
        "all_books": Book.objects.all()
    }
    return render(request, "index.html", context)

def show_book(request):
    context = {
        "title": Book.objects.get(id=2).title
    }
    return render(request, "show_book.html", context)
