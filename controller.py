# coding: utf-8

from views.display_operations import print_dico_items, clear, convert_dico_to_df
from views.inputs_operations import inputs_add_player, inputs_add_tournament,\
    dialog_box_to_confirm_or_cancel

from models.class_player_model import Player
from models.class_tournament_model import Tournament

from models.class_database import create_db_folder, Database

from controllers.algorithm import AlgoSuisse
from models.class_round import Round

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
    confirm = dialog_box_to_confirm_or_cancel("Are you sure to add this player in database ?\n"
                                              + print_dico_items(serialized_player))
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
    name, place, duration, dates, turns, rounds, players, \
    time_control, description = inputs_add_tournament()

    # CREATE TOURNAMENT OBJECT
    tournament = Tournament(name, place, duration, dates, turns, rounds,
                            players, time_control, description)

    serialized_tournament = tournament.serialized()

    # DIALOG BOX TO CONFIRM
    clear()
    confirm = dialog_box_to_confirm_or_cancel("Are you sure to add this player in database ?\n"
                                              + print_dico_items(serialized_tournament))
    if confirm:
        # CREATE OR ACCES TO DIRECTORY
        path_bdd = create_db_folder()

        # CREATE OR LOAD DATABASE
        database_object = Database(path_bdd, "database")

        # CREATE OR LOAD PLAYERS
        database_object.create_or_load_table_name("tournaments")

        # ADD SERIALIZED PLAYERS OBJECTS
        database_object.insert_serialized_objects_in_current_table([serialized_tournament])


def analyze_tournaments(table_name):
    # CREATE OR LOAD DATABASE
    path_bdd = create_db_folder()

    choices = {}
    if os.path.isdir(path_bdd):
        database_object = Database(path_bdd, "database").create_or_load_table_name(table_name)

        tournaments = database_object.get_all_items_in_current_table()

        empty_tournaments = []
        for st in tournaments:
            tournament = Tournament(st["name"], st["place"], st["duration"],
                                    st["dates"], st["turns"], st["rounds"],
                                    st["players"], st["time_control"],
                                    st["description"])
            if not tournament.rounds:
                empty_tournaments.append(tournament)

        for i, t in enumerate(empty_tournaments, 1):
            choices[str(i)] = "- Enter " + str(i) + " to run : " + t.name + " | " + t.place + "\n"

    return choices, empty_tournaments


def analyze_players(table_name):
    # CREATE OR LOAD DATABASE
    path_bdd = create_db_folder()

    choices = {}
    if os.path.isdir(path_bdd):
        database_object = Database(path_bdd, "database").create_or_load_table_name(table_name)

        players = database_object.get_all_items_in_current_table()

        players_objects = []
        for sp in players:
            player = Player(sp["name"], sp["firstname"], sp["birthday"], sp["gender"], sp["ranking"])
            players_objects.append(player)

        for i, p in enumerate(players_objects, 1):
            choices[str(i)] = "- Enter " + str(i) + " to add : " + p.name + " " + p.firstname + "\n"

    return choices, players_objects


def search_element_in_db():
    # CREATE OR ACCES TO DIRECTORY
    path_bdd = create_db_folder()

    database_object = Database(path_bdd, "database").create_or_load_table_name("tournaments")

    # SEARCH ITEM IN TABLE
    database_object.search_item_in_table('L+')


# GAME ACTIONS --------------------------------------------------

def show_rounds_result(rounds):
    # TODO A DEBUG
    for round in rounds:
        players_list = []
        for match in round.matchs():
            p_one, p_two = match.serialized_infos()
            players_list.append(p_one)
            players_list.append(p_two)

        list_results = []
        for player in players_list:
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
    tournament.set_players(players)  # init players list

    algo = AlgoSuisse(players)
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
        matchs = algo.second_sort(last_round).get_matchs_historic(tournament.rounds).second_pairing() \
            .apply_first_player_condition()

        new_round = Round(matchs, "Round " + str(rounds_count + 1))

        tournament.add_round_in_rounds(new_round)
        new_round.start().play(0).end()

        rounds_count = len(tournament.rounds)

        show_rounds_result([new_round])

    # show_rounds_result(tournament.rounds)

    input("Press Enter to continue...")
    # print("write tournament")
    # print(tournament.serialized())
    # database_object.create_or_load_table_name('tournaments').update_item(tournament.name, tournament.serialized())

#analyze_tournaments("tournaments")
