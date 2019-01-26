from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'yb123/index.html',
    )

def one(request):
    return render(request, 'yb123/one.html',
    )

def two(request):
    return render(request, 'yb123/two.html',
    )

def three(request):
    return render(request, 'yb123/three.html',
    )