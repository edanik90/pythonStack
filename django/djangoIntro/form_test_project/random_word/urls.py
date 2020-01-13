from django.urls import path
from . import views

urlpatterns = [
    path('', views.random_word),
    path('reset_resets/', views.reset_count)
]
