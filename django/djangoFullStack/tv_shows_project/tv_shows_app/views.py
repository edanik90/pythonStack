from django.shortcuts import render, redirect
from .models import Show
from django.contrib import messages

def shows(request):
    context = {
        "shows":Show.objects.all()
    }
    return render(request, "index.html", context)

def index(request):
    return redirect("/shows")

def new_show(request):
    return render(request, "new_show.html")

def add_new_show(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f"/shows/new")
    else:
        new_show = Show.objects.create(title = request.POST['title'],
            description = request.POST['description'],
            network = request.POST['network'],
            release_date = request.POST['release_date']
            )
        return redirect(f"/shows/{new_show.id}")

def show(request, show_id):
    context = {
        "show":Show.objects.get(id = show_id)
    }
    return render(request, "show.html", context)

def edit_show(request, show_id):
    context = {
        "show":Show.objects.get(id = show_id)
    }
    return render(request, "edit_show.html", context)

def update_show(request, show_id):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f"/shows/{show_id}/edit")
    else:
        new_show = Show.objects.get(id = show_id)
        new_show.title = request.POST['title']
        new_show.description = request.POST['description']
        new_show.network = request.POST['network']
        new_show.release_date = request.POST['release_date']
        new_show.save()
        return redirect(f"/shows/{new_show.id}")

def delete_show(request, show_id):
    show = Show.objects.get(id = show_id)
    show.delete()
    return redirect("/shows")