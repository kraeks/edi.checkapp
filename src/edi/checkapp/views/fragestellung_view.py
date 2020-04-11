# -*- coding: utf-8 -*-
from edi.checkapp import _
from Products.Five.browser import BrowserView
from edi.checkapp.content.fragestellung import possibleThemen
from plone import api as ploneapi

class FragestellungView(BrowserView):

    def create_optionmarkup(self):
        snippet = ''
        for i in self.context.getFolderContents():
            obj = i.getObject()
            snippet += ploneapi.content.get_view('option-view', obj, self.request).create_snippet()
        return snippet

    def create_formmarkup(self):
        if self.context.antworttyp in ['radio', 'checkbox']:
            return self.create_optionmarkup()
        else:
            return u'<p></p>'

    def __call__(self):
        self.thema = possibleThemen(self.context).getTerm(self.context.thema).title
        self.formmarkup = self.create_formmarkup()
        return self.index()
