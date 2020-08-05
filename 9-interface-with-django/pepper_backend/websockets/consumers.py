from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from channels.generic.websocket import JsonWebsocketConsumer


class Operation:

    SAVE = 'SAVE'
    DELETE = 'DELETE'


class PepperTablet(JsonWebsocketConsumer):

    groups = ('broadcast', )

    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        self.close()

    def receive(self, text_data=None, bytes_data=None):
        # not expecting to receive data from the websocket connections at the moment
        pass

    def _send_tablet_data(self, op, instance):
        self.send_json(
            {
                'op': op,
                'recognizedText': {
                    'id': instance.id,
                    'active': instance.active,
                    'date': str(instance.date),
                    'text': instance.text,
                },
            },
        )

    def tablet_save(self, event):
        self._send_tablet_data(op=Operation.SAVE, instance=event['object'])

    def tablet_delete(self, event):
        self._send_tablet_data(op=Operation.DELETE, instance=event['object'])
