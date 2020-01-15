from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('books/add', views.add_book),
    path('books/<int:book_id>', views.book),
    path('authors', views.authors),
    path('authors/add', views.add_author),
    path('authors/<int:author_id>', views.author)
]