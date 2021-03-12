# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
from edi.checkapp.views.examples import uischema
from plone.i18n.normalizer import idnormalizer
from plone import api
import jsonlib

class EllaView(BrowserView):

    def __call__(self):
        content = self.get_content()
        return jsonlib.write(content)

    def formatcontent(self, obj):
        article = dict()
        article['id'] = obj.getId()
        article['title'] = obj.title
        article['description'] = obj.description
        article['text'] = u''
        if hasattr(obj, 'text'):
            if obj.text:
                article['text'] = obj.text.output
        article['img'] = u''
        if hasattr(obj, 'image'):
            if obj.image:
                article['img'] = '%s/@@download/image' % obj.absolute_url()
        return article

    def get_content(self):
        content = []
        if self.context.portal_type == 'Folder':
            fc = self.context.listFolderContents(contentFilter={"portal_type" : "Document"})
            for obj in fc:
                content.append(self.formatcontent(obj))
        else:
            content.append(self.formatcontent(self.context))
        return content
