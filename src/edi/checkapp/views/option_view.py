# -*- coding: utf-8 -*-
from edi.checkapp import _
from Products.Five.browser import BrowserView
from edi.checkapp.views.formsnippets import option, option_group, option_group_legend, option_group_legend_einheit
from edi.checkapp.views.formsnippets import option_group_textarea, option_group_legend_textarea, option_group_einheit
class OptionView(BrowserView):

    def create_snippet(self):
        if self.context.label:
            if self.context.showlabel and self.context.zusatzformat == 'textline':
                return option_group_legend(self.context)
            elif self.context.showlabel and self.context.zusatzformat == 'textarea':
                return option_group_legend_textarea(self.context)
            elif not self.context.showlabel and self.context.zusatzformat == 'textarea':
                return option_group_textarea(self.context)
            elif self.context.showlabel and self.context.zusatzformat == 'number' and self.context.einheit:
                return option_group_legend_einheit(self.context)
            elif not self.context.showlabel and self.context.zusatzformat == 'number' and self.context.einheit:
                return option_group_einheit(self.context)
            elif self.context.showlabel and self.context.zusatzformat == 'number' and not self.context.einheit:
                return option_group_legend(self.context)
            else:
                return option_group(self.context)
        else:
            return option(self.context)

    def __call__(self):
        self.snippet = self.create_snippet()
        return self.index()
