from django.contrib import admin
from django.urls import path,include
from firstapp import views

urlpatterns = [
   path('',views.login,name='login'),
]