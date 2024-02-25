from django.contrib import admin
from .models.models_Entite_marchandise import *
from .models.models_documents import *
from .models.models_ligneDocument import *
from .models.models_remise import *
from .models.models_stock import *
from .models.models_payement import *
# Register your models here.

admin.site.register(Article)
admin.site.register(Famille)
admin.site.register(S_famille)
admin.site.register(S_article)

admin.site.register(BonCMD)
admin.site.register(Facture)
admin.site.register(FactureAvoir)
admin.site.register(BonArtIn)
admin.site.register(BonArtOut)
admin.site.register(FactureProfor)
admin.site.register(BonLivraison)
admin.site.register(BonReception)

admin.site.register(LigneBonCMD)
admin.site.register(LigneFacture)
admin.site.register(LigneFactureAvoir)
admin.site.register(LigneBonArtIn)
admin.site.register(LigneBonArtOut)
admin.site.register(LigneFactureProfor)
admin.site.register(LigneBonLivraison)
admin.site.register(LigneBonReception)

admin.site.register(TypePayement)
admin.site.register(Etatoperations)
admin.site.register(TypeClient)
admin.site.register(EtatsClient)
admin.site.register(LiseEtatSortie)

admin.site.register(Fournisseur)
admin.site.register(Client)
admin.site.register(Etablissement)
admin.site.register(SousTraitent)

admin.site.register(Stock)
admin.site.register(MvtStock)

admin.site.register(RemiseClient)
admin.site.register(RemiseEtablissement)
admin.site.register(RemiseFournisseur)
admin.site.register(RemiseSousTraitent)

admin.site.register(PayementClient)
admin.site.register(PayementEtablissement)
admin.site.register(PayementFournisseur)
admin.site.register(PayementSousTraitant)
