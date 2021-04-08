# coding: utf-8
import pandas as pd
from mvc.models.class_match import Match


class Algo_suisse:

    def __init__(self, players_ob):
        self.players_ob = players_ob

        self.sorted_dataframe = None
        self.round = None

        self.matchs_historic = None

        self.new_matchs_temp_sorted = None
        self.new_matchs_temp_no_sorted = None

    def first_sort(self):
        """ First sort and pairing """
        sorted_players = sorted(self.players_ob, key=lambda x: x.ranking)

        len_half = int(len(self.players_ob) / 2)

        matchs = []
        # ASSIGN OPPONENT TO TOP HALF PART
        for i in range(0, len_half):
            player_a = [sorted_players[i], 0]
            player_b = [sorted_players[i + len_half], 0]

            match = Match(player_a, player_b)
            matchs.append(match)

        return matchs

    def second_sort(self, round):
        """ Sort players by score and if equal values sort by ranking """
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
        players_infos_sorted = list(reversed(sorted(players_infos_to_sort,
                                                    key=lambda x: x['player_object'].tournament_ranking)))
        # SORT FROM PLAYER_SCORE COLUMN
        df = pd.DataFrame(players_infos_sorted)

        # SORT EACH VALUE FROM PLAYER_RANKING COLUMN
        dataframes = []
        for d_value in all_scores_without_double:
            mask = df['Tournament ranking'] == d_value
            dataframes.append(df[mask].sort_values(by='player_ranking'))

        self.sorted_dataframe = pd.concat(dataframes).reset_index(drop=True)  # Merge dataframes and reset index

        return self

    def old_matchs(self, rounds):
        """ Generate players games historic from all match """
        matchs_historic = []

        for round in rounds:
            matchs = round.matchs()
            for match in matchs:
                array = match.serialized_infos()
                players_temp = [array[0], array[1]]
                sorted_players_temp = sorted(players_temp, key=lambda x: x['player_object'].name)
                matchs_historic.append(sorted_players_temp)
        self.matchs_historic = matchs_historic

        return self

    def second_pairing(self):
        """ Associate first player with second and so on """
        # ASSOCIATION
        new_matchs_temp_sorted = []  # players are not sorted to each match
        new_matchs_temp_no_sorted = []  # players are sorted by name to each match
        df = self.sorted_dataframe

        # PAIRING
        for i in range(0, len(df)):
            if (i + 1) % 2 == 0:
                sub_df = df.iloc[[i - 1, i], [0, 1, 2]]
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

    def switch_players(self):
        """ If first player already played to second player, associate this to third """
        separator = "    "
        for i, new_match in enumerate(self.new_matchs_temp_sorted, 0):
            if i == 0:
                player_one = new_match[0]['player_object']
                player_two = new_match[1]['player_object']
                vs = player_one.name + separator + player_two.name

                switch_bool = False
                for old_match in self.matchs_historic:
                    player_one_old = old_match[0]['player_object']
                    player_two_old = old_match[1]['player_object']
                    vs_old = player_one_old.name + separator + player_two_old.name

                    if vs == vs_old:
                        print("-----> SWITCH PLAYER\n" + vs)
                        switch_bool = True
                        break
                if switch_bool:
                    player_two_dico = self.new_matchs_temp_no_sorted[i][1]
                    player_third_dico = self.new_matchs_temp_no_sorted[i + 1][0]

                    self.new_matchs_temp_no_sorted[i][1] = player_third_dico
                    self.new_matchs_temp_no_sorted[i + 1][0] = player_two_dico

        matchs = []
        for i, new_match in enumerate(self.new_matchs_temp_no_sorted, 0):
            match = Match([new_match[0]["player_object"], 0], [new_match[1]["player_object"], 0])
            matchs.append(match)
        return matchs
