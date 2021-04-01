# coding: utf-8

from views.display_operations import show_menu, clear
from views.inputs_operations import ask_user, dialog_box_to_confirm_or_cancel

from controller import add_player_in_db, add_tournament_in_db, \
    analyze_tournaments, analyze_players, start_game, report_game

class UI:
    def __init__(self):
        self.main_menu_actions()
        self.select_tournament = None

    def main_menu_actions(self):
        """ Display main menu and control calls to actions """
        choice = "0"
        choices = {"1": "- Enter 1 to acces Players Menu.\n",
                   "2": "- Enter 2 to acces Tournaments Menu\n",
                   "3": "- Enter 3 to access a Game Menu\n"}

        while choice not in list(choices):
            choice = show_menu("MAIN - MENU", ''.join(choices.values()))

        if choice == "1":
            self.menu_player_actions()
        elif choice == "2":
            self.menu_tournament_actions()
        elif choice == "3":
            self.menu_game_actions()

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
        choices = {"1": "- Enter 1 to Add a new tournament\n",
                   "2": "- Enter 2 to Delete a tournament\n",
                   "4": "- Enter 4 to Return in Main Menu\n"}

        while choice not in list(choices):
            choice = show_menu("TOURNAMENT - MENU", ''.join(choices.values()))

        if choice == "1":
            add_tournament_in_db()
            self.menu_tournament_actions()
        elif choice == "2":
            self.menu_tournament_actions()
        elif choice == "4":
            self.main_menu_actions()

    # GAME ACTIONS
    def menu_game_actions(self):
        """ Display tournament menu and control calls to actions """
        choice = "0"
        choices = {"1": "- Enter 1 to start a game\n",
                   "2": "- Enter 2 to continue a game\n",
                   "3": "- Enter 3 to show game results\n",
                   "4": "- Enter 4 to Return in Main Menu\n"}

        while choice not in list(choices):
            choice = show_menu("GAME - MENU", ''.join(choices.values()))

        if choice == "1":
            self.menu_start_a_game()
            self.menu_game_actions()
        elif choice == "2":
            self.menu_resume_play()
            self.menu_game_actions()
        elif choice == "3":
            self.menu_show_game_result()
            self.menu_game_actions()
        elif choice == "4":
            self.main_menu_actions()

    def menu_start_a_game(self):
        choices, tournaments_empty = analyze_tournaments("tournaments", 0)
        choice = "0"
        cancel_id = str(len(choices) + 1)
        choices[cancel_id] = "- Enter " + cancel_id + " to access a Game Menu\n"

        while choice not in list(choices):
            choice = show_menu("RUN - TOURNAMENT", ''.join(choices.values()), False)

        if choice in choices and choice != cancel_id:
            tournament = tournaments_empty[int(choice) - 1]
            # INPUT PLAYERS
            self.select_tournament = tournament
            self.menu_select_players()

    def menu_resume_play(self):
        choices, tournaments_empty = analyze_tournaments("tournaments", 1)
        choice = "0"
        cancel_id = str(len(choices) + 1)
        choices[cancel_id] = "- Enter " + cancel_id + " to access a Game Menu\n"

        while choice not in list(choices):
            choice = show_menu("RESUME - TOURNAMENT", ''.join(choices.values()), False)

        if choice in choices and choice != cancel_id:
            tournament = tournaments_empty[int(choice) - 1]
            # INPUT PLAYERS
            self.select_tournament = tournament

    def menu_show_game_result(self):
        choices, tournaments_empty = analyze_tournaments("tournaments", 2)
        choice = "0"
        cancel_id = str(len(choices) + 1)
        choices[cancel_id] = "- Enter " + cancel_id + " to access a Game Menu\n"

        while choice not in list(choices):
            choice = show_menu("SHOW - TOURNAMENT", ''.join(choices.values()), False)

        if choice in choices and choice != cancel_id:
            tournament = tournaments_empty[int(choice) - 1]
            # INPUT PLAYERS
            self.select_tournament = tournament
            self.menu_game_report()

    def menu_select_players(self):
        players_max = ask_user('Enter players number', int, "8")
        choices, players_objects = analyze_players("players")
        choice = "0"
        # cancel_id = str(len(choices) + 1)

        players_to_party = []
        players_object_to_party = []
        while len(players_to_party) != players_max:
            clear()
            print("Players list :")
            print(players_to_party)

            while choice not in list(choices):
                choice = show_menu("IMPORT - PLAYERS", ''.join(choices.values()), False)

            if choice in choices and len(choices) > 1:
                if choice not in players_to_party:
                    players_to_party.append(choice)
                    players_object_to_party.append(players_objects[int(choice) - 1])
            choice = "0"

        print(players_to_party)
        confirm = dialog_box_to_confirm_or_cancel("Are you sure to start this tournament ?\n")
        if confirm:
            start_game(self.select_tournament, players_object_to_party)

    def menu_game_report(self):
        choice = "0"
        choices = {"1": "- Enter 1 to print players by alphabetical order\n",
                   "2": "- Enter 2 to print players by ranking\n",
                   "3": "- Enter 3 to print rounds\n",
                   "4": "- Enter 4 to print matchs\n",
                   "5": "- Enter 5 to access a Game Menu\n"}

        while choice not in list(choices):
            choice = show_menu("GAME - REPORTS", ''.join(choices.values()))

        print("choice = " + str(choice))
        if choice == "1":
            report_game(self.select_tournament, int(choice))
            self.menu_game_report()
        elif choice == "2":
            report_game(self.select_tournament, int(choice))
            self.menu_game_report()
        elif choice == "3":
            report_game(self.select_tournament, int(choice))
            self.menu_game_report()
        elif choice == "4":
            report_game(self.select_tournament, int(choice))
            self.menu_game_report()
        elif choice == "5":
            self.menu_game_actions()

if __name__ == '__main__':
    UI()

