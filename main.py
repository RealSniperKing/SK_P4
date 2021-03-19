# coding: utf-8

from views.display_operations import show_menu, clear
# from views.inputs_operations import inputs_add_player

from controller import add_player_in_db

class UI:
    def __init__(self):
        self.main_menu_actions()

    def main_menu_actions(self):
        """ Display main menu and control calls to actions """
        choice = "0"
        choices = {"1": "- Enter 1 to acces Players Menu.\n",
                   "2": "- Enter 2 to acces Tournaments Menu\n",
                   "3": "- Enter 3 to start a new tournament\n"}

        while choice not in list(choices):
            choice = show_menu("MAIN - MENU", ''.join(choices.values()))

        if choice == "1":
            self.menu_player_actions()
        elif choice == "2":
            self.menu_tournament_actions()
        elif choice == "3":
            self.menu_tournament_actions()

        return self

    def menu_player_actions(self):
        """ Display players menu and control calls to actions """
        choice = "0"
        choices = {"1": "- Enter 1 to Add player\n",
                   "2": "- Enter 2 to Edit Player\n",
                   # "3": "- Enter 3 to Remove Player\n",
                   "4": "- Enter 4 to Return in Main Menu\n"}

        while choice not in choices:
            choice = show_menu("PLAYER - MENU", ''.join(choices.values()))

        if choice == "1":
            add_player_in_db()
            self.menu_player_actions()
        elif choice == "2":
            self.menu_player_actions()
        # elif choice == "3":
        #     menu_tournament_actions()
        elif choice == "4":
            self.main_menu_actions()

        return self

    def menu_tournament_actions(self):
        """ Display tournament menu and control calls to actions """
        choice = "0"
        choices = {"1": "- Enter 1 to Edit Tournament\n",
                   "2": "- Enter 2 to Delete Tournament\n",
                   "4": "- Enter 4 to Return in Main Menu\n"}

        while choice not in list(choices):
            choice = show_menu("TOURNAMENT - MENU", ''.join(choices.values()))

        if choice == "1":
            self.menu_player_actions()
        elif choice == "2":
            self.menu_tournament_actions()
        elif choice == "4":
            self.main_menu_actions()

if __name__ == '__main__':
    UI()

