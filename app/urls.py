from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),

    path('login/', loginHandle, name='login'),
    path('register/', signupHandle, name='signUp'),
    path('logout/', handleLogout, name='logout'),
    path('company_register/', companySignupHandle, name='companySignupHandle'),
]