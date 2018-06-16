from django.shortcuts import render

from .models import BookModel

def BookShare(request):
    return render(request, 'book/book_index.html')

def addBook(request):
    tytul = request.POST.get('tytul')
    autor = request.POST.get('autor')
    kategoria = request.POST.get('kategoria')
    wersja = request.POST.get('wersja')

    if request.method == 'POST':
        model = BookModel.objects.create(
                                    tytul = tytul,
                                    autor = autor,
                                    kategoria = kategoria,
                                    wersja = wersja
                                    )
        model.save()
        return render(request, 'book/success.html')
    else:
        return render(request, 'book/fail.html')
