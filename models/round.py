# coding: utf-8

from basics_operations import get_curent_date_time
import time
import random


def generate_fake_results():
    dico = {0: [0.5, 0.5], 1: [1, 0], 2: [0, 1]}
    random_value = random.randrange(0, 3)

    return dico[random_value]


class Round:
    def __init__(self, list_matchs, name):
        self.list_matchs = list_matchs
        self.name = name

        self.date_start = None
        self.date_end = None

    def start(self):
        self.date_start = get_curent_date_time()

        print("------ START ------ " + self.date_start)

    def play(self, time_value):
        for match in self.list_matchs:
            fake_result = generate_fake_results()
            match.set_score_player_1(fake_result[0])
            match.set_score_player_2(fake_result[1])
        time.sleep(time_value)

    def end(self):
        self.date_end = get_curent_date_time()
        print("------ END ------ " + self.date_end)

    def round_results(self):
        players_scores = []

        for match in self.list_matchs:
            for data in match.datas:
                players_scores.append(data)

        return players_scores
