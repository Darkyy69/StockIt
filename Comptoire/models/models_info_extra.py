from django.db import models
from django.contrib.auth.models import User
from .models_Entite_personnes import *



class TypePayement(models.Model):
    typePayement = models.CharField(max_length=10) 
    def __str__(self):
        return str(self.typePayement)+' - '+str(self.id)
    
class TypeClient(models.Model):
    typeClient = models.CharField(max_length=10) 
    def __str__(self):
        return str(self.typeClient)

class EtatsClient(models.Model):
    etatDisignation = models.CharField(max_length=10)
    def __str__(self):
        return str(self.etatDisignation)
    
class Etatoperations(models.Model):
    etatOperation = models.CharField(max_length=50)
    def __str__(self):
        return str(self.etatOperation)
    
class LiseEtatSortie(models.Model):
    etatimprimable = models.CharField(max_length=50)
    def __str__(self):
        return str(self.etatimprimable)        