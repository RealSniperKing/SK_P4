# coding: utf-8

def convert_matchs_instances_to_dico(round_matchs):
    matchs_serialized = []
    for match in round_matchs:
        match_temp = match.serialized_infos()
        for item in match_temp:
            item["player_object"] = item["player_object"].serialized()
        matchs_serialized.append(match_temp)
    return matchs_serialized


class Tournament:
    def __init__(self, name, place, duration, dates, turns, rounds, players, time_control, description):
        # WHERE
        self.name = name
        self.place = place

        # DATE(S)
        self.duration = duration
        self.dates = dates

        # RULES
        self.turns = turns
        self.rounds = rounds
        self.players = players
        self.players_count = len(players)

        self.time_control = time_control
        self.description = description

        # EXPORT
        self.serialized_tournament = None

    def serialized(self):
        # SERIALIZED PLAYERS
        serialized_players = []
        for player in self.players:
            serialized_player = player.serialized()
            serialized_players.append(serialized_player)

        # SERIALIZED ROUNDS AND MATCHS
        serialized_rounds = []
        for round in self.rounds:
            round_srz = round.serialized()
            round_matchs = round_srz["matchs"]

            round_srz["matchs"] = convert_matchs_instances_to_dico(round_matchs)
            serialized_rounds.append(round_srz)

        self.serialized_tournament = {"name": self.name,
                                      "place": self.place,
                                      "duration": self.duration,
                                      "dates": self.dates,
                                      "turns": self.turns,
                                      "rounds": serialized_rounds,
                                      "players": serialized_players,
                                      "time_control": self.time_control,
                                      "description": self.description}
        return self.serialized_tournament

    def add_round_in_rounds(self, value):
        self.rounds.append(value)
        return self

    def set_players(self, value):
        self.players = value
        return self

    def get_rounds(self):
        return self.rounds
