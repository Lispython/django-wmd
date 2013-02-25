#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms

from wmd.widgets import WMDWidget

from testapp.models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        widgets = {
            'body': WMDWidget
        }
