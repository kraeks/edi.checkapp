# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from plone.autoform import directives
from plone.dexterity.content import Container
from plone.supermodel import model
from zope import schema
from plone.app.z3cform.widget import RelatedItemsFieldWidget
from zope.interface import implementer
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary
from plone.app.multilingual.browser.interfaces import make_relation_root_path

from edi.checkapp import _

servicetyp = SimpleVocabulary((
    SimpleTerm(value='service', token='service', title='Formular/Checkliste'),
    SimpleTerm(value='page', token='page', title='Seite'),
    SimpleTerm(value='group', token='group', title='Gruppe von Formularen oder Seiten')
    ))

class IService(model.Schema):
    """ Marker interface and Dexterity Python Schema for Service
    """
    
    servicetyp = Choice(title=u"Servicetyp", default='service', vocabulary=servicetyp)

    serviceref = RelationChoice(title="Referenz auf das Formular, die Checkliste oder Seite",
            vocabulary='plone.app.vocabularies.Catalog',
            required=False)

    directives.widget(
        "serviceref",
        RelatedItemsFieldWidget,
        pattern_options={
            "basePath": make_relation_root_path,
            "selectableTypes": ["Fragebogen"],
        },


@implementer(IService)
class Service(Container):
    """
    """
