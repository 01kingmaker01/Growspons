from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('', home, name='home'),
	path('view/<slug>', viewinf, name='viewinf'),
    path('influencer_details/', influencer_details, name="influencer_details"),
    path('dashboard/', dashboardInf, name="dashboardInf"),
	path('dashboard/filter', dashboardFilter, name="dashboardFilter"),
    path('add_post/', influencerPost, name="influencerPost"),


    path('login/', loginHandle, name='login'),
    path('register/', signupHandle, name='signUp'),
    path('logout/', handleLogout, name='logout'),
    path('company_register/', companySignupHandle, name='companySignupHandle'),



    path('reset_password/',
	 auth_views.PasswordResetView.as_view(template_name = 'authentication/password_reset.html'),
	  name='reset_password'), #submit email form
	path('reset_password_sent/',
	 auth_views.PasswordResetDoneView.as_view(template_name = 'authentication/password_reset_sent.html'),
	  name='password_reset_done'), #Email send and reset
	path('reset/<uidb64>/<token>',
	 auth_views.PasswordResetConfirmView.as_view(template_name = 'authentication/password_reset_form.html'),
	  name='password_reset_confirm'), #link to reset and email
	path('reset_password_complete/',
	 auth_views.PasswordResetCompleteView.as_view(template_name = 'authentication/password_reset_done.html'),
	  name='password_reset_complete'), #password successfully send
]