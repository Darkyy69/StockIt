from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator
import re
# Create your models here.

def validate_barcode(value):
    if not re.match(r'^\d{13}$', str(value)):
        raise ValidationError(
            _('%(value)s is not a valid 13-digit barcode'),
            params={'value': value},
        )    




class Famille(models.Model):
    codif = models.CharField(max_length=10)
    disignation = models.CharField(max_length=50)
    def __str__(self):
        return 'Famille: ' + str(self.pk)
    
class S_famille(models.Model):
    id_famille = models.ForeignKey(Famille, on_delete=models.CASCADE)
    codif = models.CharField(max_length=10)
    disignation = models.CharField(max_length=50)
    def __str__(self):
        return 'S_famille: ' + str(self.pk)
    
class S_article(models.Model):
    codif = models.CharField(max_length=10)
    disignation = models.CharField(max_length=50)
    def __str__(self):
        return 'S_article: ' + str(self.pk)

class Article (models.Model):
    id_S_famille = models.ForeignKey(S_famille, on_delete=models.CASCADE)
    id_S_article = models.ForeignKey(S_article, on_delete=models.CASCADE)
    codif = models.CharField(max_length=10, blank=False)
    disignation = models.CharField(max_length=50, blank=False)
    P_achat = models.FloatField()
    P_vente = models.FloatField(blank=False, validators=[MinValueValidator(limit_value=0)]) # >0
    P_min = models.FloatField()
    barrcode = models.CharField(max_length=13, validators=[validate_barcode], unique=True)
    fournisseur_best = models.IntegerField()

    def __str__(self):
        return 'Article: ' + str(self.pk) + ' - Barrcode: ' + str(self.barrcode)
    

#Todo

class Bon (models.Model):
    datetime = models.DateTimeField()
    # id_propreat
    montant = models.FloatField(default=0.0)
    
    def __str__(self):
        return self.pk

#Todo
    
class ligne_Bon(models.Model):
    id_Bon = models.ForeignKey(Bon, on_delete=models.CASCADE)
    id_Art = models.ForeignKey(Article, on_delete=models.CASCADE)
    Qte    = models.IntegerField()
    Prix   = models.FloatField()
    Total  = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.Total = self.Prix * self.Qte
        super(ligne_Bon, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.pk)  # Ensure to return a string    


# Todo
class Wilaya(models.Model):
    pass




class Client(models.Model):
    # R.S = models.
    Nom = models.CharField(max_length=30)
    Tel = models.IntegerField()
    adresse = models.CharField(max_length=150)
    creance_init = models.FloatField()
    id_wilaya = models.ForeignKey(Wilaya, on_delete=models.CASCADE)


class Fournisseur(models.Model):
    # R.S = models.
    Nom = models.CharField(max_length=30)
    Tel = models.IntegerField()
    adresse = models.CharField(max_length=150)
    credit_init = models.FloatField()
    id_wilaya = models.ForeignKey(Wilaya, on_delete=models.CASCADE)

