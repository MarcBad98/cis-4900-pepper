from django.contrib import admin, messages
from django.core import serializers
from django.http import HttpResponse
from django.utils.translation import ngettext

import db_app.models as models


@admin.register(models.RecognizedText)
class RecognizedTextAdminModel(admin.ModelAdmin):

    date_hierarchy = 'date'
    list_display = ('text', 'active', )
    list_filter = ('active', )
    search_fields = ('text', )
    fields = ('id', 'date', 'text', 'active',  )
    readonly_fields = ('id', 'date', )
    actions = ['export_as_json', ]

    def export_as_json(self, request, queryset):
        response = HttpResponse(content_type='application/json')
        response['Content-Disposition'] = 'attachment; filename=export.json'
        serializers.serialize('json', queryset, stream=response)
        return response
