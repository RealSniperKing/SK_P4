# coding: utf-8

import operator
import numpy as np
import pandas as pd

from models.class_player_model import Player
from models.class_match import Match

#https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html

class AlgoSuisse:
    def __init__(self, serialized_players):
        self.serialized_players = serialized_players

        self.sorted_dataframe = None
        self.round = None

        self.matchs_historic = None

        self.new_matchs_temp_sorted = None
        self.new_matchs_temp_no_sorted = None

    def sort_players_by(self, key):
        self.serialized_players.sort(key=operator.itemgetter(key))  # Sorted dictionaries

    def first_sort(self):
        """ 1. Au début du premier tour, triez tous les joueurs en fonction de leur classement. """
        self.sort_players_by('ranking')

        """ 2. Divisez les joueurs en deux moitiés, une supérieure et une inférieure. Le meilleur joueur de la moitié 
        supérieure est jumelé avec le meilleur joueur de la moitié inférieure, et ainsi de suite. """
        len_dico = len(self.serialized_players)
        len_half = int(len_dico / 2)
        df2 = pd.DataFrame(self.serialized_players)  # split_up = df2[0:len_half]  # split_down = df2[4:len_dico]

        matchs = []
        players = []
        # ASSIGN OPPONENT TO TOP HALF PART
        for i in range(0, len_half):
            sub_df = df2.iloc[[i, i + len_half], [0, 1, 2, 3, 4]]

            players_and_scores = [] * 2  # This list contain 2 players
            for index, row in sub_df.iterrows():
                dico = row.to_dict()
                # CREATE PLAYER OBJECT
                player = Player(dico["name"], dico["firstname"], dico["birthday"], dico["gender"], dico["ranking"])

                if player not in players:
                    players.append(player)
                score = 0
                players_and_scores.append([player, score])

            # CREATE MATCH
            match = Match(players_and_scores[0], players_and_scores[1])
            # ADD MATCH IN MATCHS LIST
            matchs.append(match)

        # print(players)
        return matchs, players

    def second_sort(self, round):
        """ 3. Triez tous les joueurs en fonction de leur nombre total de points. Si plusieurs
        joueurs ont le même nombre de points, triez-les en fonction de leur rang. """
        self.round = round
        matchs = round.matchs()

        # CONVERT MATCHS TO PLAYERS LIST
        players_infos_to_sort = []
        all_scores = []
        for match in matchs:
            p_one, p_two = match.serialized_infos()
            p_one["Tournament ranking"] = p_one['player_object'].tournament_ranking
            p_two["Tournament ranking"] = p_two['player_object'].tournament_ranking

            players_infos_to_sort.append(p_one)
            players_infos_to_sort.append(p_two)

            all_scores.append(p_one['player_object'].tournament_ranking)
            all_scores.append(p_two['player_object'].tournament_ranking)

        all_scores_without_double = list(reversed(sorted(set(all_scores))))  # Delete double, sort, invert
        players_infos_sorted = list(reversed(sorted(players_infos_to_sort, key=lambda x: x['player_object'].tournament_ranking)))

        # for p in players_infos_sorted:
        #     print("-----" + str(p["player_object"].name) + "    " + str(p["player_object"].tournament_ranking))

        # SORT FROM PLAYER_SCORE COLUMN
        df = pd.DataFrame(players_infos_sorted)

        # SORT EACH VALUE FROM PLAYER_RANKING COLUMN
        dataframes = []
        for d_value in all_scores_without_double:
            mask = df['Tournament ranking'] == d_value
            # print(df[mask])
            dataframes.append(df[mask].sort_values(by='player_ranking'))

        self.sorted_dataframe = pd.concat(dataframes).reset_index(drop=True)  # Merge dataframes and reset index
        #print(self.sorted_dataframe)

        return self

    def get_matchs_historic(self, rounds):
        # GENERATE PLAYERS GAMES HISTORIC FROM ALL MATCH
        matchs_historic = []

        for round in rounds:
        # matchs = rounds[len(rounds) - 1].matchs()
            matchs = round.matchs()
            for match in matchs:
                array = match.serialized_infos()
                players_temp = [array[0], array[1]]
                sorted_players_temp = sorted(players_temp, key=lambda x: x['player_object'].name)
                matchs_historic.append(sorted_players_temp)
        self.matchs_historic = matchs_historic

        return self

    def second_pairing(self):
        """ 4. Associez le joueur 1 avec le joueur 2 et ainsi de suite."""

        # ASSOCIATION
        new_matchs_temp_sorted = []  # players are not sorted to each match
        new_matchs_temp_no_sorted = []  # players are sorted by name to each match
        df = self.sorted_dataframe

        # PAIRING
        for i in range(0, len(df)):
            if (i + 1) % 2 == 0:
                sub_df = df.iloc[[i - 1, i], [0, 1, 2]]
                #print(sub_df)
                new_match_temp = []
                for index, row in sub_df.iterrows():
                    dico = row.to_dict()
                    new_match_temp.append(dico)

                new_matchs_temp_no_sorted.append(new_match_temp)
                new_match_temp_sorted = sorted(new_match_temp, key=lambda x: x['player_object'].name)
                new_matchs_temp_sorted.append(new_match_temp_sorted)

        self.new_matchs_temp_sorted = new_matchs_temp_sorted
        self.new_matchs_temp_no_sorted = new_matchs_temp_no_sorted

        return self

    def apply_first_player_condition(self):
        """Si le joueur 1 a déjà joué contre le joueur 2, associez-le plutôt au joueur 3. """
        separator = "    "
        # print("apply")
        for i, new_match in enumerate(self.new_matchs_temp_sorted, 0):
            if i == 0:
                player_one = new_match[0]['player_object']
                player_two = new_match[1]['player_object']
                vs = player_one.name + separator + player_two.name
                #print(vs)

                switch_bool = False
                for old_match in self.matchs_historic:
                    #print("old_match = " + str(old_match))
                    player_one_old = old_match[0]['player_object']
                    player_two_old = old_match[1]['player_object']
                    vs_old = player_one_old.name + separator + player_two_old.name
                    #print(vs_old)

                    if vs == vs_old:
                        print("-----> SWITCH PLAYER")
                        print(vs)

                        switch_bool = True
                        break
                    # else:
                    #     switch_bool = True
                    #     break
                if switch_bool == True:

                    player_two_dico = self.new_matchs_temp_no_sorted[i][1]
                    player_third_dico = self.new_matchs_temp_no_sorted[i + 1][0]

                    self.new_matchs_temp_no_sorted[i][1] = player_third_dico
                    self.new_matchs_temp_no_sorted[i + 1][0] = player_two_dico

        matchs = []
        for i, new_match in enumerate(self.new_matchs_temp_no_sorted, 0):
            #print(str(new_match[0]["player_object"].tournament_ranking) + "    " + str(new_match[1]["player_object"].tournament_ranking))
            # CREATE MATCH
            match = Match([new_match[0]["player_object"], 0], [new_match[1]["player_object"], 0])
            matchs.append(match)
        return matchs


