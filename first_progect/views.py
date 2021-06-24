from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def hello_world(request):
    return HttpResponse(b'<h1>Hello World!!!</h1>')


def index(request):
    return render(request, "index.html")
