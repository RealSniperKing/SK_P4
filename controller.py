# coding: utf-8

from display_operations import print_dico_items, clear
from inputs_operations import main_menu_actions, inputs_add_player, dialog_box_to_confirm_or_cancel

from player_model import Player
from db_operations import create_db_folder, create_db_table, insert_objects_in_table

def add_player():
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
        # CREATE OR ACCES TO DATA BASE
        path_bdd = create_db_folder()
        players_table = create_db_table(path_bdd, "Players")

        # INSERT OBJECT TO DATA BASE
        insert_objects_in_table(players_table, [serialized_player])
    else:
        main_menu_actions()


def start_new_tournament():
    print("START NEW TOURNAMENT")
    #t = Tournament()


add_player()
