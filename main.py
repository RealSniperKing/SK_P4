# coding: utf-8

# import logging as lg
from views.inputs_operations import main_menu_actions


class Main:
    """ Run main menu """

    def __init__(self):
        # lg.basicConfig(level=lg.DEBUG)
        main_menu_actions()


if __name__ == '__main__':
    Main()

