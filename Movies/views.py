from django.shortcuts import render,HttpResponse

def index(request):
    return render(request, 'Movies/index.html')

def about(request):
    context = {
        'movies': ['black men', 'gladiator', 'iron- man', 'spider-man']
    }
    return render(request, 'Movies/about.html', context)