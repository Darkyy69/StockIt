from rest_framework.routers import DefaultRouter
from Comptoire.api.urls import Documents_router, Entite_Marchandise_router
from django.urls import path, include

# router = DefaultRouter()
# router.registry.extend(Documents_router.registry)
# router.registry.extend(Entite_Marchandise_router.registry)

urlpatterns = [
    # path('', include(router.urls)),
    # path('', include('Comptoire.api.urls')),
    path('documents/', include(Documents_router.urls)),
    path('entite-marchandise/', include(Entite_Marchandise_router.urls)),
    # path('entite-personnes/', include(router.urls)),
    # path('info-extra/', include(router.urls)),
    # path('ligne-document/', include(router.urls)),
    # path('payement/', include(router.urls)),
    # path('remise/', include(router.urls)),
    # path('stock/', include(router.urls)),
]
