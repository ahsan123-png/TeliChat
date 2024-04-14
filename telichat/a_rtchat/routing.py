from django.urls import path
from .consumers import *
#================================
# here we create consumer routing paths 

websocket_urlpatterns=[
    path('ws/chatroom/<chatroom_name>',ChatroomConsumer.as_asgi()),
]