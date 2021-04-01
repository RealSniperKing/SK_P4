# coding: utf-8

from views.ask_user_module import ask_user, date_time_controller
from views.display_operations import show_menu, clear

from basics_operations import get_curent_date_time, date_type, convert_string_to_date_time, add_days_to_date_time,\
    convert_date_time_to_string
# --- MENUS ---


def press_key_to_continue():
    input("Press Enter to continue...")


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


def tournament_dates_start_end_from_duration(duration_value):
    # INIT
    dates = []
    input_days = duration_value
    date_string = get_curent_date_time()
    format_date = "%Y-%m-%d %H:%M:%S"
    format_date_stamp = format_date.replace("%", "")

    user_input = ask_user('Enter tournament date start ' + format_date_stamp, str, date_string)
    while type(user_input) != date_type():
        user_input = convert_string_to_date_time(user_input)
        if user_input is "":
            print("Please write date in this format : " + + format_date_stamp)
            user_input = ask_user('Enter tournament date start' + format_date_stamp, str, date_string)

    # ADD ITEM(S) IN LIST
    dates.append(convert_date_time_to_string(user_input))

    if input_days > 1:
        tournament_date_end = add_days_to_date_time(user_input, input_days)
        dates.append(convert_date_time_to_string(tournament_date_end))
    return dates


def inputs_add_tournament():
    name = ask_user('Enter name', str, "test")
    place = ask_user('Enter place', str, "ici")

    duration = ask_user('Enter tournament duration (on how many days)', int, "1")
    dates = tournament_dates_start_end_from_duration(duration)

    turns = ask_user('Enter number of turns', int, "4")
    rounds = []

    players = []

    time_control = ask_user("Enter 1 for Bullet.\nEnter 2 for Blitz.\nEnter 3 for Coup Rapide\n", int, "1")
    description = ask_user('Enter a description', str, "blabla")

    return name, place, duration, dates, turns, rounds, players, time_control, description



