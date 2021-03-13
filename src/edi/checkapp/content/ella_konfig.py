# -*- coding: utf-8 -*-
from plone.app.vocabularies.catalog import CatalogSource
from z3c.relationfield.schema import RelationChoice
from z3c.relationfield.schema import RelationList
from plone.app.z3cform.widget import RelatedItemsFieldWidget
from plone.app.textfield import RichText
from plone.namedfile.field import NamedBlobImage
from plone.autoform import directives
from plone.dexterity.content import Container
from plone.supermodel import model
from zope import schema
from zope.interface import implementer
from plone.app.multilingual.browser.interfaces import make_relation_root_path


from edi.checkapp import _


default_template = \
"""<div class="card mb-3">
     <img src="{{ ella_image }}" class="card-img-top" alt="Titelbild der App">
     <div class="card-body">
       <h5 class="card-title">{{ ella_title }}</h5>
       {{ ella_bodytext }}
     </div>
   </div>""" 
   
class IEllaKonfig(model.Schema):
    """ Marker interface and Dexterity Python Schema for EllaKonfig
    """
    bodytemplate = schema.Text(title="HTML-Template der Startseite",
            default = default_template,
            description="Das Template kann die Jinja-Variablen {{ella_title }}, {{ ella_bodytext }} und {{ ella_image }} enthalten.")

    bodytext = RichText(title=u"Konfiguration einer der Ella-App", required=False)

    image = NamedBlobImage(title=u"Titelbild der Startseite", required=False)

    startseiten = RelationList(
            title=u"Alternativ: Referenz auf eine oder mehrere Startseiten",
            description="Referenzieren Sie hier eine oder mehrere Startseiten. Mehrere Startseiten werden als Tour angezeigt.",
            default=[],
            value_type=RelationChoice(vocabulary='plone.app.vocabularies.Catalog'),
            required=False)

    directives.widget(
        "startseiten",
            RelatedItemsFieldWidget,
            vocabulary='plone.app.vocabularies.Catalog',
            pattern_options={
                "basePath": make_relation_root_path,
                "selectableTypes": ["News Item", "Document"]}) 

    groupname = schema.TextLine(title=u"Name und Titel der Ella-Gruppe",
            description = u"Muss eingesetzt werden, wenn mehrere Startseiten konfiguriert werden. Schreibweise: Name#Titel", required=False)


@implementer(IEllaKonfig)
class EllaKonfig(Container):
    """
    """
