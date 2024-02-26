from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.documents_views import *
from .views.entite_marchandise_views import *
from .views.entite_personnes_views import *
from .views.info_extra_views import *
from .views.ligne_document_views import *
from .views.payement_views import *
from .views.remise_views import *
from .views.stock_views import *

# Router for Model Documents
Documents_router = DefaultRouter()
Documents_router.register(r'bon-cmd',BonCMDViewSet, basename='bon-cmd')
Documents_router.register(r'facture',FactureViewSet, basename='facture')
Documents_router.register(r'facture-avoir',FactureAvoirViewSet, basename='facture-avoir')
Documents_router.register(r'bon-art-in',BonArtInViewSet, basename='bon-art-in')
Documents_router.register(r'bon-art-out',BonArtOutViewSet, basename='bon-art-out')
Documents_router.register(r'facture-profor',FactureProforViewSet, basename='facture-profor')
Documents_router.register(r'bon-livraison',BonLivraisonViewSet, basename='bon-livraison')
Documents_router.register(r'bon-reception',BonReceptionViewSet, basename='bon-reception')

# Router for Model Entite_personnes
Entite_Personnes_router = DefaultRouter()
Entite_Personnes_router.register(r'fournisseur',FournisseurViewSet, basename='fournisseur')
Entite_Personnes_router.register(r'client',ClientViewSet, basename='client')
Entite_Personnes_router.register(r'etablissement',EtablissementViewSet, basename='etablissement')
Entite_Personnes_router.register(r'sous-traitent',SousTraitentViewSet, basename='sous-traitent')

# Router for Model Entite_marchandise
Entite_Marchandise_router = DefaultRouter()
Entite_Marchandise_router.register(r'famille',FamilleViewSet, basename='famille')
Entite_Marchandise_router.register(r's-famille',S_familleViewSet, basename='s-famille')
Entite_Marchandise_router.register(r's-article',S_articleViewSet, basename='s-article')
Entite_Marchandise_router.register(r'article',ArticleViewSet, basename='article')

# Router for Model info_extra
Info_Extra_router = DefaultRouter()
Info_Extra_router.register(r'type-payement',TypePayementViewSet, basename='type-payement')
Info_Extra_router.register(r'type-client',TypeClientViewSet, basename='type-client')
Info_Extra_router.register(r'etats-client',EtatsClientViewSet, basename='etats-client')
Info_Extra_router.register(r'etat-operations',EtatoperationsViewSet, basename='etat-operations')
Info_Extra_router.register(r'liste-etat-sortie',LiseEtatSortieViewSet, basename='liste-etat-sortie')

# Router for Model LigneDocument
Ligne_Document_router = DefaultRouter()
Ligne_Document_router.register(r'ligne-bon-cmd',LigneBonCMDViewSet, basename='ligne-bon-cmd')
Ligne_Document_router.register(r'ligne-facture',LigneFactureViewSet, basename='ligne-facture')
Ligne_Document_router.register(r'ligne-facture-avoir',LigneFactureAvoirViewSet, basename='ligne-facture-avoir')
Ligne_Document_router.register(r'ligne-bon-art-in',LigneBonArtInViewSet, basename='ligne-bon-art-in')
Ligne_Document_router.register(r'ligne-bon-art-out',LigneBonArtOutViewSet, basename='ligne-bon-art-out')
Ligne_Document_router.register(r'ligne-facture-profor',LigneFactureProforViewSet, basename='ligne-facture-profor')
Ligne_Document_router.register(r'ligne-bon-livraison',LigneBonLivraisonViewSet, basename='ligne-bon-livraison')
Ligne_Document_router.register(r'ligne-bon-reception',LigneBonReceptionViewSet, basename='ligne-bon-reception')

# Router for Model Payement
Payement_router = DefaultRouter()
Payement_router.register(r'payement-fournisseur',PayementFournisseurViewSet, basename='payement-fournisseur')
Payement_router.register(r'payement-client',PayementClientViewSet, basename='payement-client')
Payement_router.register(r'payement-sous-traitant',PayementSousTraitantViewSet, basename='payement-sous-traitant')
Payement_router.register(r'payement-etablissement',PayementEtablissementViewSet, basename='payement-etablissement')

# Router for Model Remise
Remise_router = DefaultRouter()
Remise_router.register(r'remise-fournisseur',RemiseFournisseurViewSet, basename='remise-fournisseur')
Remise_router.register(r'remise-client',RemiseClientViewSet, basename='remise-client')
Remise_router.register(r'remise-etablissement',RemiseEtablissementViewSet, basename='remise-etablissement')
Remise_router.register(r'remise-sous-traitent',RemiseSousTraitentViewSet, basename='remise-sous-traitent')

# Router for Model Stock
Stock_router = DefaultRouter()
Stock_router.register(r'stock',StockViewSet, basename='stock')
Stock_router.register(r'mvt-stock',MvtStockViewSet, basename='mvt-stock')
