from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('book/add', views.add_book),
    path('book/add_author', views.add_book_author),
    path('books/<int:book_id>', views.book),
    path('authors', views.authors),
    path('author/add', views.add_author),
    path('authors/<int:author_id>', views.author)
]