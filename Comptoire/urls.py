from django.urls import path, include
from .views import comptoire_view, print_article, trait_enregistrer, test_method

urlpatterns = [
    path('', comptoire_view, name='comptoire'),
    path('article/<int:article_id>/', print_article, name='print_article'),
    path('testMethod/', test_method, name='test_method'),
    path('enregistrer/<int:modeFen>/<int:doc>', trait_enregistrer, name='trait_enregistrer'),
]