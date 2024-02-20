from django.urls import path, include
from .views import comptoire_view, import_articles_from_txt

urlpatterns = [
    # path('api/', ), 
    path('', comptoire_view, name='comptoire'),
    path('abc/', import_articles_from_txt, name='ssss'),
]
