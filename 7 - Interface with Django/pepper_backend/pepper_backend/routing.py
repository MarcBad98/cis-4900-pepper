from django.urls import path

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator

import websockets.consumers as consumers


application = ProtocolTypeRouter({
    # (http ---> Django views) is added by default
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter([
                path('ws/pepper-tablet', consumers.PepperTablet),
            ])
        ),
    ),
})
