# -*- coding: utf-8 -*-
#Import der benoetigten Bibliotheken
from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, mm
from time import gmtime, strftime
from reportlab.graphics.barcode import code39
from reportlab.lib.colors import gray
from reportlab.lib.utils import ImageReader

def createpdf(filehandle):
    """
    Schreibt eine PDF-Datei
    """

    #Pfad und Dateiname
    timestamp=datetime.now().strftime("%d%m%Y%H%M%S")

    #c ist ein Objekt der Klasse Canvas
    c = canvas.Canvas(filehandle,pagesize=A4)

    #Metainformationen fuer das PDF-Dokument
    c.setAuthor(u"educorvi GmbH & Co. KG")
    c.setTitle(u"Checkliste Sicher investieren")

    #Variablen 
    schriftart = "Helvetica"
    schriftartfett = "Helvetica-Bold"
    datum = datetime.now().strftime("%d.%m.%Y")

    c.setFont(schriftart, 12)
    c.drawString(5*cm, 20*cm, 'Hallo')
    c.drawString(5*cm, 19*cm, 'Welt')

    c.showPage()
    c.save()
    return filehandle
