from rest_framework.viewsets import ModelViewSet
from ...models.models_Entite_marchandise import *
from ..serializers import FamilleSerializer, S_familleSerializer, S_articleSerializer, ArticleSerializer



class FamilleViewSet(ModelViewSet):
    queryset = Famille.objects.all()
    serializer_class = FamilleSerializer

class S_familleViewSet(ModelViewSet):
    queryset = S_famille.objects.all()
    serializer_class = S_familleSerializer

class S_articleViewSet(ModelViewSet):
    queryset = S_article.objects.all()
    serializer_class = S_articleSerializer

class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer