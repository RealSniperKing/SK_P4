# coding: utf-8

from ask_user_module import ask_user, date_time_controller
from display_operations import show_menu

def inputs_add_player():
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

    return name, first_name, birthday, gender, ranking
