from rest_framework.viewsets import ModelViewSet
from ...models.models_documents import *
from ..serializers import BonCMDSerializer, FactureSerializer, FactureAvoirSerializer, BonArtInSerializer, BonArtOutSerializer, FactureProforSerializer, BonLivraisonSerializer, BonReceptionSerializer


class BonCMDViewSet(ModelViewSet):
    queryset = BonCMD.objects.all()
    serializer_class = BonCMDSerializer

class FactureViewSet(ModelViewSet):
    queryset = Facture.objects.all()
    serializer_class = FactureSerializer

class FactureAvoirViewSet(ModelViewSet):
    queryset = FactureAvoir.objects.all()
    serializer_class = FactureAvoirSerializer

class BonArtInViewSet(ModelViewSet):
    queryset = BonArtIn.objects.all()
    serializer_class = BonArtInSerializer

class BonArtOutViewSet(ModelViewSet):
    queryset = BonArtOut.objects.all()
    serializer_class = BonArtOutSerializer

class FactureProforViewSet(ModelViewSet):
    queryset = FactureProfor.objects.all()
    serializer_class = FactureProforSerializer

class BonLivraisonViewSet(ModelViewSet):
    queryset = BonLivraison.objects.all()
    serializer_class = BonLivraisonSerializer

class BonReceptionViewSet(ModelViewSet):
    queryset = BonReception.objects.all()
    serializer_class = BonReceptionSerializer
            