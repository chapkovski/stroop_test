from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

author = "Philip Chapkovski, chapkovski@gmail.com"


class Constants(BaseConstants):
    name_in_url = 'minimum_ret'
    players_per_group = None
    num_rounds = 1
    colors = ['Purple', 'Brown', 'Red', 'Blue', 'Green', ]


class Subsession(BaseSubsession):
    ...


class Group(BaseGroup):
    ...


class Player(BasePlayer):
    dump_tasks = models.LongStringField()
    num_answered = models.IntegerField(initial=0)
    num_correct = models.IntegerField(initial=0)


from django.db import models as djmodels


class Task(djmodels.Model):
    player = djmodels.ForeignKey(to=Player, related_name='tasks')
    color = models.StringField()
    text = models.StringField()
    answer = models.StringField(null=True)
