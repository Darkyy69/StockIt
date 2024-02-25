from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

Documents_router = DefaultRouter()
Documents_router.register(r'BonCMD',BonCMDViewSet, basename='BonCMD')
Documents_router.register(r'Facture',FactureViewSet, basename='Facture')
Documents_router.register(r'FactureAvoir',FactureAvoirViewSet, basename='FactureAvoir')
Documents_router.register(r'BonArtIn',BonArtInViewSet, basename='BonArtIn')
Documents_router.register(r'BonArtOut',BonArtOutViewSet, basename='BonArtOut')
Documents_router.register(r'FactureProfor',FactureProforViewSet, basename='FactureProfor')
Documents_router.register(r'BonLivraison',BonLivraisonViewSet, basename='BonLivraison')
Documents_router.register(r'BonReception',BonReceptionViewSet, basename='BonReception')

Entite_Marchandise_router = DefaultRouter()
Entite_Marchandise_router.register(r'Something',BonCMDViewSet, basename='Something')



# urlpatterns = [
    # path('documents/', include(Documents_router.urls)),
    # path('entite-marchandise/', include(Entite_Marchandise_router.urls)),
    # path('entite-personnes/', include(router.urls)),
    # path('info-extra/', include(router.urls)),
    # path('ligne-document/', include(router.urls)),
    # path('payement/', include(router.urls)),
    # path('remise/', include(router.urls)),
    # path('stock/', include(router.urls)),
# ]
