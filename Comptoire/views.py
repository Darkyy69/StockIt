from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404
# Create your views here.

def comptoire_view(request):
    Articles = Article.objects.all()

    return render(request,'comptoire.html', {'Articles':Articles})

import csv
from Comptoire.models import Article  # Replace 'myapp' with the actual name of your Django app

def import_articles_from_txt(request):
    file_path = "C:\\Users\\nouchka\\Desktop\\listeArt.txt"
    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            barrcode, designation, P_vente = row
            print(barrcode)
            # Assuming you have S_famille and S_article instances, replace them with your actual ForeignKey values
            article = Article(
                id_S_famille=1,
                id_S_article=1,
                codif='',  # Provide a value for codif, or adjust the model accordingly
                disignation=designation,
                P_achat=0.0,  # Provide a value for P_achat, or adjust the model accordingly
                P_vente=float(P_vente),
                P_min=0.0,  # Provide a value for P_min, or adjust the model accordingly
                barrcode=barrcode,
                fournisseur_best=0  # Provide a value for fournisseur_best, or adjust the model accordingly
            )
            article.save()
