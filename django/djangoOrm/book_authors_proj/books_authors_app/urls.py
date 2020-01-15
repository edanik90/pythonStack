from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('books/<int:book_id>', views.book),
    path('authors', views.authors),
    path('authors/<int:author_id>', views.author)
]