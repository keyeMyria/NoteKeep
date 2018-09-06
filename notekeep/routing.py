from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.conf.urls import url

from notekeep import consumers

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            [
                url(r'^ws/refresh/notes/$', consumers.RefreshNotesConsumer),
            ]
        )
    )
})
