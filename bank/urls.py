from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [
	path('', views.get_bank, name='bank-ifsc'),
    path('bank/', views.get_bank, name='bank'),
    path('branches/', views.get_branches, name='branches'),
]


