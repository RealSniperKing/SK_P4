# coding: utf-8

from tinydb import TinyDB, Query, where
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

# class DBTable:
#     def __init__(self, name):

class Database:
    def __init__(self, path, name):
        self.path = path
        self.name = name
        path_table = Path(self.path, self.name + ".json")
        self.db = TinyDB(path_table)

        # DEF VAR
        self.current_table_name = None
        self.current_table_object = None
        self.serialized_objects = None
        self.item_to_search = None

    def create_or_load_table_name(self, value):
        self.current_table_name = value

        players_table = None
        if self.current_table_name is not None:
            players_table = self.db.table(self.current_table_name)
            #players_table.truncate()  # clear the table first
            self.current_table_object = players_table

        return players_table

    def insert_serialized_objects_in_current_table(self, value):
        self.serialized_objects = value
        self.current_table_object.insert_multiple(self.serialized_objects)

    def search_item_in_table(self, value):
        self.item_to_search = value
        Player = Query()
        #test = db_table.search(Player.firstname == 'Eli')
        test = self.current_table_object.search(Player.firstname.search(self.item_to_search))

        print(test)

# TODO search object in BDD
