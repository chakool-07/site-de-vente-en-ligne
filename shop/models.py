from django.db import models
from django.db.models import ForeignKey


# Create your models here.
class Category(models.Model):
    nom = models.CharField(max_length=100)
    date_ajout = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_ajout']
      
    def __str__(self):
        return self.nom 

class Produit(models.Model):
    titre = models.CharField(max_length=100)
    prix = models.FloatField()
    description = models.TextField()
    category = ForeignKey(Category, related_name='categorie', on_delete=models.CASCADE)
    image =models.CharField(max_length=5000)
    date_ajout = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_ajout']
    def __str__(self):
        return self.titre
        