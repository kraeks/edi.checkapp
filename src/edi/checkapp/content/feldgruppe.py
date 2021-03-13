# -*- coding: utf-8 -*-
from plone.dexterity.content import Container
from plone.supermodel import model
from zope import schema
from zope.interface import implementer

from edi.checkapp import _

from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

fieldsetlook = SimpleVocabulary((
    SimpleTerm(value=u"block", token=u"block", title=u"Feldgruppe mit Zwischen-Überschrift"),
    SimpleTerm(value=u"accordeon", token=u"accordeon", title=u"Akkordeon")
    ))



class IFeldgruppe(model.Schema):
    """ Marker interface and Dexterity Python Schema for Feldgruppe
    """

    fieldsets = schema.Choice(title="Darstellung der Feldgruppe",
            required = True,
            vocabulary = fieldsetlook)

@implementer(IFeldgruppe)
class Feldgruppe(Container):
    """
    """
