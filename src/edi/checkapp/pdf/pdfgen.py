# -*- encoding: utf-8 -*- 
import os.path
import tempfile
from datetime import date
from time import localtime, gmtime, strftime
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import cm
from reportlab.lib.colors import grey, white
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus.frames import Frame
from reportlab.platypus import Table
from reportlab.platypus.flowables import Flowable, Spacer, Image, PageBreak, BalancedColumns
from reportlab.platypus.paragraph import Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_RIGHT as _r
from reportlab.lib.enums import TA_CENTER as _c
from reportlab.platypus.doctemplate import PageTemplate, BaseDocTemplate
from apply import apply

dguvnormal = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'DGUVMeta-Normal.ttf')
dguvbold = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'DGUVMeta-Bold.ttf')

dguvnormal = '/home/bgetem/dienste/src/nva.coronaformulare/src/nva/coronaformulare/pdf/DGUVMeta-Normal.ttf'
dguvbold = '/home/bgetem/dienste/src/nva.coronaformulare/src/nva/coronaformulare/pdf/DGUVMeta-Bold.ttf'

pdfmetrics.registerFont(TTFont('DGUVNormal', dguvnormal))
pdfmetrics.registerFont(TTFont('DGUVBold', dguvbold))

class PdfBaseTemplate(BaseDocTemplate):
    """Basistemplate for PDF-Prints"""

    def __init__(self, filename, **kw):
        frame1 = Frame(1 * cm, 1 * cm, 18.5 * cm, 27 * cm, id='F1', showBoundary=False)
        self.allowSplitting = 0
        apply(BaseDocTemplate.__init__, (self, filename), kw)
        self.addPageTemplates(PageTemplate('normal', [frame1]))

class NumberedCanvas(canvas.Canvas):
    """Add Page number to generated PDF"""

    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        """add page info to each page (page x of y)"""
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_number(self, page_count):
        self.setFont("DGUVBold", 7.5)
        if self._pageNumber < page_count:
            self.drawRightString(19.3 * cm, 1 * cm, "Seite %d von %d" % (self._pageNumber, page_count))
        if self._pageNumber == page_count:
            self.drawRightString(19.3 * cm, 2 * cm, "Seite %d von %d" % (self._pageNumber, page_count))
            self.drawString(9.25 * cm, 2 * cm, "www.bgetem.de")
            self.drawString(1.2 * cm, 2 * cm, "Berufsgenossenschaft")
            self.drawString(1.2 * cm, 1.6 * cm, "Energie Textil Elektro")
            self.drawString(1.2 * cm, 1.2 * cm, "Medienerzeugnisse")


class InteractiveTextField(Flowable):
    def __init__(self, text='A Text', width=210):
        Flowable.__init__(self)
        self.text = text
        self.width = width
        self.height = 20

    def draw(self):
        self.canv.saveState()
        form = self.canv.acroForm
        form.textfield(borderStyle='underlined',
                      name=self.text,
                      width=self.width,
                      fillColor=white,
                      borderWidth=0.5,
                      height=self.height,
                      fieldFlags="richText",
                      fontSize=8,
                      tooltip=self.text,
                      relative=True)
        self.canv.restoreState()
        return


def create_tabelle(tabelle, cols, header, coronastyles):
    styles = coronastyles
    colWidths = cols

    mytable = []

    if header:
        tableheader = []
        for i in header:
            tableheader.append(Paragraph(i, styles['entry_bold']))
        mytable.append(tableheader)

    count = 0
    for zeile in tabelle:
        row = []
        for spalte in zeile:
            row.append(Paragraph(spalte, styles['entry_normal']))
        mytable.append(row)

    table = Table(mytable, repeatRows=1, colWidths=colWidths, style=[('GRID', (0, 0), (-1, -1), 1, grey),
                                                                     ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')])

    table.hAlign = "LEFT"
    return table


def createpdf(filehandle, data):
    """Funktion zum Schreiben der PDF-Datei"""

    story = []  # Alle Elemente des PDFs werden der Story hinzugefuegt

    # Styles fuer normale Paragraphen, gelesen aus dem SampleStyleSheet
    stylesheet = getSampleStyleSheet()

    h1 = stylesheet['Heading1']
    h1.fontname = 'DGUVBold'

    h2 = stylesheet['Heading2']
    h2.fontName = 'DGUVBold'

    h3 = stylesheet['Heading3']
    h3.fontname = 'DGUVBold'

    code = stylesheet['Code']

    bodytext = stylesheet['BodyText']
    bodytext.fontName = 'DGUVNormal'

    bodybold = stylesheet['BodyText']
    bodybold.fontName = 'DGUVBold'

    # Weitere Styles fuer Paragraphen
    stylesheet.add(ParagraphStyle(name='smallbody', fontName='DGUVNormal', fontSize=9, spaceAfter=5))
    stylesheet.add(ParagraphStyle(name='normal', fontName='DGUVNormal', fontSize=7.5, borderPadding=(5, 3, 3, 5)))
    stylesheet.add(ParagraphStyle(name='free', fontName='DGUVNormal', fontSize=7.5, borderPadding=0))
    stylesheet.add(ParagraphStyle(name='right', fontName='DGUVNormal', fontSize=7.5, borderPadding=(5, 3, 3, 5), alignment=_r))
    stylesheet.add(ParagraphStyle(name='center', fontName='DGUVNormal', fontSize=7.5, borderPadding=(5, 3, 3, 5), alignment=_c))
    stylesheet.add(ParagraphStyle(name='bold', fontName='DGUVBold', fontSize=7.5, borderPadding=(5, 3, 3, 5)))
    stylesheet.add(ParagraphStyle(name='boldnew', fontName='DGUVBold', fontSize=9, borderPadding=(5, 3, 3, 5)))
    stylesheet.add(ParagraphStyle(name='boldright', fontName='DGUVBold', fontSize=7.5, borderPadding=(5, 3, 3, 5), alignment=_r))
    stylesheet.add(ParagraphStyle(name='boldcenter', fontName='DGUVBold', fontSize=7.5, borderPadding=(5, 3, 3, 5), alignment=_c))

    smallbody = stylesheet['smallbody']
    bullet = stylesheet['Bullet']
    bullet.fontSize=9
    bullet.fontName='DGUVNormal'
    entry_normal = stylesheet['normal']
    entry_free = stylesheet['free']
    entry_right = stylesheet['right']
    entry_center = stylesheet['center']
    entry_bold = stylesheet['bold']
    entry_boldnew = stylesheet['boldnew']
    entry_boldright = stylesheet['boldright']
    entry_boldcenter = stylesheet['boldcenter']

    coronastyles = {}
    coronastyles['h1'] = h1
    coronastyles['h2'] = h2
    coronastyles['h3'] = h3
    coronastyles['code'] = code
    coronastyles['bodytext'] = bodytext
    coronastyles['bodybold'] = bodybold
    coronastyles['smallbody'] = smallbody
    coronastyles['bullet'] = bullet
    coronastyles['entry_normal'] = entry_normal
    coronastyles['entry_free'] = entry_free
    coronastyles['entry_right'] = entry_right
    coronastyles['entry_center'] = entry_center
    coronastyles['entry_bold'] = entry_bold
    coronastyles['entry_boldnew'] = entry_boldnew
    coronastyles['entry_boldright'] = entry_boldright
    coronastyles['entry_boldcenter'] = entry_boldcenter

    im = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images/logo_etem.jpg')
    logo = Image(im)
    logo.drawHeight = 6 * cm * logo.drawHeight / logo.drawWidth
    logo.drawWidth = 6 * cm
    logo.hAlign = 'RIGHT'

    # Datum
    datum = u"Datum: %s" % (strftime("%d.%m.%Y"))
    zeit = u"Zeit: %s" % (strftime("%H:%M:%S", localtime()))

    colWidths = [9.5*cm, 2.75*cm, 6.25*cm]
    formtitle = data.get('fragebogenName')
    testheadline = u'<font color="#008c8e"><b>%s</b></font>' % formtitle
    toptable = [[Paragraph(testheadline, h2), Paragraph(u" ", bodytext), logo]]
    table = Table(toptable, colWidths=colWidths, style=[('VALIGN', (0, 0), (-1, -1), 'TOP')])
    table.hAlign = 'CENTER'
    story.append(table)
    story.append(Spacer(0 * cm, 0.5 * cm))

    textbox_name = InteractiveTextField('Name', 250)
    textbox_datum = InteractiveTextField('Datum', 250)
    textbox_unternehmer = InteractiveTextField('Bearbeiter', 250)

    story.append(Paragraph(u"Firma", entry_free))
    story.append(textbox_name)
    story.append(Spacer(0 * cm, 0.1 * cm))
    story.append(Paragraph(u"Datum", entry_free))
    story.append(textbox_datum)
    story.append(Spacer(0 * cm, 0.1 * cm))
    story.append(Paragraph(u"Name des Bearbeiters", entry_free))
    story.append(textbox_unternehmer)

    story.append(Spacer(0 * cm, 0.5 * cm))

    story.append(Paragraph(u"Ihre Daten zur Maschine", h2))
    tabelle = list()
    cols = [6*cm, 6*cm]
    header = []
    tabelle.append(['Maschinentyp', data.get('maschinentyp')])
    tabelle.append(['Maschinennummer', data.get('maschinennummer')])
    tabelle.append(['Hersteller', data.get('hersteller')])
    tabelle.append(['Dateiname', data.get('dateiname')])
    story.append(create_tabelle(tabelle, cols, header, coronastyles))

    story.append(Spacer(0 * cm, 1 * cm))
    
    story.append(Paragraph(u"Ihre Antworten zur Checkliste", h2))
    tabelle = data.get('tabelle')
    cols = [6*cm, 3*cm, 2*cm, 5*cm]
    header = [u'Frage', u'Kategorie', u'Antwort', u'Notiz']
    story.append(create_tabelle(tabelle, cols, header, coronastyles))

    story.append(PageBreak())
    story.append(Spacer(0 * cm, 1 * cm))
    story.append(Paragraph(u"Ihre Notizen zur Checkliste", h2))
    notizen = data.get('globaleNotizen')
    if not notizen:
        notizen  = ''
    story.append(Paragraph(notizen, bodytext))
    story.append(Spacer(0 * cm, 0.5 * cm))
    story.append(InteractiveTextField('massnahme1', 500))
    story.append(InteractiveTextField('massnahme2', 500))
    story.append(InteractiveTextField('massnahme3', 500))
    story.append(InteractiveTextField('massnahme4', 500))
    story.append(InteractiveTextField('massnahme5', 500))
    story.append(InteractiveTextField('massnahme6', 500))
    story.append(InteractiveTextField('massnahme7', 500))
    story.append(InteractiveTextField('massnahme8', 500))

    story.append(Spacer(0 * cm, 14 * cm))
    schlusstext = u"""Diese Checkliste ergänzt die betriebliche Gefährdungsbeurteilung."""
    schlussline = u'<font color="#008c8e"><b>%s</b></font>' % schlusstext
    story.append(Paragraph(schlussline, bodybold))

    story.append(Spacer(0 * cm, 0.5 * cm))

    textbox_name = InteractiveTextField('name_verantwortlich', 250)
    textbox_unterschrift = InteractiveTextField('datum_unterschrift', 250)
    colWidths = [9.25*cm, 9.25*cm]
    signtable = [[textbox_name, textbox_unterschrift],
                 [Paragraph(u"Name des Bearbeiters", entry_free),
                  Paragraph(u"Datum, Unterschrift", entry_free)]
                ]
    table = Table(signtable, colWidths=colWidths)
    table.hAlign = 'CENTER'
    story.append(table)

    story.append(Spacer(0 * cm, 1 * cm))

    doc = PdfBaseTemplate(filehandle, pagesize=A4)
    doc.build(story, canvasmaker=NumberedCanvas)
