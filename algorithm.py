# coding: utf-8

import operator
import numpy as np
import pandas as pd

#https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html
class AlgoSuisse:
    def __init__(self, serialized_players):
        self.serialized_players = serialized_players

    def sort_players_by(self, key):
        self.serialized_players.sort(key=operator.itemgetter(key))  # Sorted dictionaries

    def first_sort_players(self):
        self.sort_players_by('ranking')

        len_dico = len(self.serialized_players)
        len_half = int(len_dico / 2)
        # print(len_half)

        df2 = pd.DataFrame(self.serialized_players)
        # split_up = df2[0:len_half]
        # split_down = df2[4:len_dico]

        for i in range(0, len_half):
            print(df2.iloc[[i, i + len_half], [0, 1, 2, 3, 4]])
            print('...')

