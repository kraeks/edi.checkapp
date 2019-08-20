# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from plone.autoform import directives
from plone.dexterity.content import Item
from plone.supermodel import model
from plone.supermodel.directives import fieldset
from z3c.form.browser.radio import RadioFieldWidget
from plone import api as ploneapi
from z3c.relationfield.schema import RelationChoice, RelationList
from plone.app.vocabularies.catalog import CatalogSource
from zope.interface import provider
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary
from zope import schema
from zope.interface import implementer
from zope.component import getUtility
from plone.i18n.normalizer.interfaces import IIDNormalizer

dictdefault={'ja':u'', 'unbekannt':u'', 'nein':u''}

@provider(IContextSourceBinder)
def possibleQuestionsOrPages(context):
    brains = ploneapi.content.find(portal_type=[u'Document', u'Frage'])
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


class IFrage(model.Schema):
    """ Marker interface and Dexterity Python Schema for Frage
    """

    frage = RichText(title=u"Fragestellung",
                     description=u"Bitte bearbeiten Sie hier die Frage für die Checkliste")

    thema = schema.Choice(title=u"Auswahl des Themas für die Frage",
                          source=possibleThemen,
                          required=False)

    optionen = schema.Dict(title=u"Anwortoptionen",
                           key_type=schema.TextLine(title=u"Antwort"),
                           value_type=schema.Choice(title=u"Nächste Aktion",
                                                    description=u"Ohne Auswahl wird die nächste Frage der Liste angezeigt",
                                                    source=possibleQuestionsOrPages,
                                                    required=False),
                           default=dictdefault,
                           )


    farbe = schema.Bool(title=u"Hier markieren, wenn die Antwortoptionen im Farbschema dargestellt werden sollen")


@implementer(IFrage)
class Frage(Item):
    """
    """
