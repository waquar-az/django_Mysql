from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home,name='home'),
    path('saveparty/',views.Saveparty,name='saveparty'),
    path('insertuser/',views.insertuser,name='insertuser'),
]
