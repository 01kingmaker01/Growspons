from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect
from .utils import *
from app.decorators import unauthenticated_user, allowed_users
from app.forms import UserForm

group_inf='Influencer'

@login_required(login_url='login')
@allowed_users(allowed_roles=[group_inf])
def home(request):
    content = {}
    return render(request, 'home.html', content)


@login_required(login_url='login')
@allowed_users(allowed_roles=[group_inf])
def influencer_details(request):
    content = {}
    return render(request, 'add_details.html', content)

@unauthenticated_user
def loginHandle(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
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
    content = {}
    return render(request, 'authentication/login.html', content)

@unauthenticated_user
def signupHandle(request):
    #influencer account creation
    if request.method == 'POST':
        email = request.POST.get("inf_email")
        password = request.POST.get("inf_pass")
        cpassword = request.POST.get("inf_cpass")
        first_name = request.POST.get("inf_name")
        username = request.POST.get("inf_username")
        if password == cpassword:
            if password_val(password):
                try:
                    user = User.objects.create_user(username=username, password=password, email=email,
                                                    first_name=first_name)
                    group = Group.objects.get(name='Influencer')
                    user.groups.add(group)
                    user.save()
                    login(request, user)
                    request.session.set_expiry(60 * 60 * 24 * 7)
                    messages.success(request, f"created")
                    return redirect('home')
                except:
                    messages.error(request, f"username already exist")
                    return redirect('signUp')
            else:
                messages.error(request, f"Password should contain atleast 6 digit, upper lower case and one symbol")
                return redirect('signUp')
        else:
            messages.error(request, f"Password and cpassword should be same")
            return redirect('signUp')
    content = {}
    return render(request, 'authentication/signup.html',content)

@unauthenticated_user
def companySignupHandle(request):
    email = request.POST.get("cmp_email")
    password = request.POST.get("cmp_pass")
    cpassword = request.POST.get("cmp_cpass")
    first_name = request.POST.get("cmp_name")
    if password == cpassword:
        if password_val(password):
            try:
                user = User.objects.create_user(username=email, password=password, email=email, first_name=first_name)
                group = Group.objects.get(name='Company')
                user.groups.add(group)
                user.save()
                login(request, user)
                request.session.set_expiry(60 * 60 * 24 * 7)
                messages.success(request, f"created")
                return redirect('index')
            except:
                messages.error(request, f"username already exist")
                return redirect('signUp')

        else:
            messages.error(request, f"Password should contain atleast 6 digit, upper lower case and one symbol")
            return redirect('signUp')
    else:
        messages.error(request, f"Password and confirm password should be same")
        return redirect('signUp')


def handleLogout(request):
    logout(request)
    messages.success(request, f"Good bye :)")
    return redirect('login')
