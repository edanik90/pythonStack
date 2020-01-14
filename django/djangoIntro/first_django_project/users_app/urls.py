from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register_user),
    path('', views.index),
    path('users', views.users_show),
    path('users/new', views.register_user),
    path('login', views.login)
]