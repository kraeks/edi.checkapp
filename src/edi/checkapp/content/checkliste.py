# -*- coding: utf-8 -*-
# from plone.app.textfield import RichText
# from plone.autoform import directives
from plone.dexterity.content import Item
# from plone.namedfile import field as namedfile
from plone.supermodel import model
# from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import implementer


# from edi.checkapp import _


class ICheckliste(model.Schema):
    """ Marker interface and Dexterity Python Schema for Checkliste
    """

    maschnr = schema.TextLine(title=u"Maschinen-Nummer", required=False)

    hersteller = schema.TextLine(title=u"Hersteller der Maschine", required=False)

    fragebogen = schema.TextLine(title=u"ID des Frageboges", required=True)

    fortschritt = schema.Float(title=u"Fortschritt des Fragebogens", required=False)

    daten = schema.Dict(title=u"Daten des Fragebogens", required=True,
                        key_type=schema.TextLine(),
                        value_type=schema.List(value_type=schema.TextLine())) 


@implementer(ICheckliste)
class Checkliste(Item):
    """
    """
