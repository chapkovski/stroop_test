from channels.routing import route_class
from channels.generic.websockets import JsonWebsocketConsumer
import random
from stroopapp.models import Constants


class TaskTracker(JsonWebsocketConsumer):
    url_pattern = (r'^/tasktracker/(?P<player>[0-9]+)$')

    def prepare_task(self):
        color_text, color_color = random.sample(Constants.colors, 2)
        return {'color_text': color_text,
                'color_color': color_color
                }

    def connect(self, message, **kwargs):
        response = self.prepare_task()
        self.send(response)

    def receive(self, text=None, bytes=None, **kwargs):
        print('ANSWER:', text)
        response = self.prepare_task()

        self.send(response)


channel_routing = [
    route_class(TaskTracker, path=TaskTracker.url_pattern),
]
