from django.contrib import admin, messages
from django.core import serializers
from django.http import HttpResponse
from django.utils.translation import ngettext

import db_app.models as models


@admin.register(models.RecognizedText)
class RecognizedTextAdminModel(admin.ModelAdmin):

    date_hierarchy = 'date'
    fields = ('id', 'date', 'active', 'text', )
    actions = ['mark_active', 'mark_inactive', ]

    def export_as_json(self, request, queryset):
        response = HttpResponse(content_type='application/json')
        serializers.serialize('json', queryset, stream=response)
        return response

    def mark_active(self, request, queryset):
        updated = queryset.update(active=True)
        self.message_user(
            request,
            ngettext(
                'Successfully marked text as active.',
                'Successfully marked texts as active.',
                updated,
            ),
            messages.SUCCESS,
        )

    def mark_inactive(self, request, queryset):
        updated = queryset.update(active=False)
        self.message_user(
            request,
            ngettext(
                'Successfully marked text as inactive.',
                'Successfully marked texts as inactive.',
                updated,
            ),
            messages.SUCCESS,
        )
