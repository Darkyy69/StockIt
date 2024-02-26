from rest_framework.viewsets import ModelViewSet
from ...models.models_remise import *
from ..serializers import RemiseFournisseurSerializer, RemiseClientSerializer, RemiseEtablissementSerializer, RemiseSousTraitentSerializer

class RemiseFournisseurViewSet(ModelViewSet):
    queryset = RemiseFournisseur.objects.all()
    serializer_class = RemiseFournisseurSerializer

class RemiseClientViewSet(ModelViewSet):
    queryset = RemiseClient.objects.all()
    serializer_class = RemiseClientSerializer

class RemiseEtablissementViewSet(ModelViewSet):
    queryset = RemiseEtablissement.objects.all()
    serializer_class = RemiseEtablissementSerializer

class RemiseSousTraitentViewSet(ModelViewSet):
    queryset = RemiseSousTraitent.objects.all()
    serializer_class = RemiseSousTraitentSerializer