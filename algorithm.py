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
        # ASSIGN OPPONENT TO TOP HALF PART
        for i in range(0, len_half):
            sub_df = df2.iloc[[i, i + len_half], [0, 1, 2, 3, 4]]

            players_and_scores = [] * 2  # This list contain 2 players
            for index, row in sub_df.iterrows():
                dico = row.to_dict()

                # CREATE PLAYER OBJECT
                player = Player(dico["name"], dico["firstname"], dico["birthday"], dico["gender"], dico["ranking"])
                score = 0
                players_and_scores.append([player, score])

            # CREATE MATCH
            match = Match(players_and_scores[0], players_and_scores[1])

            # ADD MATCH IN MATCHS LIST
            matchs.append(match)
        return matchs

    def second_sort(self, round):
        """ 3. Triez tous les joueurs en fonction de leur nombre total de points. Si plusieurs
        joueurs ont le même nombre de points, triez-les en fonction de leur rang. """
        self.round = round
        players_results = round.round_results()

        # CONVERT player result to dico
        players_infos_to_sort = []
        all_scores = []
        for player_result in players_results:
            player_object = player_result[0]
            player_score = player_result[1]

            dico = {"player_object": player_object, "player_score": player_score,
                    "player_ranking": player_object.ranking}
            players_infos_to_sort.append(dico)
            all_scores.append(player_score)

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

    def second_pairing(self):
        """ 4. Associez le joueur 1 avec le joueur 2, le joueur 3 avec le joueur 4, et ainsi de suite. Si le joueur 1 a
        déjà joué contre le joueur 2, associez-le plutôt au joueur 3. """

        df = self.sorted_dataframe
        for i in range(0, len(df)):
            if (i + 1) % 2 == 0:
                sub_df = df.iloc[[i-1, i], [0, 1, 2]]
                print(sub_df)

                # TODO CHECK IF PLAYER 1 HAVE ALREADY PLAYED WITH SECOND PLAYER

                # for index, row in sub_df.iterrows():
                #     dico = row.to_dict()
                #     print(dico)
                # print("...")

