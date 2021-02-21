# -*- coding: utf-8 -*-

from Products.Five.browser import BrowserView
from edi.checkapp.views.examples import uischema
from plone.i18n.normalizer import idnormalizer
from plone import api
import jsonlib

class UiSchemaView(BrowserView):

    def __call__(self):
        uischema = self.get_uischema()
        return jsonlib.write(uischema)

    def get_uischema(self):
        context = self.context
        kopffragen = context.kopffragen
        elements = list()
        for i in kopffragen:
            element = dict()
            id = idnormalizer.normalize(i.get('frage'))
            antworttyp = i.get('antworttyp')
            if antworttyp in ['text', 'datetime-local', 'date']:
                element['type'] = "Control"
                element['scope'] = "#/properties/%s" % id
            elif antworttyp == 'textarea':
                element['type'] = "Control"
                element['scope'] = "#/properties/%s" % id
                element['options'] = {'multi':True}
            elif antworttyp == 'radio':
                element['type'] = "Control"
                element['scope'] = "#/properties/%s" % id
                element['options'] = {'radiobuttons':True, 'stacked':True}
            elif antworttyp == 'checkbox':
                element['type'] = "Control"
                element['scope'] = "#/properties/%s" % id
                element['options'] = {'stacked':True}
            elements.append(element)
        fiverulesview = api.content.get_view(name='five-rules-view', context=self.context, request=self.request)
        content = fiverulesview.get_content()
        for thema in content:
            form_deps = dict()
            group = dict()
            group['type'] = "Group"
            group['label'] = thema
            group['elements'] = list()
            groupelements = list()
            for k in content[thema]:
                groupelement = dict()
                groupelement['options'] = dict()
                antworttyp = k['typ']
                if antworttyp in ['text', 'number']:
                    groupelement['type'] = "Control"
                    groupelement['scope'] = "#/properties/%s" % k['id']
                    if k['einheit']:
                        groupelement['options']['append'] = k['einheit']
                    if k['placeholder']:
                        groupelement['options']['placeholder'] = k['placeholder']
                elif antworttyp == 'textarea':
                    groupelement['type'] = "Control"
                    groupelement['scope'] = "#/properties/%s" % k['id']
                    groupelement['options']['multi'] = 3
                    if k['placeholder']:
                        groupelement['options']['placeholder'] = k['placeholder']
                elif antworttyp == 'radio':
                    groupelement['type'] = "Control"
                    groupelement['scope'] = "#/properties/%s" % k['id']
                    groupelement['options']['radiobuttons'] = True 
                    groupelement['options']['stacked'] = True
                elif antworttyp == 'checkbox':
                    groupelement['type'] = "Control"
                    groupelement['scope'] = "#/properties/%s" % k['id']
                    groupelement['options']['stacked'] = True
                if k['id'] in form_deps:
                    groupelement['showOn'] = form_deps[k['id']]
                if antworttyp in ['radio', 'checkbox']:
                    for option in k['optionen']:
                        if option.dep_fields:
                            targetuid = 'edi' + option.dep_fields.to_object.UID()
                            form_deps[targetuid] = {'scope':groupelement['scope'], 'type':'EQUALS', 'referenceValue':option.title}
                groupelements.append(groupelement)
            group['elements'] = groupelements
            elements.append(group)

        return elements
