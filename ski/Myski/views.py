from django.shortcuts import render
from .forms import LivreForm
from . import models


def index(request):
    return render(request, 'Myski/index.html')

def ajout(request):
    if request.method == "POST":
        form = LivreForm(request)
        if form.is_valid():
            station = form.save()
            return render(request,"Magasin/affiche.html",{"Livre" : station})
        else:
            return render(request,"Magasin/ajout.html",{"form": form})
    else :
        form = LivreForm()
        return render(request,"Magasin/ajout.html",{"form" : form})

def traitement(request):
lform = LivreForm(request.POST)
if lform.is_valid():
Livre = lform.save()
    return render(request,"Magasin/affiche.html",{"Livre" : Livre})
else:
return render(request,"Magasin/ajout.html",{"form": lform})

def affiche(request, id):
    Livre = models.Livre.objects.get(pk=id)
    return render(request,"bibliotheque/affiche.html",{"Livre": Livre})