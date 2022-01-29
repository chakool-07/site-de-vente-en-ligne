from django.contrib import admin

from shop.models import Produit,Category

# Register your models here.

class AdminCategory(admin.ModelAdmin):
    list_display = ('nom', 'date_ajout',)

class AdminProduit(admin.ModelAdmin):
    list_display = ('titre', 'prix', 'category', 'date_ajout',)
admin.site.register(Produit,AdminProduit)
admin.site.register(Category, AdminCategory)
