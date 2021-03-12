# coding: utf-8

from datetime import datetime, date, timedelta
from ask_user_module import ask_user
import os
from basics_operations import add_folder

from tinydb import TinyDB

class Tournament:
    def __init__(self, name, place, duration_value, dates, number_of_turns, rounds, players_count, players,
                 time_control, description):
        # WHERE
        self.name = None
        self.place = None

        # DATE(S)
        self.duration_value = None
        self.dates = None

        # RULES
        self.number_of_turns = None
        self.rounds = None

        self.players_count = None
        self.players = None

        self.time_control = None
        self.description = None

    # def create(self):
    #     self.name = ask_user('Enter name', str, "test")
    #     self.place = ask_user('Enter place', str, "ici")
    #
    #     # TOURNAMENT DATE(S)
    #     self.duration_value = ask_user('Enter tournament duration (on how many days)', int, "1")
    #
    #     self.dates = self.tournament_dates_start_end_from_duration(self)
    #
    #     self.number_of_turns = ask_user('Enter number of turns', int, "4")
    #     self.rounds = []
    #
    #     self.players_count = 8
    #     self.players = []
    #
    #     self.time_control = ask_user("Enter 1 for Bullet.\nEnter 2 for Blitz.\nEnter 3 for Coup Rapide\n",
    #                                  int, "1")
    #     self.description = "description"

    # def tournament_dates_start_end_from_duration(self):
    #     # INIT
    #     input_days = self.duration_value
    #     dates = []
    #     today = date.today()  # Today's date
    #     format_date = "%Y-%m-%d"
    #     date_string = today.strftime(format_date)  # Default value
    #
    #     user_input = ask_user('Enter tournament date start yyyy-mm-dd', str, date_string)
    #
    #     while type(user_input) != datetime:
    #         try:
    #             user_input = datetime.strptime(user_input, format_date)
    #         except:
    #             print("Please write date in this format : yyyy-mm-dd")
    #             user_input = ask_user('Enter tournament date start yyyy-mm-dd', str, date_string)
    #
    #     # ADD ITEM(S) IN LIST
    #     dates.append(user_input)
    #     # print("tournament_date_start = " + str(user_input))
    #
    #     if input_days > 1:
    #         tournament_date_end = user_input + timedelta(days=input_days)
    #         # print("tournament_date_end = " + str(tournament_date_end))
    #
    #         dates.append(tournament_date_end)
    #     return dates

    # def save_to_BDD(self):
    #     print("save")
    #     base_dir_script = os.getcwd()
    #
    #     # GET 'BDD' FOLDER
    #     path_bdd_directory = add_folder(base_dir_script, 'BDD')
