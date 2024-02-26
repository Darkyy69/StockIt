from rest_framework.viewsets import ModelViewSet
from ...models.models_Entite_personnes import *
from ..serializers import FournisseurSerializer, ClientSerializer, EtablissementSerializer, SousTraitentSerializer


class FournisseurViewSet(ModelViewSet):
    queryset = Fournisseur.objects.all()
    serializer_class = FournisseurSerializer

class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class EtablissementViewSet(ModelViewSet):
    queryset = Etablissement.objects.all()
    serializer_class = EtablissementSerializer

class SousTraitentViewSet(ModelViewSet):
    queryset = SousTraitent.objects.all()
    serializer_class = SousTraitentSerializer