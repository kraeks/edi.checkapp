# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from plone.autoform import directives
from plone.dexterity.content import Item, Container
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
from z3c.form.interfaces import NOVALUE
from zope import schema
from zope.interface import implementer
from zope.component import getUtility
from plone.i18n.normalizer.interfaces import IIDNormalizer
from zope.interface import implementer, alsoProvides
from plone.autoform.interfaces import IFormFieldProvider
from zope.schema.fieldproperty import FieldProperty

dictdefault={'ja':u'', 'unbekannt':u'', 'nein':u''}

listdefault=[
             {u'antwort':u'ja', u'aktion':None, u'color':u'#51AE31'},
             {u'antwort':u'unbekannt', u'aktion':None, u'color':u'#F39200'},
             {u'antwort':u'nein', u'aktion':None, u'color':u'#D40F14'},
            ]

@provider(IContextSourceBinder)
def possibleQuestionsOrPages(context):
    print('Fragen')
    print(context)
    brains = ploneapi.content.find(portal_type=[u'Hinweistext', u'Frage'], review_state="published")
    terms = []
    if brains:
        for i in brains:
            obj = i.getObject()
            fragebogen = obj.fbid
            vocabtitle = "%s-%s (%s)" %(fragebogen, i.Title, i.portal_type)
            terms.append(SimpleVocabulary.createTerm(i.UID, i.UID, vocabtitle))
    terms.sort(key=lambda x: x.title)
    return SimpleVocabulary(terms)        



@provider(IContextSourceBinder)
def possibleThemen(context):
    print('Themen')
    print(context)
    terms = []
    normalizer = getUtility(IIDNormalizer)
    themenbereiche = context.themenbereiche
    if themenbereiche:
        for i in themenbereiche:
            mytoken = normalizer.normalize(i)
            terms.append(SimpleVocabulary.createTerm(i,mytoken,i))
    return SimpleVocabulary(terms)

colorterms = [
         SimpleTerm(u'#555555', u'secondary', u'siguv-grau'),
         SimpleTerm(u'#004994', u'primary', u'siguv-blau'),
         SimpleTerm(u'#0095DB', u'info', u'siguv-cyan'),
         SimpleTerm(u'#51AE31', u'success', u'siguv-grün'),
         SimpleTerm(u'#F39200', u'warning', u'siguv-orange'),
         SimpleTerm(u'#D40F14', u'danger', u'siguv-rot'),
         SimpleTerm(u'#B80D78', u'dark', u'siguv-violett'),
         SimpleTerm(u'#FFCC00', u'light', u'siguv-gelb'),
        ]
SiguvColors = SimpleVocabulary(colorterms)


class IAnswers(model.Schema):
    antwort = schema.TextLine(title=u"Antwortoption", required=True)

    #aktion = schema.Choice(title=u"Aktion",
    #                       source=possibleQuestionsOrPages,
    #                       required=False)

    #color = schema.Choice(title=u"Farbe",
    #                      source=SiguvColors,
    #                      required=False)


@implementer(IAnswers)
class Answer(object):
    """
    """    
    antwort = FieldProperty(IAnswers['antwort'])

from z3c.form.object import registerFactoryAdapter
registerFactoryAdapter(IAnswers, Answer)
    

class IFragestellung(model.Schema):
    """ Marker interface and Dexterity Python Schema for Frage
    """

    fbid = schema.TextLine(title=u"Kürzel oder Nummer des Fragebogens")

    frage = RichText(title=u"Fragestellung",
                     description=u"Bitte bearbeiten Sie hier die Frage für die Checkliste")

    thema = schema.Choice(title=u"Auswahl des Themas für die Frage",
                          source=possibleThemen,
                          required=False)

    optionen = schema.List(title=u"Antwortoptionen",
                               required=True,
                               value_type=schema.Object(IAnswers),)

    tipp = RichText(title=u"Hinweis zur Fragestellung",
                     description=u"Bitte bearbeiten Sie hier einen Hinweis zur Frage",
                     required=False)

    

@implementer(IFragestellung)
class Fragestellung(Container):
    """
    """
