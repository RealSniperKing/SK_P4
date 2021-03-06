# coding: utf-8

from ask_user_module import ask_user, date_time_controller
from display_operations import show_menu, clear

# --- MENUS ---


def main_menu_actions():
    """ Display main menu and control calls to actions """
    choice = "0"
    choices = {"1": "- Enter 1 to acces Players Menu.\n",
               "2": "- Enter 2 to acces Tournaments Menu\n",
               "3": "- Enter 3 to start a new tournament\n"}

    while choice not in list(choices):
        choice = show_menu("MAIN - MENU",  ''.join(choices.values()))

    if choice == "1":
        menu_player_actions()
    elif choice == "2":
        menu_tournament_actions()
    elif choice == "3":
        menu_tournament_actions()


def menu_player_actions():
    """ Display players menu and control calls to actions """
    choice = "0"
    choices = {"1": "- Enter 1 to Add player\n",
               "2": "- Enter 2 to Edit Player\n",
               "3": "- Enter 3 to Remove Player\n",
               "4": "- Enter 4 to Return in Main Menu\n"}

    while choice not in choices:
        choice = show_menu("PLAYER - MENU", ''.join(choices.values()))

    if choice == "1":
        menu_player_actions()
    elif choice == "2":
        menu_tournament_actions()
    elif choice == "3":
        menu_tournament_actions()
    elif choice == "4":
        main_menu_actions()


def menu_tournament_actions():
    """ Display tournament menu and control calls to actions """
    choice = "0"
    choices = {"1": "- Enter 1 to Edit Tournament\n",
               "2": "- Enter 2 to Delete Tournament\n",
               "4": "- Enter 4 to Return in Main Menu\n"}

    while choice not in list(choices):
        choice = show_menu("TOURNAMENT - MENU", ''.join(choices.values()))

    if choice == "1":
        menu_player_actions()
    elif choice == "2":
        menu_tournament_actions()
    elif choice == "4":
        main_menu_actions()


def dialog_box_to_confirm_or_cancel(title):
    choice = "0"
    choices = {"1": "- Enter 1 to Confirm\n",
               "2": "- Enter 2 to Cancel\n"}

    while choice not in list(choices):
        choice = show_menu(title,  ''.join(choices.values()), False)

    if choice == "1":
        confirm = True
    else:
        confirm = False

    return confirm


# --- TOOLS ---


def inputs_add_player():
    # IDENTITY
    name = ask_user('Enter name', str, "CHAM")
    first_name = ask_user('Enter first name', str, "Luc")

    # BIRTHDAY
    format_date = "%Y-%m-%d"
    user_input = ask_user('Enter birthday yyyy-mm-dd', str, "2020-02-03")
    birthday = date_time_controller(user_input, format_date)

    # GENDER
    choice = "0"
    choices = {"1": "- Enter 1 to Male\n",
               "2": "- Enter 2 to Female\n"}

    while choice not in list(choices):
        choice = show_menu("Gender ?", ''.join(choices.values()), False)
    choice_content_split = choices[choice].split(" ")
    gender = choice_content_split[len(choice_content_split) - 1].strip("\n")

    # RANKING
    ranking = ask_user('Enter ranking', int, "1")

    return name, first_name, birthday, gender, ranking


