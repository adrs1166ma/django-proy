from django.shortcuts import render, HttpResponse

# Create your views here.

def hola_mundo(request):
    return HttpResponse("Hola mundo!!!")

def index(request):
    return render(request,"index.html")