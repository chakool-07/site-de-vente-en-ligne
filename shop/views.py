from django.shortcuts import render

from shop.models import Produit

# Create your views here.

def index(request):
    article = Produit.objects.all()
    item_name = request.GET.get('item-name')
    if item_name !='' and item_name is not None:
        article = Produit.objects.filter(titre__icontains=item_name)
   
    return render(request, "index.html", {'article': article})

def detail(request,id_produit):
    article = Produit.objects.get(id=id_produit)
    
    return render(request, "detail.html", {'article': article})