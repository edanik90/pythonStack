from django.shortcuts import render, HttpResponse, redirect

def register_user(request):
    return HttpResponse("placeholder for users to create a new user record")

def login(request):
    return HttpResponse("placeholder for users to log in")

def index(request):
    return redirect("/users")

def users_show(request):
    return HttpResponse("placeholder to later display all the list of users")