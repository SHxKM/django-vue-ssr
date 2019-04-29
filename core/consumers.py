from channels.generic.websocket import WebsocketConsumer
import json
from asgiref.sync import async_to_sync


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = 'index'
        self.room_group_name = 'index'

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'message': message
            }
        )

    def chat_message(self, event):
        message = event['message']

        send_to_client = {
            'message': message,
        }

        # Send message to WebSocket
        self.send(text_data=json.dumps(send_to_client))
