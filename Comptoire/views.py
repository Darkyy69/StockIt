from django.shortcuts import render
from .models.models_Entite_marchandise import *
from .models.models_documents import *
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

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