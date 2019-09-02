# -*- coding: utf-8 -*-

from Products.Five.browser import BrowserView
from edi.checkapp.content.frage import possibleQuestionsOrPages, SiguvColors

class FrageAnsicht(BrowserView):

    def getOptionen(self):
        results = []
        myoptionen = self.context.optionen
        for i in myoptionen:
            result = {}
            result['antwort'] = i.get('antwort')
            result['aktion'] = ''
            if i.get('aktion'):
                result['aktion'] = possibleQuestionsOrPages(self.context).getTerm(i.get('aktion')).title
            result['color'] = SiguvColors.getTerm(i.get('color')).title
            results.append(result)
        return results
        
