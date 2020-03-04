# -*- coding: utf-8 -*-

from edi.checkapp import _
from Products.Five.browser import BrowserView
from plone import api
from edi.checkapp.content.frage import possibleQuestionsOrPages, SiguvColors

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class RedaktionsAnsicht(BrowserView):

    def get_content(self):
        themen = {}
        for i in self.context.themenbereiche:
            themen[i] = []
        for i in self.context.getFolderContents():
            if i.portal_type == 'Frage':
                obj = i.getObject()
                entry={}
                entry['title'] = obj.title
                entry['frage'] = obj.frage.output
                entry['tipp'] = ''
                if obj.tipp:
                    entry['tipp'] = obj.tipp.output
                optionen = obj.optionen
                format_optionen = []
                for k in optionen:
                    option = {}
                    option['antwort'] = k['antwort']
                    option['color'] = SiguvColors.getTerm(k['color']).token
                    option['aktion'] = u'nächste Frage'
                    if k.get('aktion'):
                        aktion = api.content.get(UID=k['aktion'])
                        aktionstext = aktion.title
                        option['aktion'] = aktionstext
                    format_optionen.append(option)
                entry['optionen'] = format_optionen    
                entry['editurl'] = obj.absolute_url() + '/edit'
                if obj.thema in themen:
                    themen[obj.thema].append(entry)
        return themen

    def get_themenbereiche(self):
        return self.context.themenbereiche
