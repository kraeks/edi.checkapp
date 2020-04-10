# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from plone.dexterity.content import Container
from plone.supermodel import model
from plone import api as ploneapi
from zope.interface import provider
from plone.autoform import directives as form
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from collective.z3cform.datagridfield import DataGridFieldFactory
from collective.z3cform.datagridfield import DictRow
from zope import schema
from zope.interface import implementer

# from edi.checkapp import _

answertypes = [
         SimpleTerm(u'choice', u'choice', u'Auswahl'),
         SimpleTerm(u'list', u'list', u'Mehrfachauswahl'),
         SimpleTerm(u'integer', u'integer', u'Ganzzahl'),
         SimpleTerm(u'float', u'float', u'Gleitkommazahl'),
         SimpleTerm(u'textline', u'textline', u'Textzeile'),
         SimpleTerm(u'textarea', u'textarea', u'Textfeld'),
        ]
Antworttypen = SimpleVocabulary(answertypes)


class IKopffragen(model.Schema):
    frage = schema.TextLine(title=u"Frage oder Angabe")

    antworttyp = schema.Choice(title=u"Antworttyp", source=Antworttypen)

    einheit = schema.TextLine(title=u"Maßeinheit", required=False)

    optionen = schema.List(title=u"Antwortoptionen", value_type=schema.TextLine(), required=False)


class IFragebogen(model.Schema):
    """ Marker interface and Dexterity Python Schema for Fragebogen
    """

    fbid = schema.TextLine(title=u"Kürzel oder Nummer des Fragebogens")

    text = RichText(title=u'Startseite oder Kopf des Fragebogens', required=False)

    themenbereiche = schema.List(title=u'Themenbereiche',
                                 description=u'Geben Sie hier die Themenbereiche an, zu denen die Fragen gruppiert werden sollen.',
                                 value_type=schema.TextLine(),
                                 required=False)

    form.widget('kopffragen', DataGridFieldFactory)
    kopffragen = schema.List(title=u"Allgemeine Fragen im Kopf des Fragebogens",
                               required=False,
                               value_type=DictRow(title=u"Kopffragen", schema=IKopffragen))

    notiz = schema.Bool(title=u"Notizenfeld anbieten",
                        description=u"Anklicken wenn Sie eine Notiz zu dieser Fragestellung erlauben wollen.")

    schlusstext = RichText(title=u'Schlusstext des Fragebogens', required=False)



@implementer(IFragebogen)
class Fragebogen(Container):
    """
    """
