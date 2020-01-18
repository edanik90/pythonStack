from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, "index.html")

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        new_user = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            birthday = request.POST['birthday'],
            email = request.POST['email'],
            password = pw_hash)
        request.session['new_user_id'] = new_user.id
        request.session['first_name'] = new_user.first_name
        return redirect("/success")

def login(request):
        try:
            user = User.objects.get(email=request.POST['email'])
        except:
            messages.error(request, "Invalid email or password")
            return redirect("/")
        if not bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
            messages.error(request, "Invalid email or password")
            return redirect("/")
        else:
            request.session['user_id'] = user.id
            request.session['first_name'] = user.first_name
            return redirect("/success")
        return redirect("/")

def success(request):
    if not "user_id" and not "new_user_id" in request.session:
        messages.error(request, "Please, log in first!")
        return redirect("/")
    else:
        if "new_user_id" in request.session:
            messages.info(request, "You have successfully registered!")
        else:
            messages.info(request, "You have successfully loged in!")
        return render(request, "success.html")

def logout(request):
    request.session.clear()
    return redirect("/")