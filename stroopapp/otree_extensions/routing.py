from channels.routing import route_class
from channels.generic.websockets import JsonWebsocketConsumer
import random
from minimum.models import Player


class TaskTracker(JsonWebsocketConsumer):
    url_pattern = (r'^/tasktracker/(?P<player>[0-9]+)$')

    def prepare_task(self, player, task):
        return {'task': task.question,
                'num_answered': player.num_answered,
                'num_correct': player.num_correct, }

    def connect(self, message, **kwargs):
        player = Player.objects.get(id=self.kwargs['player'])
        unanswered_tasks = player.tasks.filter(answer__isnull=True)
        if unanswered_tasks.exists():
            task = unanswered_tasks.first()
        else:
            task = player.tasks.create(question=random.randint(1, 99))
        response = self.prepare_task(player, task)
        self.send(response)

    def receive(self, text=None, bytes=None, **kwargs):
        player = Player.objects.get(id=self.kwargs['player'])
        oldtask = player.tasks.filter(answer__isnull=True).first()
        oldtask.answer = text
        oldtask.save()
        player.num_answered += 1
        if text == 100 - oldtask.question:
            player.num_correct += 1
        newtask = player.tasks.create(question=random.randint(1, 99))
        response = self.prepare_task(player, newtask)
        player.save()
        self.send(response)


channel_routing = [
    route_class(TaskTracker, path=TaskTracker.url_pattern),
]
