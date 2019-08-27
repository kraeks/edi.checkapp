# -*- coding: utf-8 -*-
from plone.dexterity.content import Item
from plone.supermodel import model
from zope import schema
from zope.interface import implementer


class IErgebnisdaten(model.Schema):
    """ Marker interface and Dexterity Python Schema for Ergebnisdaten
    """

    maschnr = schema.TextLine(title=u"Maschinen-Nummer", required=False)

    hersteller = schema.TextLine(title=u"Hersteller der Maschine", required=False)

    fragebogen = schema.TextLine(title=u"ID des Frageboges", required=True)

    fortschritt = schema.Float(title=u"Fortschritt des Fragebogens", required=False)

    notizen = schema.Dict(title=u"Notizen des Fragebogens", required=False,
                        key_type=schema.TextLine(),
                        value_type=schema.Text(),)

    daten = schema.Dict(title=u"Daten des Fragebogens", required=False,
                        key_type=schema.TextLine(),
                        value_type=schema.Dict(key_type=schema.TextLine(), value_type=schema.TextLine()))


@implementer(IErgebnisdaten)
class Ergebnisdaten(Item):
    """
    """
