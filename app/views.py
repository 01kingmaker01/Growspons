from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect

from app.decorators import unauthenticated_user
from app.forms import UserForm


def home(request):
    context = {}
    return render(request, 'home.html', context)

@unauthenticated_user
def loginHandle(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            request.session.set_expiry(60 * 60 * 24 * 7)
            if user.is_staff:
                messages.success(request, 'welcome back :)')
                return redirect('index')
            messages.success(request, 'welcome back :)')
            return redirect('home')

        else:
            messages.error(request, 'Wrong username or password')
            return redirect('login')
    context = {}
    return render(request, 'authentication/login.html', context)

@unauthenticated_user
def signupHandle(request):
    user_form = UserForm()
    context = {'user_form':user_form}
    #influencer account creation
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            username = user_form.cleaned_data.get("username")
            user = User.objects.get(username=username)
            group = Group.objects.get(name='Influencer')
            user.groups.add(group)
            user.save()
            messages.success(request, f"created")
            return redirect('home')
        else:
            messages.error(request, f"Please enter correct information")
            return redirect('signUp')
    return render(request, 'authentication/signup.html',context)

def companySignupHandle(request):
    user_form = UserForm(request.POST)
    if user_form.is_valid():
        user_form.save()
        username = user_form.cleaned_data.get("username")
        user = User.objects.get(username=username)
        group = Group.objects.get(name='Company')
        user.groups.add(group)
        user.is_staff = True
        user.save()
        messages.success(request, f"created")
        return redirect('index')
    else:
        messages.error(request, f"Please enter correct information")
        return redirect('signUp')

def handleLogout(request):
    logout(request)
    messages.success(request, f"Good bye :)")
    return redirect('login')
