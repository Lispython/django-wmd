#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin

from testapp.models import Note
from testapp.forms import NoteForm

class NoteAdmin(admin.ModelAdmin):
    """Note admin interface
    """
    list_display = "body",
    form = NoteForm


admin.site.register(Note, NoteAdmin)
