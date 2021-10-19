from . import views
from django.urls import path

urlpatterns = [
    path('',views.dashboardCmp, name='dashboardCmp'),
	path('dashboard/filter', views.dashboardFilter, name="dashboardFilterCmp"),]