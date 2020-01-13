from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def random_word(request):
    if not 'count' in request.session:
        request.session['count'] = 0
    request.session['count'] += 1
    context = {
        "new_word":get_random_string(length = 12)
    }
    return render(request, "random_word.html", context)

def reset_count(request):
    request.session['count'] = 0
    return redirect("/random_word/")