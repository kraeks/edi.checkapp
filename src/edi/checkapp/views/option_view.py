# -*- coding: utf-8 -*-

from edi.checkapp import _
from Products.Five.browser import BrowserView

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class OptionView(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('option_view.pt')

    def __call__(self):
        # Implement your own actions:
        self.msg = _(u'A small message')
        return self.index()
