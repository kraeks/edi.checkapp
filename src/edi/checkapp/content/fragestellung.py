# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
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
         SimpleTerm(u'radio', u'radio', u'Auswahl (bitte Antwortoptionen hinzufügen)'),
         SimpleTerm(u'checkbox', u'checkbox', u'Mehrfachauswahl (bitte Antwortoptionen hinzufügen)'),
         SimpleTerm(u'number', u'number', u'Zahlenwert'),
         SimpleTerm(u'text', u'text', u'Textzeile'),
         SimpleTerm(u'textarea', u'textarea', u'Textfeld'),
        ]
Antworttypen = SimpleVocabulary(answertypes)


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
                mytoken = normalizer.normalize(thema)
                terms.append(SimpleVocabulary.createTerm(thema,mytoken,thema))
            else:    
                terms.append(SimpleVocabulary.createTerm(i,mytoken,i))
    return SimpleVocabulary(terms)


class IFragestellung(model.Schema):
    """ Marker interface and Dexterity Python Schema for Frage
    """

    title = schema.TextLine(title=u"Titel der Fragestellung",
                            description=u"Geben Sie hier Ihre Frage ein.")

    thema = schema.Choice(title=u"Auswahl des Themas für die Frage",
                          source=possibleThemen,
                          required=False)

    frage = RichText(title=u"Formatierte Fragestellung",
                     description=u"Alternativ können Sie hier eine formatierte Fragestellung für die Checkliste eingeben.",
                     required=False)

    antworttyp = schema.Choice(title=u"Wählen Sie eine Art der Antwort aus.",
                     source = Antworttypen,
                     default = 'radio')

    einheit = schema.TextLine(title=u"Einheit der Antwort (nur bei Ganzzahl oder Gleitkommazahl)",
                     description = u"Sie können hier eine Einheit für die Antwort angeben (z.B.: Ohm, Ampere, Volt)",
                     required=False)

    notiz = schema.Bool(title=u"Notizenfeld anbieten",
                        description=u"Anklicken wenn Sie eine Notiz zu dieser Fragestellung erlauben wollen.")

    tipp = RichText(title=u"Hinweis zur Fragestellung",
                     description=u"Bitte bearbeiten Sie hier einen Hinweis zur Frage",
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
