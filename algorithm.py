# coding: utf-8

import operator
import numpy as np
import pandas as pd

from models.player_model import Player
from models.match import Match

#https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html

class AlgoSuisse:
    def __init__(self, serialized_players):
        self.serialized_players = serialized_players

        self.sorted_dataframe = None
        self.round = None

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
        #players_results = round.round_results()
        matchs = round.matchs()

        # READ MATCH
        players_infos_to_sort = []
        all_scores = []
        for match in matchs:
            array = match.serialized_infos()
            players_infos_to_sort.append(array[0])
            players_infos_to_sort.append(array[1])

            all_scores.append(array[0]["player_score"])
            all_scores.append(array[1]["player_score"])

        all_scores_without_double = list(reversed(sorted(set(all_scores))))  # Delete double, sort, invert

        # SORT FROM PLAYER_SCORE COLUMN
        df = pd.DataFrame(players_infos_to_sort)
        df_sorted_by_score = df.sort_values(by='player_score')

        # SORT EACH VALUE FROM PLAYER_RANKING COLUMN
        dataframes = []
        for d_value in all_scores_without_double:
            mask = df_sorted_by_score['player_score'] == d_value
            dataframes.append(df_sorted_by_score[mask].sort_values(by='player_ranking'))

        self.sorted_dataframe = pd.concat(dataframes).reset_index(drop=True)  # Merge dataframes and reset index
        #print(self.sorted_dataframe)

        return self

    def second_pairing(self, rounds):
        """ 4. Associez le joueur 1 avec le joueur 2, le joueur 3 avec le joueur 4, et ainsi de suite. Si le joueur 1 a
        déjà joué contre le joueur 2, associez-le plutôt au joueur 3. """

        # GENERATE PLAYERS GAMES HISTORIC FROM ALL MATCH
        matchs_historic = []
        for round in rounds:
            matchs = round.matchs()
            for match in matchs:
                array = match.serialized_infos()
                players_temp = [array[0], array[1]]
                print(players_temp)
                sorted_players_temp = sorted(players_temp, key=lambda x: x['player_object'].name)
                matchs_historic.append(sorted_players_temp)

        print("----------------")
        new_matchs_temp = []
        df = self.sorted_dataframe
        for i in range(0, len(df)):
            if (i + 1) % 2 == 0:
                #sub_df = df.iloc[[i-1, i], [0, 1, 2]]
                sub_df = df.iloc[[i - 1, i], [0, 1, 2]]
                #print(sub_df)

                new_match_temp = []
                for index, row in sub_df.iterrows():
                    dico = row.to_dict()
                    new_match_temp.append(dico)

                new_match_temp_sorted = sorted(new_match_temp, key=lambda x: x['player_object'].name)
                new_matchs_temp.append(new_match_temp_sorted)

        print("****************************************")
        # TODO CHECK IF PLAYER 1 HAVE ALREADY PLAYED WITH SECOND PLAYER
        separator = "    "
        for i, new_match in enumerate(new_matchs_temp, 0):
            if i == 0:
                player_one = new_match[0]['player_object']
                player_two = new_match[1]['player_object']
                vs = player_one.name + separator + player_two.name
                print(vs)
                print(".....")

                switch_bool = False
                for old_match in matchs_historic:
                    player_one_old = old_match[0]['player_object']
                    player_two_old = old_match[1]['player_object']
                    vs_old = player_one_old.name + separator + player_two_old.name

                    print(vs_old)
                    if vs_old == vs:
                        print("SWITCH")
                        switch_bool = True
                        break
                    else:
                        switch_bool = True
                        break
                if switch_bool == True:
                    print("test")
                    new_matchs_temp[0] = player_one
                    new_matchs_temp[1] = player_two

                # print("===========")
                # print(new_match)
                # player_one = new_match[0]['player_object']
                # player_two = new_match[1]['player_object']
                # vs = player_one.name + separator + player_two.name
                # print(vs)

                # if new_match in matchs_historic:
                #     print("yes")
                #     second_player = new_matchs_temp[0][1]
                #     third_player = new_matchs_temp[1][0]
                #
                #     #SWITCH
                #     new_matchs_temp[0][1] = third_player
                #     new_matchs_temp[1][0] = second_player



