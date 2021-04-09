class Player:
    def __init__(self, name, firstname, birthday, gender, ranking):
        self.name = name
        self.firstname = firstname
        self.birthday = birthday
        self.gender = gender
        self.ranking = int(ranking)

        self.serialized_player_var = {}

        self.tournament_ranking = 0
        self.rankings_list = []
        # self.tournament_ranking_progress = 0

    def add_match_result(self, value):
        self.tournament_ranking += value
        temp_ranking = self.tournament_ranking
        self.rankings_list.append(temp_ranking)
        return self

    def serialized(self, ranking=False):
        self.serialized_player_var = {"name": self.name,
                                      "firstname": self.firstname,
                                      "birthday": str(self.birthday),
                                      "gender": self.gender,
                                      "ranking": self.ranking}
        if ranking:
            self.serialized_player_var["tournament_ranking"] = self.tournament_ranking
            self.serialized_player_var["rankings_list"] = self.rankings_list

        return self.serialized_player_var
