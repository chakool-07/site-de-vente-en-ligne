from django.urls import path
from shop.views import index,detail

urlpatterns=[
    path('', index, name= 'home'),
    path('<int:id_produit>', detail, name='detail'),

] 

# https://github.com/chakool-07/site-de-vente-en-ligne.git 