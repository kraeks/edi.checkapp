# -*- coding: utf-8 -*-
from plone.autoform import directives
from plone.dexterity.content import Item
from plone.supermodel import model
from zope import schema
from zope.interface import implementer
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary
from collective.z3cform.datagridfield import DataGridFieldFactory
from collective.z3cform.datagridfield import DictRow

from edi.checkapp import _

buttonfarbe = SimpleVocabulary((
    SimpleTerm(value="primary", token="primary", title="Blau"),
    SimpleTerm(value="secondary", token="secondary", title="Grau"),
    SimpleTerm(value="info", token="info", title="Türkis"),
    SimpleTerm(value="success", token="success", title="Grün"),
    SimpleTerm(value="danger", token="danger", title="Rot")
    ))

method = SimpleVocabulary((
    SimpleTerm(value="GET", token="GET", title="GET"),
    SimpleTerm(value="POST", token="POST", title="POST"),
    SimpleTerm(value="PUT", token="PUT", title="PUT"),
    SimpleTerm(value="REDIRECT", token="REDIRECT", title="REDIRECT")
    ))

field = SimpleVocabulary((
    SimpleTerm(value="string", token="string", title="Textzeile"),
    SimpleTerm(value="boolean", token="boolean", title="Checkbox")
    ))

class IProperties(model.Schema):
    addid = schema.TextLine(title="ID")
    addtitle = schema.TextLine(title="Titel")
    addtype = schema.Choice(title=u"Feldtyp", vocabulary=field, default="string")
    pflichtfeld = schema.Bool(title=u"Pflichtfeld")


class IServicebutton(model.Schema):
    """ Marker interface and Dexterity Python Schema for Servicebutton
    """
    name = schema.TextLine(title=u"Servicename")
    cssclass = schema.Choice(title=u"Buttonfarbe", vocabulary=buttonfarbe, default="primary")
    method = schema.Choice(title=u"Request-Methode", vocabulary=method, default="POST")
    modaltext = schema.Text(title="Text im Modal nach Betätigung des Buttons", required=False)
    directives.widget('additional', DataGridFieldFactory)
    additional = schema.List(title="Zusatzformular im Modal nach Betätigung des Buttons", required=False, 
            value_type=DictRow(title="Properties", schema=IProperties))


@implementer(IServicebutton)
class Servicebutton(Item):
    """
    """
