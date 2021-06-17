from django.shortcuts import render

def home(request):
    context={
        'start':'hello world',
    }
    return render(request,'leaderboard\home.html',context)
