from django.db import models
from django.contrib.auth.models import User
from .models_Entite_personnes import *
from .models_info_extra import *
# Create your models here. tous ce qui conserne les document type bons et facturations


class Documents(models.Model):  # COMM0N 
    num = models.CharField(max_length=255) 
    date = models.DateTimeField()
    propretaire = models.IntegerField()
    montant = models.FloatField()
    type_payement = models.ForeignKey(TypePayement, on_delete=models.SET_NULL, null=True) 
    etat = models.ForeignKey(Etatoperations, on_delete=models.SET_NULL, null=True) 
    imprime = models.ForeignKey(LiseEtatSortie, on_delete=models.SET_NULL, null=True) 
    editeur = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta: 
        abstract = True        


class BonCMD(Documents):
    def __str__(self):
        return str(self.id)
    
class Facture(Documents):
    def __str__(self):
        return str(self.id)
class FactureAvoir(Documents):
    def __str__(self):
        return str(self.id)
class BonArtIn(Documents):
    def __str__(self):
        return str(self.id)
class BonArtOut(Documents):
    def __str__(self):
        return str(self.id)
class FactureProfor(Documents):
    def __str__(self):
        return str(self.id)
class BonLivraison(Documents):
    def __str__(self):
        return str(self.id)  
class BonReception(Documents):
    def __str__(self):
        return str(self.id)       

class BonTransfer(Documents):
    def __str__(self):
        return str(self.id)  

class BonRecuperation(Documents):
    def __str__(self):
        return str(self.id)  

class BonTranzition(Documents):
    def __str__(self):
        return str(self.id)                                 


