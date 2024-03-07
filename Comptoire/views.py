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


from Comptoire.models.models_documents import *
def test_method(request):
    cmd2 = BonCMD.objects.get(pk="2")
    print(cmd2)
    print(cmd2.verifierDocument())

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