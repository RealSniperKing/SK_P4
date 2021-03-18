# coding: utf-8

class Player():
    def __init__(self, name, firstname, birthday, gender, ranking):
        self.name = name
        self.firstname = firstname
        self.birthday = birthday
        self.gender = gender
        self.ranking = ranking

        self.serialized_player_var = {}

        self.tournament_ranking = 0

    def add_match_result(self, value):
        self.tournament_ranking += value
        return self

    def serialized(self):
        self.serialized_player_var = {"name": self.name,
                                      "firstname": self.firstname,
                                      "birthday": str(self.birthday),
                                      "gender": self.gender,
                                      "ranking": self.ranking}
        return self.serialized_player_var
