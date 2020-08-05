from rest_framework import serializers

import db_app.models as models


class RecognizedTextSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.RecognizedText
        fields = ('id', 'active', 'date', 'text', )
