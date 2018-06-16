from django.contrib import admin
from django.urls import path

from rezerwacja import views

urlpatterns = [
    path('', views.RezerwacjaIndex, name='rezerwacja'),
    path('dodaj/', views.dodajForm, name='addform'),
    path('dodaj_check/', views.dodajRezerwacje, name='dodajrezerwacje'),
    path('szukaj/', views.znajdzForm, name='znajdzForm'),
    path('szukaj_check/', views.szukajcheck, name='szukajcheck'),
    
]
