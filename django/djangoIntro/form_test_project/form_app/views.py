from django.shortcuts import render, redirect

def index(request):
    return render(request, "index.html")

def create_user(request):
    print("Got Post Info....................")
    name_from_form = request.POST['name']
    email_from_form = request.POST['email']
    password_from_form = request.POST['password']
    context = {
        "name_on_template": name_from_form,
        "email_on_template": email_from_form,
        "password_on_template": password_from_form
    }
    return redirect("/success")

def success(request):
    # this is the success route
    return render(request,"success.html")