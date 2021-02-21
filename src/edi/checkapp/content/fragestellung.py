# -*- coding: utf-8 -*-
import hashlib
from plone.app.textfield import RichText
from z3c.form.browser.radio import RadioFieldWidget
from plone.autoform import directives
from plone.dexterity.content import Container
from plone.supermodel import model
from plone import api as ploneapi
from zope.interface import provider
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope import schema
from zope.interface import implementer
from zope.component import getUtility
from plone.i18n.normalizer.interfaces import IIDNormalizer
from zope.interface import Invalid
from zope.interface import invariant

answertypes = [
         SimpleTerm(u'radio', u'radio', u'Radiobutton (Einfachauswahl)'),
         SimpleTerm(u'checkbox', u'checkbox', u'Checkboxen (Mehrfachauswahl)'),
         SimpleTerm(u'number', u'number', u'Zahlenwert'),
         SimpleTerm(u'text', u'text', u'Textzeile'),
         SimpleTerm(u'textarea', u'textarea', u'Textfeld'),
        ]
Antworttypen = SimpleVocabulary(answertypes)

direction = [
        SimpleTerm(u'left', u'left', u'linksbündig'),
        SimpleTerm(u'right', u'right', u'rechtsbündig'),
        ]
Direction = SimpleVocabulary(direction)

labelclass = [
         SimpleTerm(u'label', u'label', u'Label'),
         SimpleTerm(u'edi__checkapp', u'edi__checkapp', u'Legende'),
         ]
Labelclass = SimpleVocabulary(labelclass)



@provider(IContextSourceBinder)
def possibleThemen(context):
    terms = []
    normalizer = getUtility(IIDNormalizer)
    try:
        themenbereiche = context.themenbereiche
    except:
        themenbereiche = []
    if themenbereiche:
        for i in themenbereiche:
            if '#' in i:
                thema = i.split('#')[1]
                m = hashlib.sha256()
                m.update(thema.encode('utf-8'))
                mytoken = m.hexdigest()
                terms.append(SimpleVocabulary.createTerm(thema,mytoken,thema))
            else:    
                terms.append(SimpleVocabulary.createTerm(i,mytoken,i))
    return SimpleVocabulary(terms)


class IFragestellung(model.Schema):
    """ Marker interface and Dexterity Python Schema for Frage
    """

    title = schema.TextLine(title=u"Titel der Fragestellung")

    #directives.widget(fieldclass=RadioFieldWidget)
    fieldclass = schema.Choice(title="Wie soll der Titel der Fragestellung angezeigt werden?", 
                               vocabulary=Labelclass,
                               default='edi__checkapp')

    thema = schema.Choice(title=u"Auswahl des Themas für die Frage",
                          source=possibleThemen,
                          required=True)

    frage = RichText(title=u"Formatierte Fragestellung",
                     description=u'Die Inhalte dieses Feldes (Texte, Bilder, etc.) ersetzen die Angabe im Feld\
                                   "Titel der Fragestellung".',
                     required=False)

    antworttyp = schema.Choice(title=u"Antworttyp auswählen",
                     description = u"Bei Radiobutton und Checkboxen müssen nach Speichern der Fragestellung Antwortoptionen\
                                     hinzugefügt werden.",
                     source = Antworttypen,
                     default = 'radio')

    platzhalter = schema.TextLine(title=u'Platzhalter (nur bei Antworttypen "Textzeile" oder "Text")', required=False)

    ausrichtung = schema.Choice(title=u"Ausrichtung auswählen",
                     source=Direction,
                     default=u'left',
                     required=True)

    einheit = schema.TextLine(title=u"Einheit der Antwort (nur bei Antworttyp Zahlenwert möglich)",
                     description = u"Sie können hier eine Einheit für die Antwort angeben (z.B.: Ohm, Ampere, Volt)",
                     required=False)

    required = schema.Bool(title=u"Markieren falls die Fragestellung eine Pflichtfeld darstellt.", default=True)

    notiz = schema.Bool(title=u"Notizenfeld anbieten",
                        description=u"Anklicken wenn Sie eine Notiz zu dieser Fragestellung erlauben wollen.")

    tipp = RichText(title=u"Hinweis oder Hilfe zur Fragestellung",
                     required=False)

    @invariant
    def einheit_invariant(data):
        if data.einheit:
            if data.antworttyp != 'number':
                raise Invalid(u"Bei Angabe von Einheiten muss der Antworttyp Zahlenwert ausgewählt werden.")

    
@implementer(IFragestellung)
class Fragestellung(Container):
    """
    """
