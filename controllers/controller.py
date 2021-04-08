# coding: utf-8

from views.display_operations import print_dico, clear, convert_dico_to_df
from views.inputs_operations import inputs_add_player, inputs_add_tournament, confirm_or_cancel, \
    press_key_to_continue

from models.class_player_model import Player
from models.class_tournament_model import Tournament

from models.class_database import create_db_folder, Database

from controllers.algorithm import Algo_suisse
from models.class_round import Round
from models.class_match import Match

import os
import os.path


# DATABASE --------------------------------------------------


def add_player_in_db():
    """ Contains all operations to add a new player in data base """
    # USER INPUTS
    name, first_name, birthday, gender, ranking = inputs_add_player()

    # CREATE PLAYER OBJECT
    player = Player(name, first_name, birthday, gender, ranking)
    serialized_player = player.serialized()

    # DIALOG BOX TO CONFIRM
    clear()
    confirm = confirm_or_cancel("Are you sure to add this player in database ?\n" + print_dico(serialized_player))
    if confirm:
        # CREATE OR ACCES TO DIRECTORY
        path_bdd = create_db_folder()

        # CREATE OR LOAD DATABASE
        database_object = Database(path_bdd, "database")

        # CREATE OR LOAD PLAYERS
        database_object.create_or_load_table_name("players")

        # ADD SERIALIZED PLAYERS OBJECTS
        database_object.insert_serialized_objects_in_current_table([serialized_player])
    # else:
    #     main_menu_actions()


def add_tournament_in_db():
    """ Contains all operations to add a new tournament in data base """

    # USER INPUTS
    name, place, duration, dates, turns, rounds, players, time_control, description = inputs_add_tournament()

    # CREATE TOURNAMENT OBJECT
    tournament = Tournament(name, place, duration, dates, turns, rounds,
                            players, time_control, description)

    serialized_tournament = tournament.serialized()

    # DIALOG BOX TO CONFIRM
    clear()
    confirm = confirm_or_cancel("Are you sure to add this player in database ?\n" + print_dico(serialized_tournament))
    if confirm:
        # CREATE OR ACCES TO DIRECTORY
        path_bdd = create_db_folder()

        # CREATE OR LOAD DATABASE
        database_object = Database(path_bdd, "database")

        # CREATE OR LOAD PLAYERS
        database_object.create_or_load_table_name("tournaments")

        # ADD SERIALIZED PLAYERS OBJECTS
        database_object.insert_serialized_objects_in_current_table([serialized_tournament])


def analyze_tournaments(table_name, mode):
    """ mode 0 = empty / mode 1 = in progress / mode 2 = completed / mode 3 = all"""
    path_bdd = create_db_folder()
    choices = {}
    if os.path.isdir(path_bdd):
        database_object = Database(path_bdd, "database")\
            .create_or_load_table_name(table_name)

        tournaments = database_object.get_all_items_in_current_table()

        return_tournaments = []
        for st in tournaments:
            tournament = Tournament(st["name"],
                                    st["place"],
                                    st["duration"],
                                    st["dates"],
                                    st["turns"],
                                    dic_tournament_to_ob(st["rounds"]),
                                    dic_players_to_ob(st["players"]),
                                    st["time_control"],
                                    st["description"])
            if mode == 0:
                if not tournament.rounds:
                    return_tournaments.append(tournament)
            if mode == 1:
                if len(tournament.rounds) > tournament.turns and len(tournament.rounds) < tournament.turns:
                    return_tournaments.append(tournament)
            if mode == 2:
                if len(tournament.rounds) == tournament.turns:
                    return_tournaments.append(tournament)
            if mode == 4:
                return_tournaments.append(tournament)

        for i, t in enumerate(return_tournaments, 1):
            choices[str(i)] = "- Enter " + str(i) + " to run : " + t.name +\
                              " | " + t.place + "\n"

    return choices, return_tournaments


def analyze_players(table_name):
    """ return all players objects from database """
    path_bdd = create_db_folder()

    choices = {}
    if os.path.isdir(path_bdd):
        database_object = Database(path_bdd, "database").create_or_load_table_name(table_name)

        players = database_object.get_all_items_in_current_table()

        players_objects = dic_players_to_ob(players)

        for i, p in enumerate(players_objects, 1):
            choices[str(i)] = "- Enter " + str(i) + " to add : " + p.name + " " + p.firstname + "\n"

    return choices, players_objects


def search_element_in_db():
    # CREATE OR ACCES TO DIRECTORY
    path_bdd = create_db_folder()

    database_object = Database(path_bdd, "database").create_or_load_table_name("tournaments")

    # SEARCH ITEM IN TABLE
    database_object.search_item_in_table('L+')


# CONVERT --------------------------------------------------


def dic_players_to_ob(players):
    """ convert players dictionaries to players objects """
    players_objects = []
    for sp in players:
        player = Player(sp["name"], sp["firstname"], sp["birthday"],
                        sp["gender"], sp["ranking"])
        players_objects.append(player)
    return players_objects


def dic_tournament_to_ob(rounds):
    """ convert rounds dictionaries to rounds objects """
    rounds_ob = []
    for round in rounds:
        list_matchs = []
        for match in round['matchs']:
            player_a_ob = match[0]['player_object']
            player_a_ob_array = dic_players_to_ob([player_a_ob])

            player_a_score = match[0]['player_score']

            player_b_ob = match[1]['player_object']
            player_b_ob_array = dic_players_to_ob([player_b_ob])

            player_b_score = match[1]['player_score']

            match_ob = Match([player_a_ob_array[0], player_a_score],
                             [player_b_ob_array[0], player_b_score])

            list_matchs.append(match_ob)
        round_ob = Round(list_matchs, round['name'])
        round_ob.date_start = round['date_start']
        round_ob.date_end = round['date_end']

        rounds_ob.append(round_ob)

    return rounds_ob


def players_to_dico(players):
    players_dico = []
    for player in players:
        players_dico.append(player.serialized())
    return players_dico


# REPORT --------------------------------------------------


def extract_matchs(round_matchs):
    items = []
    for match in round_matchs:
        match_temp = match.serialized_infos()
        match_infos = {'playerA': match_temp[0]["player_object"].name, 'scoreA': match_temp[0]["player_score"],
                       'rankingA': match_temp[0]["player_ranking"], 'playerB': match_temp[1]["player_object"].name,
                       'scoreB': match_temp[1]["player_score"], 'rankingB': match_temp[0]["player_ranking"]}
        items.append(match_infos)
    return items


def extract_rounds(round_infos, round_matchs):
    versus = []
    for match in round_matchs:
        match_temp = match.serialized_infos()
        vs = match_temp[0]["player_object"].name + "|" + match_temp[1]["player_object"].name
        versus.append(vs)
    del round_infos['matchs']

    for i, match_vs in enumerate(versus, 1):
        round_infos['match ' + str(i)] = match_vs

    return round_infos


def report_game(tournament, mode):
    if mode == 1 or mode == 2:
        players = tournament.players
        if mode == 1:  # print players by alphabetical order
            players = sorted(players, key=lambda x: x.name)
        elif mode == 2:  # print players by ranking
            players = sorted(players, key=lambda x: x.ranking)
        convert_dico_to_df(players_to_dico(players))

    if mode == 3 or mode == 4:  # print rounds
        rounds = tournament.rounds
        items = []
        for round in rounds:
            round_infos = round.serialized()
            round_matchs = round_infos['matchs']

            if mode == 3:
                items_temp = extract_rounds(round_infos, round_matchs)
                items.append(items_temp)
            if mode == 4:
                items_temp = extract_matchs(round_matchs)
                items.extend(items_temp)
        if items:
            convert_dico_to_df(items)

    press_key_to_continue()


def players_reports(mode):
    """ mode 0 = by alphabetical order / mode 1 = by ranking """
    choices, players_objects = analyze_players("players")

    if mode == 0:
        sorted_players = sorted(players_objects, key=lambda x: x.name)
    elif mode == 1:
        sorted_players = sorted(players_objects, key=lambda x: x.ranking)

    convert_dico_to_df(players_to_dico(sorted_players))

    press_key_to_continue()


def tournaments_report():
    choices, tournaments = analyze_tournaments("tournaments", 4)

    tournaments_serialized = []
    for tournament in tournaments:
        tournament_temp = tournament.serialized()

        len_rounds = len(tournament_temp['rounds'])
        len_players = len(tournament_temp['players'])

        tournament_temp['rounds'] = len_rounds
        tournament_temp['players'] = len_players

        tournaments_serialized.append(tournament_temp)

    convert_dico_to_df(tournaments_serialized)

    press_key_to_continue()


# GAME ACTIONS --------------------------------------------------


def show_rounds_result(rounds):
    for round in rounds:
        players_list = []
        for match in round.matchs():
            p_one, p_two = match.serialized_infos()
            players_list.append(p_one)
            players_list.append(p_two)

        list_results = []
        for i, player in enumerate(players_list, 0):
            dico_print = {}
            dico_print["Round"] = round.name
            dico_print["Name"] = player["player_object"].name
            dico_print["First name"] = player["player_object"].firstname

            dico_print["Tournament ranking"] = player["player_object"].tournament_ranking
            dico_print["Before this round"] = player["player_object"].tournament_ranking - player["player_score"]
            dico_print["Player Score"] = player["player_score"]

            dico_print["Default ranking"] = player["player_object"].ranking
            list_results.append(dico_print)

        convert_dico_to_df(list_results)


def start_game(tournament, players):
    """ Start directly game without menu"""
    path_bdd = create_db_folder()
    database_object = Database(path_bdd, "database")

    tournament.set_players(players)  # init players list
    algo = Algo_suisse(players)
    matchs = algo.first_sort()

    # ROUND1
    first_round = Round(matchs, "Round 1")
    tournament.add_round_in_rounds(first_round)
    first_round.start().play(0).end()
    show_rounds_result([first_round])

    # OTHERS ROUNDS
    last_round = first_round
    rounds_count = len(tournament.rounds)

    while rounds_count != tournament.turns:
        matchs = algo.second_sort(last_round).old_matchs(tournament.rounds).second_pairing().switch_players()
        new_round = Round(matchs, "Round " + str(rounds_count + 1))

        tournament.add_round_in_rounds(new_round)
        new_round.start().play(0).end()

        rounds_count = len(tournament.rounds)
        show_rounds_result([new_round])

    press_key_to_continue()

    # SAVE PARTY
    database_object.create_or_load_table_name('tournaments').update_item(tournament.name, tournament.serialized())
