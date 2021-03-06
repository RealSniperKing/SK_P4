# coding: utf-8

from os import system, name
import json

# --- DISPLAY ---


def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


def show_menu(title, input_value, clear_console=True):
    if clear_console is True:
        clear()

    print(title)
    choice = input(input_value)
    return choice


def print_dico_items(serialized_player):

    text = json.dumps(serialized_player, indent=4)

    return text