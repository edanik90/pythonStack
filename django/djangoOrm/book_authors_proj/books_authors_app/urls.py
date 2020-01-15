from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('book/add', views.add_book),
    path('book/<int:book_id>/add_author', views.add_author_to_book),
    path('books/<int:book_id>', views.book),
    path('authors', views.authors),
    path('author/add', views.add_author),
    path('author/<int:author_id>/add_book', views.add_book_to_author),
    path('authors/<int:author_id>', views.author)
]