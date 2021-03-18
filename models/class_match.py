# coding: utf-8

class Match:
    def __init__(self, list1_player_score, list2_player_score):
        self.list1_player_score = list1_player_score
        self.list2_player_score = list2_player_score

        self.datas = (list1_player_score, list2_player_score)

        self.serialized_matchs = []

    def set_score_player_1(self, value):
        self.list1_player_score[1] = value
        self.list1_player_score[0].add_match_result(value)

    def set_score_player_2(self, value):
        self.list2_player_score[1] = value
        self.list2_player_score[0].add_match_result(value)

    def serialized_infos(self):
        infos = []
        for data in self.datas:
            player_object = data[0]
            player_score = data[1]

            dico = {"player_object": player_object, "player_score": player_score,
                    "player_ranking": player_object.ranking}
            infos.append(dico)

        return infos[0], infos[1]
