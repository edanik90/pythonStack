from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('my_favorite_books', views.my_favorite_books),
    path('add_new_book', views.add_new_book),
    path('<int:book_id>', views.book_info),
    path('edit/<int:book_id>',views.edit_book),
    path('<int:book_id>/unfavorite', views.unfavorite),
    path('<int:book_id>/add_favorite', views.add_to_favorite),
    path('logout', views.logout)
]