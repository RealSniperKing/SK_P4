# coding: utf-8

from tinydb import TinyDB
from pathlib import Path

from basics_operations import add_folder


def create_db_folder():
    base_dir_script = Path.cwd()
    # GET 'BDD' FOLDER
    try:
        path_bdd_directory = add_folder(base_dir_script, 'BDD')
    except:
        path_bdd_directory = ""
    return path_bdd_directory


def create_db_table(path, name):
    path_table = Path(path, name + ".json")

    db = TinyDB(path_table)
    players_table = db.table("players")
    #players_table.truncate()  # clear the table first

    return players_table


def insert_objects_in_table(table, serialized_objects):
    table.insert_multiple(serialized_objects)


# TODO search object in BDD
