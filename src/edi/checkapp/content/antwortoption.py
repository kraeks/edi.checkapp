# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from plone.dexterity.content import Item
from plone.supermodel import model
from plone import api as ploneapi
from zope.interface import provider
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope import schema
from zope.interface import implementer
from zope.interface import implementer

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

@provider(IContextSourceBinder)
def possibleQuestionsOrPages(context):
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


class IAntwortoption(model.Schema):

    title = schema.TextLine(title=u"Antwortoption (Label)")

    showlabel = schema.Bool(title="Label anzeigen/ausblenden" default=True, required=False)

    zusatz = schema.Bool(title=u"Zusatzangabe ein-/ausschalten", required=False)

    label = schema.TextLine(title="Bezeichnung der Zusatzangabe", required=False)

    einheit = schema.TextLine(title=u"optional: Maßeinheit für Zusatzangabe", required=False)

    aktion = schema.Choice(title=u"Aktion",
                           source=possibleQuestionsOrPages,
                           required=False)

    color = schema.Choice(title=u"Farbe",
                          source=SiguvColors,
                          required=False)

@implementer(IAntwortoption)
class Antwortoption(Item):
    """
    """
