# coding: utf-8

from tinydb import TinyDB, Query
from pathlib import Path, PurePath

from mvc.utils.basics_operations import add_folder
import os, sys

def create_db_folder():
    script_path = Path(sys.argv[0])
    #print("script_path = " + str(script_path))

    main_dir = script_path.parent.parent
    #print("main_dir = " + str(main_dir))

    base_dir_script = Path(main_dir, "models")

    try:
        path_bdd_directory = add_folder(base_dir_script, 'BDD')
    except:
        path_bdd_directory = ""

    #print("path_bdd_directory = " + str(path_bdd_directory))
    return path_bdd_directory

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

        return self

    def insert_serialized_objects_in_current_table(self, value):
        self.serialized_objects = value
        self.current_table_object.insert_multiple(self.serialized_objects)

    def search_item_in_table(self, value):
        self.item_to_search = value
        Player = Query()
        #test = db_table.search(Player.firstname == 'Eli')
        test = self.current_table_object.search(Player.firstname.search(self.item_to_search))

        print(test)

    def update_item(self, name, dico_t):
        id_dico = -1
        print(self.current_table_object.count)
        for i, dico in enumerate(self.current_table_object.all(), 1):
            if dico["name"] == name:
                id_dico = i
        print(id_dico)
        if id_dico != -1:

            self.current_table_object.update(dico_t, doc_ids=[id_dico])

            print(self.current_table_object.all())

    def remove_item(self, name):
        id_dico = -1
        db = self.current_table_object
        User = Query()
        contains_result = db.contains(User.name == 'Tournoi de test')
        count_result = db.count(User.name == 'Tournoi de test')
        print(contains_result)
        print(count_result)

        doc = db.get(User.name == 'Tournoi de test')
        print(doc)

        item_id = doc.doc_id
        print(item_id)
        if db.contains(doc_id=item_id):
            db.remove(doc_ids=[item_id])

        #print(self.current_table_object.all())


        # Test = Query()
        # el = self.current_table_object.get(Test.name == 'name')
        # print(el)

        # print(self.current_table_object.contains(doc_id=id_dico))
        # if id_dico != -1:
        #     self.current_table_object.remove(doc_ids=[id_dico])

    def set_current_table_name(self, value):
        self.current_table_name = value

        return self

    def get_all_items_in_current_table(self):
        items = self.current_table_object.all()
        return items


