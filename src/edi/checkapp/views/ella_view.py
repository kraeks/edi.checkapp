# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
from edi.checkapp.views.examples import uischema
from plone.i18n.normalizer import idnormalizer
from plone import api
import jsonlib
from jinja2 import Template

class EllaView(BrowserView):

    def __call__(self):
        if self.context.portal_type == "EllaKonfig":
            welcome = dict()
            welcome['name'] = self.context.getId()
            welcome['title'] = self.context.title
            welcome['description'] = self.context.description
            welcome['bodytext'] = self.get_ella_content()
            welcome['services'] = self.get_ella_services()
            return welcome
        else:    
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

    def format_ella_single(self, title, text, image):
        tm = Template(self.context.bodytemplate)
        bodytext = tm.render(ella_title = title, ella_bodytext = text, ella_image = image)
        return bodytext

    def format_ella_startnavi(self, startseiten)
        startid = startseiten[0].to_object.getId()
        navigation = """\
<nav aria-label="Navigation">
  <ul class="pagination justify-content-center">
    <li class="page-item active"><a class="page-link" href="#/services/%s">1</a></li>""" % startid
        page = 2
        for i in startseiten[1:]:
            objid = i.to_object.getId()
            navigation += """<li class="page-item"><a class="page-link" href="#/services/%s">%s</a></li>""" % (objid, str(page))
            page += 1
        navigation += """</ul></nav>"""
        return navigation

    def get_ella_content(self):
        title = self.context.title
        if not self.context.startseiten:
            text = self.context.bodytext
            if not text:
                text = u''
            if self.context.image:
                image = '%s/@@download/image' % self.context.absolute_url()
            else:
                image = u''
            content = format_ella_single(title, text, image)
        else:
            obj = self.context.startseiten[0].to_object
            text = getattr(obj, 'text', u'')
            if text:
                text = text.output
            image = getattr(obj, 'image', u'')
            if image:
                image = '%s/@@download/image' % obj.absolute_url()
            content = format_ella_single(title, text, image)
            if self.context.startseiten > 1:
                navi = format_ella_startnavi(self.context.startseiten)
                content += navi
        return content
