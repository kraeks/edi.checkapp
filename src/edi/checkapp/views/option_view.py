# -*- coding: utf-8 -*-
from edi.checkapp import _
from Products.Five.browser import BrowserView
from edi.checkapp.views.formsnippets import option, option_group, option_group_label, option_group_label_einheit

class OptionView(BrowserView):

    def create_snippet(self):
        if self.context.zusatz:
            if self.context.showlabel and not self.context.einheit:
                return option_group_label(self.context)
            elif self.context.showlabel and self.context.einheit:
                return option_group_label_einheit(self.context)
            else:
                return option_group(self.context)
        else:
            return option(self.context)

    def __call__(self):
        self.snippet = self.create_snippet()
        return self.index()
