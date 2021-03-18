# coding: utf-8

from os import system, name
import json
import pandas as pd
# --- DISPLAY ---
pd.set_option('display.max_rows', 30)
pd.set_option('display.max_columns', 10)
pd.set_option('display.width', 1000)

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


def convert_dico_to_df(dico):
    df = pd.DataFrame(dico)
    print(df)

