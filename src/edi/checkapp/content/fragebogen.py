# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
# from plone.autoform import directives
from plone.dexterity.content import Container
# from plone.namedfile import field as namedfile
from plone.supermodel import model
# from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import implementer


# from edi.checkapp import _


class IFragebogen(model.Schema):
    """ Marker interface and Dexterity Python Schema for Fragebogen
    """

    fbid = schema.TextLine(title=u"Kürzel oder Nummer des Fragebogens")

    text = RichText(title=u'Startseite des Fragebogens')

    themenbereiche = schema.List(title=u'Themenbereiche',
                                 description=u'Geben Sie hier die Themenbereiche an, zu denen die Fragen gruppiert werden sollen.',
                                 value_type=schema.TextLine(),
                                 required=False)


@implementer(IFragebogen)
class Fragebogen(Container):
    """
    """
