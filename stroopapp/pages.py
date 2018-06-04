from . import models
from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants
import json


class WorkPage(Page):
    timer_text = 'Time left to complete the task:'
    timeout_seconds = 10

    def before_next_page(self):
        self.player.dump_tasks = json.dumps(list(self.player.tasks.all().values()))


page_sequence = [
    WorkPage,
]
