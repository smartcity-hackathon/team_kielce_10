from django.db import models

class BookModel(models.Model):
    tytul = models.CharField(max_length = 100, default =None, null = None)
    autor = models.CharField(max_length = 100, default = None, null = None)
    kategoria = models.CharField(max_length = 100, default = None, null = None)
    wersja = models.CharField(max_length = 100, default =None, null = None)
