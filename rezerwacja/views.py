from django.shortcuts import render

def RezerwacjaIndex(request):
    return render(request, 'rezerwacja_index.html')

def dodajForm(request):
    return render(request, 'add/form_rezerwacja.html')

def dodajRezerwacje(request):
    tytul = request.POST.get('tytul')
    autor = request.POST.get('autor')
    wersja = request.POST.get('wersja')

    if request.method == 'POST':
        model = RezerwacjaModel.objects.create(
                                    tytul = tytul,
                                    autor = autor,
                                    wersja = wersja
                                    )
        model.save()
        return render(request, 'add/success.html')
    else:
        return render(request, 'add/fail.html')
'''' Dodawanie gotowe kurwa wreszcie huj'''

def znajdzForm(request):
    return render(request, 'znajdz/znajdz_form.html')

def szukajcheck(request):
    tytul = request.POST.get('')
