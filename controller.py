# coding: utf-8

from display_operations import clear, show_menu
from ask_user_module import ask_user, date_time_controller
from player_model import Player
from bdd_operations import create_bdd_folder, create_bdd_table, insert_objects_in_table

# --- TOOLS ---

def add_player():
    # INIT VARIABLES
    name = ask_user('Enter name', str, "CHAM")

    first_name = ask_user('Enter first name', str, "Luc")

    format_date = "%Y-%m-%d"
    user_input = ask_user('Enter birthday yyyy-mm-dd', str, "2020-02-03")
    birthday = date_time_controller(user_input, format_date)

    choice = "0"
    choices = {"1": "- Enter 1 to Male\n",
               "2": "- Enter 2 to Female\n"}
    while choice not in list(choices):
        choice = show_menu("Gender ?", ''.join(choices.values()), False)
    choice_content_split = choices[choice].split(" ")
    gender = choice_content_split[len(choice_content_split) - 1]

    ranking = ask_user('Enter ranking', int, "1")

    # PLAYER OBJECT
    player = Player(name, first_name, birthday, gender, ranking)
    serialized_player = player.serialized()

    # BDD
    path_bdd = create_bdd_folder()
    print("path_bdd = " + str(path_bdd))

    players_table = create_bdd_table(path_bdd, "Players")
    insert_objects_in_table(players_table, [serialized_player])

def start_new_tournament():
    clear()
    print("START NEW TOURNAMENT")
    #t = Tournament()

add_player()