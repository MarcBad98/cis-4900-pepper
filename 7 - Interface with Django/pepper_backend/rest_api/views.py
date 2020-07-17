from rest_framework import generics

import db_app.models as models
import rest_api.serializers as serializers


class ListRecognizedText(generics.ListAPIView):

    queryset = models.RecognizedText.objects.all()
    serializer_class = serializers.RecognizedTextSerializer


class CreateRecognizedText(generics.CreateAPIView):

    queryset = models.RecognizedText.objects.all()
    serializer_class = serializers.RecognizedTextSerializer


class ModifyRecognizedText(generics.RetrieveUpdateDestroyAPIView):

    queryset = models.RecognizedText.objects.all()
    serializer_class = serializers.RecognizedTextSerializer
