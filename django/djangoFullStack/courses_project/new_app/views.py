from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

def index(request):
    context = {
        "courses":Course.objects.all()
    }
    return render(request, "index.html", context)

def add_course(request):
    errors = Course.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    new_description = Description.objects.create(content = request.POST['description'])
    Course.objects.create(name = request.POST['name'], description = new_description)
    return redirect("/")

def destroy(request, course_id):
    context = {
        "course": Course.objects.get(id = course_id)
    }
    return render(request, "Destroy.html", context)

def delete_course(request, course_id):
    Course.objects.get(id = course_id).delete()
    return redirect("/")