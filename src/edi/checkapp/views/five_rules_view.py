# -*- coding: utf-8 -*-
from edi.checkapp import _
from Products.Five.browser import BrowserView
from plone import api as ploneapi
from edi.checkapp.content.frage import possibleQuestionsOrPages, SiguvColors
from edi.checkapp.views.formsnippets import textline, textline_unit, textarea, select, checkbox
from zope.component import getUtility
from plone.i18n.normalizer.interfaces import IIDNormalizer

from Acquisition import aq_inner
from zope.component import getUtility
from zope.intid.interfaces import IIntIds
from zope.security import checkPermission
from zc.relation.interfaces import ICatalog
from plone.app.linkintegrity.handlers import referencedRelationship

class FiveRulesView(BrowserView):

    def back_references(self, source_object, attribute_name):
        """
        Return back references from source object on specified attribute_name
        """
        catalog = getUtility(ICatalog)
        intids = getUtility(IIntIds)
        result = []
        for rel in catalog.findRelations(
             dict(to_id=intids.getId(aq_inner(source_object)),
                  from_attribute=attribute_name)
             ):
            obj = intids.queryObject(rel.from_id)
            if obj is not None and checkPermission('zope2.View', obj):
                result.append(obj)
        return result

    def create_kopffragen(self):
        normalizer = getUtility(IIDNormalizer)
        kopffragen = ''
        for i in self.context.kopffragen:
            title = i.get('frage')
            id = normalizer.normalize(title)
            fieldclass = 'edi__checkapp'
            typ = i.get('antworttyp')
            einheit = i.get('einheit')
            optionen = i.get('optionen')
            if typ == 'radio':
                kopffragen += select(id, fieldclass, title, optionen)
            elif typ == 'checkbox':
                kopffragen += checkbox(id, fieldclass, title, optionen)
            elif typ in ['text', 'date', 'datetime-local']:
                kopffragen += textline(id, fieldclass, title, typ)
            elif typ == 'number' and not einheit:
                kopffragen += textline(id, fieldclass, title, typ)
            elif typ == 'number' and einheit:
                kopffragen += textline_unit(id, fieldclass, title, typ, einheit)
            elif typ == 'textarea':
                kopffragen += textarea(id, fieldclass, title)
        return kopffragen


    def get_content(self):
        themen = {}
        depends = []
        for i in self.context.themenbereiche:
            if '#' in i:
                thema = i.split('#')[1]
                themen[thema] = []
            else:
                themen[i] = []
        for k in self.context.getFolderContents():
            if k.portal_type == 'Fragestellung':
                obj = k.getObject()
                entry = {}
                entry['id'] = 'edi'+obj.UID()
                entry['class'] = ""
                entry['title'] = u''
                entry['frage'] = u''
                if obj.getId() in depends:
                    entry['class'] = "collapse"
                if obj.antworttyp in ['radio', 'checkbox']:
                    entry['title'] = obj.title
                if obj.frage:
                    entry['frage'] = obj.frage.output
                for option in obj.getFolderContents():
                    opt_object = option.getObject()
                    if opt_object.dep_fields:
                        depends.append(opt_object.dep_fields.to_object.getId())
                entry['snippet'] = ploneapi.content.get_view('fragestellung-view', obj, self.request).create_formmarkup()    
                entry['editurl'] = obj.absolute_url() + '/edit'
                if obj.thema in themen:
                    themen[obj.thema].append(entry)
        return themen

    def get_themenbereiche(self):
        themenbereiche = []
        for i in self.context.themenbereiche:
            if '#' in i:
                themenbereiche.append(i.split('#'))
            else:
                themenbereiche.append(('', i))
        return themenbereiche
