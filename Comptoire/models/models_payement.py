from django.db import models

from django.db import models
from .models_info_extra import TypeClient,EtatsClient


class Payement(models.Model):  # COMM0N 
    date = models.DateTimeField() 
    montant = models.FloatField()
    propreot = models.IntegerField()
    editeur = models.IntegerField()
    type = models.IntegerField()
    class Meta: 
        abstract = True



class PayementFournisseur(Payement):
    def __str__(self):
        return str(self.id)
    
class PayementClient(Payement):
    def __str__(self):
        return str(self.id)
    
class PayementSousTraitant(Payement):
    def __str__(self):
        return str(self.id)
    
class PayementEtablissement(Payement):
    def __str__(self):
        return str(self.id)
    