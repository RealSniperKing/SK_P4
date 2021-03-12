# coding: utf-8

from display_operations import print_dico_items, clear
from inputs_operations import main_menu_actions, inputs_add_player, inputs_add_tournament,\
    dialog_box_to_confirm_or_cancel

from models.player_model import Player
from models.tournament_model import Tournament

from db_operations import create_db_folder, Database

from algorithm import AlgoSuisse
from models.round import Round


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
    else:
        main_menu_actions()


def add_tournament_in_db():
    """ Contains all operations to add a new tournament in data base """

    # USER INPUTS
    name, place, duration, dates, turns, rounds, players_count, \
    players, time_control, description = inputs_add_tournament()

    # CREATE TOURNAMENT OBJECT
    tournament = Tournament(name, place, duration, dates, turns, rounds, players_count, \
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
    else:
        main_menu_actions()


def load_all_items_from_db_table(table_name):
    # CREATE OR ACCES TO DIRECTORY
    path_bdd = create_db_folder()

    # CREATE OR LOAD DATABASE
    database_object = Database(path_bdd, "database")

    # CREATE OR LOAD PLAYERS
    database_object.create_or_load_table_name(table_name)

    return database_object, database_object.current_table_object


def search_element_in_db():
    # CREATE OR ACCES TO DIRECTORY
    path_bdd = create_db_folder()

    # CREATE OR LOAD DATABASE
    database_object = Database(path_bdd, "database")

    # CREATE OR LOAD PLAYERS
    database_object.create_or_load_table_name("players")

    # SEARCH ITEM IN TABLE
    database_object.search_item_in_table('L+')


# GAME ACTIONS --------------------------------------------------

def start_new_tournament():
    print("START NEW TOURNAMENT")
    #t = Tournament()


def start_game():
    database_object, table_object = load_all_items_from_db_table('players')

    serialized_players = database_object.get_all_items_in_current_table()

    algo = AlgoSuisse(serialized_players)
    matchs = algo.first_sort()

    first_round = Round(matchs, "Round 1")
    first_round.start().play(1).end()

    algo.second_sort(first_round).second_pairing()

add_tournament_in_db()
