# coding: utf-8

import logging as lg

from display_operations import show_menu
from controller import start_new_tournament  # keep this line


# --- MENUS ---


def main_menu_actions():
    """ Display main menu and control calls to actions """
    choice = 0
    choices = {1: "- Enter 1 to acces Players Menu.\n",
               2: "- Enter 2 to acces Tournaments Menu\n",
               3: "- Enter 3 to start a new tournament\n"}

    while choice not in list(choices):
        choice = int(show_menu("MAIN - MENU",  ''.join(choices.values())))

    if choice == 1:
        menu_player_actions()
    elif choice == 2:
        menu_tournament_actions()
    elif choice == 3:
        start_new_tournament()

def menu_player_actions():
    """ Display players menu and control calls to actions """
    choice = 0
    choices = {1: "- Enter 1 to Add player\n",
               2: "- Enter 2 to Edit Player\n",
               3: "- Enter 3 to Remove Player\n",
               4: "- Enter 4 to Return in Main Menu\n"}

    while choice not in choices:
        choice = int(show_menu("PLAYER - MENU", ''.join(choices.values())))

    if choice == 1:
        menu_player_actions()
    elif choice == 2:
        menu_tournament_actions()
    elif choice == 3:
        start_new_tournament()
    elif choice == 4:
        main_menu_actions()

def menu_tournament_actions():
    """ Display tournament menu and control calls to actions """
    choice = 0
    choices = {1: "- Enter 1 to Edit Tournament\n",
               2: "- Enter 2 to Delete Tournament\n",
               4: "- Enter 4 to Return in Main Menu\n"}

    while choice not in list(choices):
        choice = int(show_menu("TOURNAMENT - MENU", ''.join(choices.values())))

    if choice == 1:
        menu_player_actions()
    elif choice == 2:
        menu_tournament_actions()
    elif choice == 4:
        main_menu_actions()

def main():
    """ Run main menu """
    lg.basicConfig(level=lg.DEBUG)

    main_menu_actions()


if __name__ == '__main__':
    main()
