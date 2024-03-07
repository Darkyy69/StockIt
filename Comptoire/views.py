from django.shortcuts import render
from .models.models_Entite_marchandise import *
from .models.models_documents import *
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
import json

from io import BytesIO
from barcode import EAN13  # Choose appropriate barcode type
import barcode
from reportlab.graphics import renderPDF
from svglib.svglib import svg2rlg  # svglib for parsing SVG to reportlab graphics
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


from django.apps import apps
from Comptoire.models.models_ligneDocument import *

# Create your views here.

def comptoire_view(request):
    Articles = Article.objects.all()

    return render(request,'comptoire.html', {'Articles':Articles})


def trait_enregistrer(request, modeFen, doc):
    
    data = json.loads(request.body)
    
    match modeFen:
        case '001': # Vente
            match doc:
                case '001': # FactureProformat
                    pass
                case '002': # Facture
                    pass
                case '003': # FactureAvoir
                    pass  
                case '004': # BonArtOut
                    pass
                case '005': # BonLivraison
                    pass    



        case '002': # Achat
            match doc:
                case '001': # BonCMD
                    pass
                case '002': # BonArtIn
                    pass
                case '003': # BonArtOut   
                    pass         


        case '003': # Etablissement
            match doc:
                case '001': # BonTransfert
                    pass
                case '002': # BonRecuperation
                    pass
                case '003': # BonTranzition   
                    pass                              

def getClientFactures(self):
    Factures_propreot = self.__class__.objects.filter(propretaire = self.propretaire)      
    print(Factures_propreot)
    T_mont = 0.0
    T_ligne_mont = 0.0
    for fact_propreot in  Factures_propreot:
        T_mont += fact_propreot.montant
        ligneFactures = LigneFacture.objects.filter(id_doc = fact_propreot.id)
        for ligne_fact in ligneFactures:
            T_ligne_mont += ligne_fact.montant

    total = {T_mont,T_ligne_mont}
    return total

def verifierDocument(self):
    modelName = "Ligne" + self.__class__.__name__
    
    # Get the model class dynamically
    model_class = apps.get_model('Comptoire', modelName)        
    ligneDocuments = model_class.objects.filter(id_doc=self.id)
    total = 0.0

    for ligneDoc in ligneDocuments:
        total += float(ligneDoc.montant) 

    if total == self.montant:
        return True
    
    # Traitement si le montant != total
    #
    #
    return False





from Comptoire.models.models_documents import *
def test_method(request):
    cmd2 = BonCMD.objects.get(pk="2")
    fact1 = Facture.objects.get(pk="1")
    print(cmd2)
    print(cmd2.verifierDocument())
    print(fact1.getClientFactures())

    return render(request,'test_method.html', {"montant_egal" : cmd2.verifierDocument()})



def print_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)

    # Generate barcode
    barcode_value = article.barrcode
    if barcode_value:
        barcode_instance = EAN13(barcode_value)
        # Save barcode as SVG to a BytesIO object
        buffer = BytesIO()
        barcode_instance.write(buffer, options={'module_width': 0.2, 'module_height': 15, 'quiet_zone': 6})
        buffer.seek(0)

        # Parse SVG to reportlab graphics
        drawing = svg2rlg(buffer)

        # Convert reportlab graphics to PDF
        pdf_buffer = BytesIO()
        c = canvas.Canvas(pdf_buffer, pagesize=letter)

        # Draw barcode
        renderPDF.draw(drawing, c, 100, 700)

        # Add additional information
        c.drawString(100, 650, "Article Disignation: {}".format(article.disignation))
        c.drawString(100, 630, "Article ID: {}".format(article.id))
        # Add more information as needed

        # Save the PDF
        c.save()

        # Return PDF as HttpResponse
        response = HttpResponse(pdf_buffer.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="barcode-article-'+str(article_id)+'.pdf"'
        return response
    else:
        return HttpResponse("Barcode value is not available for this article.")