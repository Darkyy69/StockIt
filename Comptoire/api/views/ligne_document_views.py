from rest_framework.viewsets import ModelViewSet
from ...models.models_ligneDocument import *
from ..serializers import LigneBonCMDSerializer, LigneFactureSerializer, LigneFactureAvoirSerializer, LigneBonArtInSerializer, LigneBonArtOutSerializer, LigneFactureProforSerializer, LigneBonLivraisonSerializer, LigneBonReceptionSerializer


class LigneBonCMDViewSet(ModelViewSet):
    queryset = LigneBonCMD.objects.all()
    serializer_class = LigneBonCMDSerializer

class LigneFactureViewSet(ModelViewSet):
    queryset = LigneFacture.objects.all()
    serializer_class = LigneFactureSerializer

class LigneFactureAvoirViewSet(ModelViewSet):
    queryset = LigneFactureAvoir.objects.all()
    serializer_class = LigneFactureAvoirSerializer

class LigneBonArtInViewSet(ModelViewSet):
    queryset = LigneBonArtIn.objects.all()
    serializer_class = LigneBonArtInSerializer

class LigneBonArtOutViewSet(ModelViewSet):
    queryset = LigneBonArtOut.objects.all()
    serializer_class = LigneBonArtOutSerializer

class LigneFactureProforViewSet(ModelViewSet):
    queryset = LigneFactureProfor.objects.all()
    serializer_class = LigneFactureProforSerializer

class LigneBonLivraisonViewSet(ModelViewSet):
    queryset = LigneBonLivraison.objects.all()
    serializer_class = LigneBonLivraisonSerializer

class LigneBonReceptionViewSet(ModelViewSet):
    queryset = LigneBonReception.objects.all()
    serializer_class = LigneBonReceptionSerializer