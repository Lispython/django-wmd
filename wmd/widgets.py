#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.utils.safestring import mark_safe


class WMDWidget(forms.Textarea):
    class Media:
        css = {'all': ('wmd/wmd.css',)}
        js = ('wmd/showdown.js', 'wmd/wmd.js', )

    def render(self, name, value, attrs=None):
        return mark_safe(self.template % {
            "id": attrs['id'],
            "super": super(WMDWidget, self).render(name, value, attrs)})


    template = """
    <div id="%(id)s-editor-wrapper" class="wmd-editor-wrapper">
    <div id="%(id)s-wmd-button-bar" class="wmd-panel"></div>
    %(super)s
    <div id="%(id)s-wmd-preview" class="wmd-preview"></div>
    </div>
    <script type="text/javascript">
            setup_wmd({
            input: "%(id)s",
            button_bar: "%(id)s-wmd-button-bar",
            preview: "%(id)s-wmd-preview",
            helpLink: "http://daringfireball.net/projects/markdown/syntax"});
    </script>"""
