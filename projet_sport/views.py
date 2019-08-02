from django.shortcuts import render
def home(request):
    return render(request,'home.html')


def login(request):
    return render(request,'page/login.html')

def register(request):
    return render(request,'page/register.html')

def pourquoi(request):
    return render(request,"page/pourquoi.html")
