# -*- coding: utf-8 -*-
"""
Created on Thu May 17 22:33:30 2012

@author: ghost
"""

from django.contrib import admin
from gifts.models import Artifact, Permissions

class ArtifactAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'uid', 'photo', 'status')
    search_fields = ('name', 'uid')

admin.site.register(Artifact, ArtifactAdmin)
admin.site.register(Permissions)