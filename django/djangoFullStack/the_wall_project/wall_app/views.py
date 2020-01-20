from django.shortcuts import render, redirect
from django.contrib import messages
from login_app.models import *

def wall(request):
    if not 'user_id' in request.session:
        messages.error(request, "Please, log in first!")
        return redirect("/")
    context = {
        "messages":Message.objects.all().order_by("-created_at")
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
