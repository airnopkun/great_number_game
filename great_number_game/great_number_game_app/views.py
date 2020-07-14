from django.shortcuts import render, HttpResponse, redirect
import random


high_low_equal = None


def index(request):
    global high_low_equal
    context = {
        "high_low_equal": high_low_equal
    }
    if 'num' not in request.session:
        request.session['num'] = random.randint(1, 100)
    return render(request, 'index.html', context)


def guess(request):
    global high_low_equal
    if request.POST['guess']:
        if int(request.POST['guess']) == request.session['num']:
            high_low_equal = 'equal'
        if int(request.POST['guess']) > request.session['num']:
            high_low_equal = 'high'
        if int(request.POST['guess']) < request.session['num']:
            high_low_equal = 'low'
    return redirect('/')


def new_game(request):
    global high_low_equal
    high_low_equal = None
    del request.session['num']
    return redirect('/')
