from rest_framework.viewsets import ModelViewSet
from ...models.models_stock import *
from ..serializers import StockSerializer, MvtStockSerializer


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

class MvtStockViewSet(ModelViewSet):
    queryset = MvtStock.objects.all()
    serializer_class = MvtStockSerializer