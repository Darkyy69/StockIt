from rest_framework.viewsets import ModelViewSet
from ...models.models_info_extra import *
from ..serializers import TypePayementSerializer, TypeClientSerializer, EtatsClientSerializer, EtatoperationsSerializer, LiseEtatSortieSerializer

class TypePayementViewSet(ModelViewSet):
    queryset = TypePayement.objects.all()
    serializer_class = TypePayementSerializer

class TypeClientViewSet(ModelViewSet):
    queryset = TypeClient.objects.all()
    serializer_class = TypeClientSerializer

class EtatsClientViewSet(ModelViewSet):
    queryset = EtatsClient.objects.all()
    serializer_class = EtatsClientSerializer

class EtatoperationsViewSet(ModelViewSet):
    queryset = Etatoperations.objects.all()
    serializer_class = EtatoperationsSerializer

class LiseEtatSortieViewSet(ModelViewSet):
    queryset = LiseEtatSortie.objects.all()
    serializer_class = LiseEtatSortieSerializer