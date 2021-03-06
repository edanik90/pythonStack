from django.shortcuts import render, redirect
from time import gmtime, strftime
import random

def index(request):
    if not 'gold_amount' in request.session:
        request.session['gold_amount'] = 0
    if request.session['gold_amount'] < 0:
        restart_game(request)
    if not 'log' in request.session:
        request.session['log'] = ""
    return render(request, "index.html")

def process_money(request):
    if request.POST["location"] == "farm":
        temp = random.randint(0,10)
        request.session['gold_amount'] += temp
        request.session['log'] += f"\nEarned {temp} gold at the farm!"
    if request.POST["location"] == "cave":
        temp = random.randint(5,10)
        request.session['gold_amount'] += temp
        request.session['log'] += f"\nEarned {temp} gold at the cave!"
    if request.POST["location"] == "house":
        temp = random.randint(2,5)
        request.session['gold_amount'] += temp
        request.session['log'] += f"\nEarned {temp} gold at the house!"
    if request.POST["location"] == "casino":
        temp = random.randint(-50,50)
        request.session['gold_amount'] += temp
        if temp > 0:
            request.session['log'] += f"\nEntered casino and won {temp}!!!"
        else:
            request.session['log'] += f"\nEntered casino and lost {abs(temp)}...Ouch..."
    request.session['log'] +=" (" + strftime("%B %d, %Y %H:%M %p", gmtime()) + ")"
    return redirect("/")

def restart_game(request):
    request.session['gold_amount'] = 0
    request.session['log'] = ""
    return redirect("/")