from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('add_new_book', views.add_new_book),
    path('<int:book_id>', views.book_info),
    path('logout', views.logout)
]