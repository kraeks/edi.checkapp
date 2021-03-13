# -*- coding: utf-8 -*-

from Products.Five.browser import BrowserView
from edi.checkapp.views.examples import schema
from plone.i18n.normalizer import idnormalizer
import jsonlib
from plone import api

class SchemaView(BrowserView):

    def __call__(self, localmarker=False):
        objschema = self.get_schema()
        if localmarker:
            return objschema
        return jsonlib.write(objschema)

    def get_schema(self):
        context = self.context
        kopffragen = context.kopffragen
        title = "%s-%s" % (context.fbcat, context.fbid) 
        description = context.title
        props = dict()
        required = list()
        for i in kopffragen:
            id = idnormalizer.normalize(i.get('frage'))
            props[id] = {"title":i.get('frage')}
            antworttyp = i.get('antworttyp')
            req = i.get('required')
            if antworttyp in ['text','textarea']:
                props[id]['type'] = "string"
            elif antworttyp == 'datetime-local':
                props[id]['type'] = "string"
                props[id]['format'] = "date-time"
            elif antworttyp == 'date':
                props[id]['type'] = "string"
                props[id]['format'] = "date"
            elif antworttyp == 'radio':
                props[id]['type'] = "string"
                props[id]['enum'] = i.get('optionen')
            elif antworttyp == 'checkbox':
                props[id]['type'] = "array"
                props[id]['enum'] = i.get('optionen')
            elif antworttyp == "zahlenwert":
                props[id]['type'] = "number"
            if req:
                required.append(id)

        fiverulesview = api.content.get_view(name='five-rules-view', context=self.context, request=self.request)
        content = fiverulesview.get_content()
        
        for thema in content:
            for k in content[thema]:
                id = k['id']
                props[id] = dict()
                props[id]['title'] = k['title']
                antworttyp = k['typ']
                req = k['required']
                if antworttyp in ["text", "textarea"]:
                    props[id]['type'] = "string"
                elif antworttyp == "radio":
                    props[id]['type'] = "string"
                    props[id]['enum'] = [j.title for j in k['optionen']]
                elif antworttyp == "checkbox":
                    props[id]['type'] = "array"
                    props[id]['enum'] = [j.title for j in k['optionen']]
                elif antworttyp == "number":
                    props[id]['type'] = "number"
                if req:
                    required.append(id)

        return {'title':title,
                'description':description,
                'properties':props, 
                'required':required,}
