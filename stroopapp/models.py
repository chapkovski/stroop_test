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
    ...


