# coding: utf-8

import logging as lg

from display_operations import show_menu
from controller import start_new_tournament  # keep this line


# --- MENUS ---


def main_menu_actions():
    choice = "0"
    choices = {"1": "menu_player_actions()", "2": "menu_tournament_actions()", "3": "start_new_tournament()"}

    while choice not in list(choices):
        choice = show_menu("M A I N - M E N U",
                                "- Enter 1 to acces Players Menu.\n"
                                "- Enter 2 to acces Tournaments Menu\n"
                                "- Enter 3 to start a new tournament\n")
    func_to_run = eval(choices[choice])


def menu_player_actions():
    choice = "0"
    choices = {"1": "menu_player_actions()", "2": "menu_tournament_actions()",
               "3": "start_new_tournament()", "4": "main_menu_actions()"}

    while choice not in list(choices):
        choice = show_menu("P L A Y E R - M E N U",
                           # "- Enter 1 to Add player.\n"
                           # "- Enter 2 to Edit Player\n"
                           # "- Enter 3 to Remove Player\n"
                           "- Enter 4 to Return in Main Menu\n")
    func_to_run = eval(choices[choice])


def menu_tournament_actions():
    choice = "0"
    choices = {"1": "menu_player_actions()", "2": "menu_tournament_actions()",
               "3": "start_new_tournament()", "4": "main_menu_actions()"}

    while choice not in list(choices):
        choice = show_menu("T O U R N A M E N T - M E N U",
                           # "- Enter 1 to Add player.\n"
                           # "- Enter 2 to Edit Player\n"
                           # "- Enter 3 to Remove Player\n"
                           "- Enter 4 to Return in Main Menu\n")
    func_to_run = eval(choices[choice])


def main():

    lg.basicConfig(level=lg.DEBUG)

    main_menu_actions()

    # t = Tournament()


if __name__ == '__main__':
    main()
