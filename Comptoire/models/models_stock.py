from django.db import models
from .models_Entite_marchandise import *
from .models_Entite_personnes import *
# Create your models here. tous ce qui conserne les document type bons et facturations

class Stock(models.Model):  # COMM0N 
    id_Art = models.ForeignKey(Article, on_delete=models.CASCADE) # foreign key selon heritage
    qte = models.FloatField()
    etablissement = models.ForeignKey(Etablissement, on_delete=models.CASCADE) # foreign key selon heritage

    def __str__(self):
        return str(self.id)
    


class MvtStock(models.Model):    
    id_Art = models.ForeignKey(Article, on_delete=models.CASCADE) # foreign key selon heritage
    qte = models.FloatField()
    entree = models.BooleanField()
    sortie = models.BooleanField()
    etablissement = models.ForeignKey(Etablissement, on_delete=models.CASCADE) # foreign key selon heritage

    def __str__(self):
        return str(self.id)
    