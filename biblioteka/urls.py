from django.contrib import admin
from django.urls import path, include

from biblioteka import views

urlpatterns = [
    path('', views.Liblary, name='biblioteka'),

]
