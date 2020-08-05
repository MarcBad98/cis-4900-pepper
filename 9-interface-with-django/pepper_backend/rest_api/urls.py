from django.urls import path, include

import rest_api.views as views


app_name = 'rest'


urlpatterns = [
    path('list', views.ListRecognizedText.as_view(), name='list'),
    path('create', views.CreateRecognizedText.as_view(), name='create'),
    path('modify/<int:pk>', views.ModifyRecognizedText.as_view(), name='modify'),
]
