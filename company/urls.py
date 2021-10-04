from os import name
from . import views
from django.urls import path

urlpatterns = [
    path('',views.index, name='index'),
    path("posted/",views.posted,name="posted")
]