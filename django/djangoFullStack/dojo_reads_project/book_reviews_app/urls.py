from django.urls import path
from . import views

urlpatterns = [
    path('', views.books_home),
    path('add', views.page_for_adding),
    path('add_book', views.add_book),
    path('<int:book_id>', views.book_info),
    path('user/<int:user_id>', views.user_info),
    path('<int:book_id>/add_review', views.add_review),
    path('<int:book_id>/review/<int:review_id>/delete', views.delete_review),
    path('logout', views.logout)
]