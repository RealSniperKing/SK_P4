# coding: utf-8

from datetime import datetime, date, timedelta
from ask_user_module import ask_user
import os
from basics_operations import add_folder

from tinydb import TinyDB

class Tournament:
    def __init__(self, name, place, duration, dates, turns, rounds, players_count, players, time_control, description):
        # WHERE
        self.name = name
        self.place = place

        # DATE(S)
        self.duration = duration
        self.dates = dates

        # RULES
        self.turns = turns
        self.rounds = rounds

        self.players_count = players_count
        self.players = players

        self.time_control = time_control
        self.description = description

        # EXPORT
        self.serialized_tournament = None

    def serialized(self):
        self.serialized_tournament = {"name": self.name, "place": self.place, "duration": self.duration,
                                      "dates": self.dates, "turns": self.turns, "rounds": self.rounds,
                                      "players_count": self.players_count, "players": self.players,
                                      "time_control": self.time_control, "description": self.description}
        return self.serialized_tournament

    def add_round_in_rounds(self, value):
        self.rounds.append(value)
        return self

    def set_players(self, value):
        self.players = value
        return self

    def get_rounds(self):
        return self.rounds