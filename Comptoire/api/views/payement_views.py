from rest_framework.viewsets import ModelViewSet
from ...models.models_payement import *
from ..serializers import PayementFournisseurSerializer, PayementClientSerializer, PayementSousTraitantSerializer, PayementEtablissementSerializer

class PayementFournisseurViewSet(ModelViewSet):
    queryset = PayementFournisseur.objects.all()
    serializer_class = PayementFournisseurSerializer

class PayementClientViewSet(ModelViewSet):
    queryset = PayementClient.objects.all()
    serializer_class = PayementClientSerializer

class PayementSousTraitantViewSet(ModelViewSet):
    queryset = PayementSousTraitant.objects.all()
    serializer_class = PayementSousTraitantSerializer

class PayementEtablissementViewSet(ModelViewSet):
    queryset = PayementEtablissement.objects.all()
    serializer_class = PayementEtablissementSerializer