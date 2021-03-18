# coding: utf-8

from display_operations import print_dico_items, clear
from inputs_operations import main_menu_actions, inputs_add_player, inputs_add_tournament,\
    dialog_box_to_confirm_or_cancel

from models.player_model import Player
from models.tournament_model import Tournament

from db_operations import create_db_folder, Database

from algorithm import AlgoSuisse
from models.round import Round


# DATABASE --------------------------------------------------
def add_player_in_db():
    """ Contains all operations to add a new player in data base """
    # USER INPUTS
    name, first_name, birthday, gender, ranking = inputs_add_player()

    # CREATE PLAYER OBJECT
    player = Player(name, first_name, birthday, gender, ranking)
    serialized_player = player.serialized()

    # DIALOG BOX TO CONFIRM
    clear()
    confirm = dialog_box_to_confirm_or_cancel("Are you sure to add this player in database ?\n"
                                              + print_dico_items(serialized_player))
    if confirm:
        # CREATE OR ACCES TO DIRECTORY
        path_bdd = create_db_folder()

        # CREATE OR LOAD DATABASE
        database_object = Database(path_bdd, "database")

        # CREATE OR LOAD PLAYERS
        database_object.create_or_load_table_name("players")

        # ADD SERIALIZED PLAYERS OBJECTS
        database_object.insert_serialized_objects_in_current_table([serialized_player])
    else:
        main_menu_actions()


def add_tournament_in_db():
    """ Contains all operations to add a new tournament in data base """

    # USER INPUTS
    name, place, duration, dates, turns, rounds, players_count, \
    players, time_control, description = inputs_add_tournament()

    # CREATE TOURNAMENT OBJECT
    tournament = Tournament(name, place, duration, dates, turns, rounds, players_count, \
    players, time_control, description)

    serialized_tournament = tournament.serialized()

    # DIALOG BOX TO CONFIRM
    clear()
    confirm = dialog_box_to_confirm_or_cancel("Are you sure to add this player in database ?\n"
                                              + print_dico_items(serialized_tournament))
    if confirm:
        # CREATE OR ACCES TO DIRECTORY
        path_bdd = create_db_folder()

        # CREATE OR LOAD DATABASE
        database_object = Database(path_bdd, "database")

        # CREATE OR LOAD PLAYERS
        database_object.create_or_load_table_name("tournaments")

        # ADD SERIALIZED PLAYERS OBJECTS
        database_object.insert_serialized_objects_in_current_table([serialized_tournament])
    else:
        main_menu_actions()


def load_all_items_from_db_table(table_name):
    # CREATE OR ACCES TO DIRECTORY
    path_bdd = create_db_folder()

    # CREATE OR LOAD DATABASE
    database_object = Database(path_bdd, "database")

    # CREATE OR LOAD PLAYERS
    database_object.create_or_load_table_name(table_name)

    return database_object


def search_element_in_db():
    # CREATE OR ACCES TO DIRECTORY
    path_bdd = create_db_folder()

    # CREATE OR LOAD DATABASE
    database_object = Database(path_bdd, "database")

    # CREATE OR LOAD PLAYERS
    database_object.create_or_load_table_name("players")

    # SEARCH ITEM IN TABLE
    database_object.search_item_in_table('L+')


# GAME ACTIONS --------------------------------------------------

def start_new_tournament():
    print("START NEW TOURNAMENT")
    #t = Tournament()


def show_round_result(round):
    players_list = []
    for match in round.matchs():
        p_one, p_two = match.serialized_infos()
        players_list.append(p_one)
        players_list.append(p_two)

    print(round.name)
    for player in players_list:
        print(str(player["player_object"].tournament_ranking) + "   " +
              str(str(player["player_object"].name)) + "    " + str(player["player_score"]))
def start_game():
    """ Start directly game without menu"""

    # LOAD TOURNAMENT
    database_object = load_all_items_from_db_table('tournaments')
    serialized_tournaments = database_object.get_all_items_in_current_table()

    # TODO OPTION TO CHOICE THE TOURNAMENT
    st = serialized_tournaments[0]
    #print(st)
    tournament = Tournament(st["name"], st["place"], st["duration"], st["dates"], st["turns"], st["rounds"],
                            st["players_count"], st["players"], st["time_control"], st["description"])
    # LOAD PLAYERS
    database_object.create_or_load_table_name('players')

    # TODO OPTION TO EXTRACT 8 PLAYERS FROM BDD = serialized_players
    serialized_players = database_object.get_all_items_in_current_table()

    algo = AlgoSuisse(serialized_players)
    matchs, players_objects = algo.first_sort()
    tournament.set_players(players_objects)  # init players list

    # ROUND1
    first_round = Round(matchs, "Round 1")
    show_round_result(first_round)

    tournament.add_round_in_rounds(first_round)
    first_round.start().play(1).end()

    show_round_result(first_round)

    # OTHERS ROUNDS
    print("len rounds = " + str(len(tournament.rounds)))
    last_round = first_round
    rounds_count = len(tournament.rounds)

    while rounds_count != tournament.turns:
        print("=====================================")
        print("=====================================")
        matchs = algo.second_sort(last_round).get_matchs_historic(tournament.rounds).second_pairing() \
            .apply_first_player_condition()

        new_round = Round(matchs, "Round " + str(rounds_count + 1))
        show_round_result(new_round)

        tournament.add_round_in_rounds(new_round)

        new_round.start().play(1).end()

        show_round_result(new_round)
        rounds_count = len(tournament.rounds)

    #     print("....")
    #     algo.second_sort(last_round).second_pairing(tournament.rounds)


start_game()
