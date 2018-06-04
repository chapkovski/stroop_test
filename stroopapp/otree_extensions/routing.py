from channels.routing import route_class
from channels.generic.websockets import JsonWebsocketConsumer
import random
from stroopapp.models import Constants, Player


class TaskTracker(JsonWebsocketConsumer):
    url_pattern = (r'^/tasktracker/(?P<player>[0-9]+)$')

    def prepare_task(self, player, task):
        return {'color_text': task.text,
                'color_color': task.color,
                'num_answered': player.num_answered,
                'num_correct': player.num_correct, }

    def connect(self, message, **kwargs):
        player = Player.objects.get(id=self.kwargs['player'])
        unanswered_tasks = player.tasks.filter(answer__isnull=True)
        if unanswered_tasks.exists():
            task = unanswered_tasks.first()
        else:
            color, text =  random.sample(Constants.colors, 2)
            task = player.tasks.create(color=color, text=text)
        response = self.prepare_task(player, task)
        self.send(response)

    def receive(self, text=None, bytes=None, **kwargs):
        player = Player.objects.get(id=self.kwargs['player'])
        oldtask = player.tasks.filter(answer__isnull=True).first()
        oldtask.answer = text
        oldtask.save()
        player.num_answered += 1
        if text == oldtask.color:
            player.num_correct += 1
        color, text = random.sample(Constants.colors, 2)
        newtask = player.tasks.create(color=color, text=text)
        response = self.prepare_task(player, newtask)
        player.save()
        self.send(response)



channel_routing = [
    route_class(TaskTracker, path=TaskTracker.url_pattern),
]
