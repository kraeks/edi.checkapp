# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from plone.autoform import directives
from plone.dexterity.content import Item
from plone.supermodel import model
from plone.supermodel.directives import fieldset
from z3c.form.browser.radio import RadioFieldWidget
from plone import api as ploneapi
from z3c.relationfield.schema import RelationChoice, RelationList
from zope.interface import provider
from plone.autoform import directives as form
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from collective.z3cform.datagridfield import DataGridFieldFactory
from collective.z3cform.datagridfield import DictRow
from plone.app.vocabularies.catalog import CatalogSource
from zope import schema
from zope.interface import implementer
from zope.component import getUtility
from plone.i18n.normalizer.interfaces import IIDNormalizer

dictdefault={'ja':u'', 'unbekannt':u'', 'nein':u''}

listdefault=[
             {u'antwort':u'ja', u'aktion':u'', u'color':u'#555555'},
             {u'antwort':u'unbekannt', u'aktion':u'', u'color':u'#555555'},
             {u'antwort':u'nein', u'aktion':u'', u'color':u'#555555'},
            ]

@provider(IContextSourceBinder)
def possibleQuestionsOrPages(context):
    brains = ploneapi.content.find(portal_type=[u'Hinweistext', u'Frage'])
    terms = []
    if brains:
        for i in brains:
            vocabtitle = "%s (%s)" %(i.Title, i.portal_type)
            terms.append(SimpleVocabulary.createTerm(i.UID, i.UID, vocabtitle))
    return SimpleVocabulary(terms)


@provider(IContextSourceBinder)
def possibleThemen(context):
    terms = []
    normalizer = getUtility(IIDNormalizer)
    themenbereiche = context.themenbereiche
    if themenbereiche:
        for i in themenbereiche:
            mytoken = normalizer.normalize(i)
            terms.append(SimpleVocabulary.createTerm(i,mytoken,i))
    return SimpleVocabulary(terms)

colorterms = [
         SimpleTerm(u'#555555', u'#555555', u'siguv-grau'),
         SimpleTerm(u'#004994', u'#004994', u'siguv-blau'),
         SimpleTerm(u'#0095DB', u'#0095DB', u'siguv-cyan'),
         SimpleTerm(u'#51AE31', u'#51AE31', u'siguv-grün'),
         SimpleTerm(u'#F39200', u'#F39200', u'siguv-orange'),
         SimpleTerm(u'#D40F14', u'#D40F14', u'siguv-rot'),
         SimpleTerm(u'#B80D78', u'#B80D78', u'siguv-violett'),
         SimpleTerm(u'#FFCC00', u'#FFCC00', u'siguv-gelb'),
        ]
SiguvColors = SimpleVocabulary(colorterms)


class IAnswerOptions(model.Schema):
    antwort = schema.TextLine(title=u"Antwortoption")

    aktion = RelationChoice(title=u"Aktion",
                            source=CatalogSource(),
                            required=False)

    color = schema.Choice(title=u"Farbe",
                          source=SiguvColors,
                          required=False)

class IFrage(model.Schema):
    """ Marker interface and Dexterity Python Schema for Frage
    """

    frage = RichText(title=u"Fragestellung",
                     description=u"Bitte bearbeiten Sie hier die Frage für die Checkliste")

    thema = schema.Choice(title=u"Auswahl des Themas für die Frage",
                          source=possibleThemen,
                          required=False)

    form.widget('optionen', DataGridFieldFactory)
    optionen = schema.List(title=u"Antwortoptionen",
                               required=True,
                               value_type=DictRow(title=u"Optionen", schema=IAnswerOptions),
                               default=listdefault)

    tipp = RichText(title=u"Hinweis zur Fragestellung",
                     description=u"Bitte bearbeiten Sie hier einen Hinweis zur Frage")


@implementer(IFrage)
class Frage(Item):
    """
    """
