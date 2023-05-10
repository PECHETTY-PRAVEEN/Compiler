from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index,name='home'),
    path('',views.compiler_python,name='compiler')
]
