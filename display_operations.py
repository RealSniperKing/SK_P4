# coding: utf-8

from os import system, name


# --- DISPLAY ---


def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


def show_menu(title, input_value):
    clear()
    print(title)
    choice = input(input_value)
    return choice
