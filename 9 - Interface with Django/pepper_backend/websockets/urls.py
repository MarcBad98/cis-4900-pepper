from django.urls import path, include

import websockets.views as views


app_name = 'ws'


urlpatterns = [
    path('demo', views.DemoView.as_view(), name='simple'),
]
