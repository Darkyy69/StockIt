from rest_framework.routers import DefaultRouter
from Comptoire.api.urls import Documents_router, Entite_Marchandise_router, Entite_Personnes_router, Stock_router, Remise_router, Payement_router, Ligne_Document_router, Info_Extra_router 
from django.urls import path, include

# router = DefaultRouter()
# router.registry.extend(Documents_router.registry)
# router.registry.extend(Entite_Marchandise_router.registry)

urlpatterns = [
    # path('', include(router.urls)),
    # path('', include('Comptoire.api.urls')),
    path('comptoire/documents/', include(Documents_router.urls)),
    path('comptoire/entite-marchandise/', include(Entite_Marchandise_router.urls)),
    path('comptoire/entite-personnes/', include(Entite_Personnes_router.urls)),
    path('comptoire/info-extra/', include(Info_Extra_router.urls)),
    path('comptoire/ligne-document/', include(Ligne_Document_router.urls)),
    path('comptoire/payement/', include(Payement_router.urls)),
    path('comptoire/remise/', include(Remise_router.urls)),
    path('comptoire/stock/', include(Stock_router.urls)),
    
]
