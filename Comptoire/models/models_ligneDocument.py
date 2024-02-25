from django.db import models

# Create your models here. tous ce qui conserne les document type bons et facturations

class LigneDocument(models.Model):  # COMM0N 
    id_doc = models.IntegerField()
    id_art = models.IntegerField()
    qte = models.CharField(max_length=255) 
    prix = models.FloatField()
    montant = models.FloatField()
  
    class Meta: 
        abstract = True



class LigneBonCMD(LigneDocument):
    def __str__(self):
        return str(self.id)
class LigneFacture(LigneDocument):
    def __str__(self):
        return str(self.id)
class LigneFactureAvoir(LigneDocument):
    def __str__(self):
        return str(self.id)
class LigneBonArtIn(LigneDocument):
    def __str__(self):
        return str(self.id)
class LigneBonArtOut(LigneDocument):
    def __str__(self):
        return str(self.id)
class LigneFactureProfor(LigneDocument):
    def __str__(self):
        return str(self.id)
class LigneBonLivraison(LigneDocument):
    def __str__(self):
        return str(self.id)
class LigneBonReception(LigneDocument):
    def __str__(self):
        return str(self.id) 


        