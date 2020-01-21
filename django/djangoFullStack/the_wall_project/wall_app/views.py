from django.shortcuts import render, redirect
from django.contrib import messages
from login_app.models import *
from .models import *
from datetime import timedelta
from django.utils import timezone
from time import gmtime, strftime

def wall(request):
    if not 'user_id' in request.session:
        messages.error(request, "Please, log in first!")
        return redirect("/")
    context = {
        "all_messages":Message.objects.all().order_by("-created_at")
    }
    return render(request, "wall/wall.html", context)

def post_message(request):
    errors = Message.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/wall")
    Message.objects.create(content = request.POST['message'], user = User.objects.get(id = request.session['user_id']))
    return redirect("/wall")

def delete_message(request):
    message = Message.objects.get(id = request.POST['message_id'])
    current_time = timezone.now()
    print(current_time)
    if message.created_at < current_time - timedelta(minutes = 30):
        messages.error(request, "30 minutes past: you cannot delete this message")
        return redirect("/wall")
    message.delete()
    return redirect("/wall")

def post_comment(request):
    errors = Comment.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/wall")
    Comment.objects.create(content = request.POST['comment'], 
        user = User.objects.get(id = request.session['user_id']),
        message = Message.objects.get(id = request.POST['message_id']))
    return redirect("/wall")

def logout(request):
    request.session.clear()
    return redirect("/")
