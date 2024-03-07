from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator
from .models_info_extra import TypeClient,EtatsClient
import re
from .models_ligneDocument import LigneFacture


class Propreot(models.Model):  # COMM0N 
    RSS = models.CharField(max_length=50) 
    nom = models.CharField(max_length=50)
    adresse = models.CharField(max_length=200)
    credit_init = models.FloatField()
    type = models.ForeignKey(TypeClient, on_delete=models.SET_NULL, null=True) 
    etat = models.ForeignKey(EtatsClient, on_delete=models.SET_NULL, null=True) 
    registre_commerce = models.CharField(max_length=50)
    NIF = models.CharField(max_length=50)
    NIS = models.CharField(max_length=50)
    ART = models.CharField(max_length=50)
    BP = models.CharField(max_length=50)
  
    class Meta: 
        abstract = True



class Fournisseur(Propreot):
    def __str__(self):
        return str(self.id)
    
class Client(Propreot):
    def __str__(self):
        return str(self.id)
    
class Etablissement(Propreot):
    def __str__(self):
        return str(self.id)
    
class SousTraitent(Propreot):
    def __str__(self):
        return str(self.id)
    