# -*- coding: utf-8 -*-
from edi.checkapp import _
from Products.Five.browser import BrowserView
from edi.checkapp.content.fragestellung import possibleThemen
from edi.checkapp.views.formsnippets import textline, textline_unit, textarea
from plone import api as ploneapi

class FragestellungView(BrowserView):

    def create_optionmarkup(self):
        snippet = ''
        for i in self.context.getFolderContents():
            obj = i.getObject()
            if obj.portal_type == 'Antwortoption':
                snippet += ploneapi.content.get_view('option-view', obj, self.request).create_snippet()
        return snippet

    def create_formmarkup(self):
        if self.context.antworttyp in ['radio', 'checkbox']:
            return self.create_optionmarkup()
        if self.context.antworttyp == 'text':
            return textline(self.context.getId(), self.context.fieldclass, self.context.title, self.context.antworttyp)
        if self.context.antworttyp == 'number' and not self.context.einheit:
            return textline(self.context.getId(), self.context.fieldclass, self.context.title, self.context.antworttyp)
        if self.context.antworttyp == 'number' and self.context.einheit:
            return textline_unit(self.context.getId(), self.context.fieldclass, self.context.title, self.context.antworttyp, self.context.einheit)
        if self.context.antworttyp == 'textarea':
            return textarea(self.context.getId(), self.context.fieldclass, self.context.title)
        return u'<p>Error: es konnte kein Eingabefeld zugeordnet werden.</p>'

    def check_options(self):
        if not self.context.getFolderContents():
            if self.context.antworttyp == 'radio':
                return 'Radiobutton'
            if self.context.antworttyp == 'checkbox':
                return 'Checkboxen'
        return False

    def __call__(self):
        self.thema = possibleThemen(self.context).getTerm(self.context.thema).title
        self.formmarkup = self.create_formmarkup()
        return self.index()
