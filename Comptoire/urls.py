from django.urls import path, include
from .views import comptoire_view, print_article

urlpatterns = [
    path('', comptoire_view, name='comptoire'),
    path('article/<int:article_id>/', print_article, name='print_article'),
    path('enregistrer/<int:modeFen>/<int:doc>', trait_enregistrer, name='trait_enregistrer'),
]