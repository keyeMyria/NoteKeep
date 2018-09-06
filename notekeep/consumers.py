from channels.generic.websocket import AsyncWebsocketConsumer


class RefreshNotesConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        user = self.scope["user"]
        await self.channel_layer.group_add(
            user.username,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, code):
        user = self.scope["user"]
        await self.channel_layer.group_discard(
            user.username,
            self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None):
        print("Received message!")

    async def events_refresh(self, event):
        await self.send("Refresh")
