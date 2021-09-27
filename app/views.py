from django.shortcuts import render, redirect


def home(request):
    context = {}
    return render(request, 'home.html', context)

def login(request):
    if request.method == "POST":
        email = request.GET.get("email")
        password = request.GET.get("password")
        
        return redirect('')
    context = {}
    return render(request, 'authentication/login.html', context)

def signUp(request):

    context = {}
    return render(request, 'authentication/signup.html',context)