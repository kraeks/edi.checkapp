# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from plone.dexterity.content import Item
from plone.supermodel import model
from plone.autoform import directives
from plone import api as ploneapi
from zope.interface import provider
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from plone.app.vocabularies.catalog import CatalogSource
from z3c.relationfield.schema import RelationChoice
from plone.app.z3cform.widget import RelatedItemsFieldWidget
from zope import schema
from zope.interface import implementer
from zope.interface import Invalid
from zope.interface import invariant
from plone.app.multilingual.browser.interfaces import make_relation_root_path

from edi.checkapp import _

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

fieldtypes = [
         SimpleTerm(u'textline', u'textline', u'Textzeile'),
         SimpleTerm(u'number', u'number', u'Zahlenwert'),
         SimpleTerm(u'textarea', u'textarea', u'Textfeld'),
        ]
Feldtypen = SimpleVocabulary(fieldtypes)


@provider(IContextSourceBinder)
def possibleQuestionsOrPages(context):
    try:
        searchcontext = context.aq_parent
        brains = ploneapi.content.find(context=searchcontext, portal_type=[u'Hinweistext', u'Fragestellung'], 
                                       review_state="published")
    except:
        brains = ploneapi.content.find(portal_type=[u'Hinweistext', u'Fragestellung'], review_state="published")
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

    title = schema.TextLine(title=u"Label oder Legende der Antwortoption",
                            description="Bei einfachen Optionen wird diese Angabe als Label verwendet. Werden Zusatzangaben\
                                    zur Antwortoption gefordert, Bsp: ja, im Abstand von 20 Meter kann diese Angabe als Legende\
                                    über der Antwortoption angezeigt werden.")

    showlabel = schema.Bool(title="Legende anzeigen", default=True, required=False,
                            description="Bei zusätzlichen Angaben kann in bestimmten Fällen auf die Legende verzichtet werden.\
                                         In diesen Fällen wird lediglich die Bezeichnung der Zusatzangabe angezeigt.")

    label = schema.TextLine(title="Bezeichnung der Zusatzangabe", required=False)

    platzhalter = schema.TextLine(title=u"Platzhalter für das Eingabefeld", required=False)

    zusatzformat = schema.Choice(title="Feldtyp der zusätzlichen Angabe", required=True,
                            source=Feldtypen, default='textline')    

    einheit = schema.TextLine(title=u"optional: Maßeinheit für Zusatzangabe", required=False)

    xseinheit = schema.TextLine(title=u"optional: Maßeinheit für Zusatzangabe (Kurzform für Smartphone)", 
                                required=False)


    dep_fields = RelationChoice(title=u'Abhängiges Feld',
            description="Bitte wählen Sie hier eine Fragestellung, die dem Benutzer bei Auswahl dieser Option angezeigt\
                    werden soll.",
            vocabulary='plone.app.vocabularies.Catalog',
            required=False,
    )

    directives.widget(
        "dep_fields",
        RelatedItemsFieldWidget,
        pattern_options={
            "selectableTypes": ["Fragestellung"],
            #"basePath": make_relation_root_path,
        },
    )
    
    aktion = schema.Choice(title=u"Aktion",
                           source=possibleQuestionsOrPages,
                           required=False)

    color = schema.Choice(title=u"Farbe",
                          source=SiguvColors,
                          required=False)

    @invariant
    def zusatz_invariant(data):
        if data.einheit:
            if data.zusatzformat != 'number':
                raise Invalid(u"Eine Einheit kann nur bei einem Zahlenwert eingetragen werden.")


@implementer(IAntwortoption)
class Antwortoption(Item):
    """
    """
