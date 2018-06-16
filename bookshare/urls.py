from django.contrib import admin
from django.urls import path, include

from bookshare import views

urlpatterns = [
    path('', views.BookShare, name='bookshare'),
    path('add_book', views.addBook, name='addbook'),

]
