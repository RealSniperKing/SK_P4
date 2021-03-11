# coding: utf-8


class Match:
    def __init__(self, list1_player_score, list2_player_score):
        self.list1_player_score = list1_player_score
        self.list2_player_score = list2_player_score

        self.datas = (list1_player_score, list2_player_score)

    def set_score_player_1(self, value):
        self.list1_player_score[1] = value

    def set_score_player_2(self, value):
        self.list2_player_score[1] = value
