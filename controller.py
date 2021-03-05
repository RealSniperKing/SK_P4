# coding: utf-8

from display_operations import clear, show_menu
from ask_user_module import ask_user, date_time_controller
from player_model import Player
from db_operations import create_db_folder, create_db_table, insert_objects_in_table

from inputs_operations import inputs_add_player
# --- TOOLS ---

def add_player():
    """ Contains all operations to add a new player in data base """
    # USER INPUTS
    name, first_name, birthday, gender, ranking = inputs_add_player()

    # CREATE PLAYER OBJECT
    player = Player(name, first_name, birthday, gender, ranking)
    serialized_player = player.serialized()

    # CREATE OR ACCES TO DATA BASE
    path_bdd = create_db_folder()
    players_table = create_db_table(path_bdd, "Players")

    # INSERT OBJECT TO DATA BASE
    insert_objects_in_table(players_table, [serialized_player])

def start_new_tournament():
    clear()
    print("START NEW TOURNAMENT")
    #t = Tournament()

add_player()