# coding: utf-8

from display_operations import print_dico_items, clear
from inputs_operations import main_menu_actions, inputs_add_player, dialog_box_to_confirm_or_cancel

from models.player_model import Player
from db_operations import create_db_folder, Database

from algorithm import AlgoSuisse
from models.round import Round


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


def start_new_tournament():
    print("START NEW TOURNAMENT")
    #t = Tournament()


def start_game():
    database_object, table_object = load_all_items_from_db_table('players')

    # GET ALL ITEMS
    serialized_players = database_object.get_all_items_in_current_table()

    algo = AlgoSuisse(serialized_players)
    matchs = algo.step_1_2()

    # ROUND 1
    round_1 = Round(matchs, "Round 1")
    round_1.start()
    round_1.play(1)
    round_1.end()

    players_results = round_1.round_results()

    # OTHERS ROUNDS
    algo.step_3(players_results)


start_game()
