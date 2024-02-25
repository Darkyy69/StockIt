from django.db import models
# from .models_Entite_personnes import *
# Create your models here. tous ce qui conserne les document type bons et facturations

class Remise(models.Model):  # COMM0N 
    client = models.IntegerField() # foreign key selon heritage
    date = models.DateTimeField()
    etablissement = models.IntegerField() # foreign key selon heritage
    montant = models.FloatField()
  
    class Meta: 
        abstract = True



class RemiseFournisseur(Remise):
    def __str__(self):
        return str(self.id)
    
class RemiseClient(Remise):
    def __str__(self):
        return str(self.id)
    
class RemiseEtablissement(Remise):
    def __str__(self):
        return str(self.id)
    
class RemiseSousTraitent(Remise):
    def __str__(self):
        return str(self.id)
    
        