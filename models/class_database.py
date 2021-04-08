from tinydb import TinyDB, Query, where
from pathlib import Path

from utils.basics_operations import add_folder
import sys


def create_db_folder():
    script_path = Path(sys.argv[0])
    # print("script_path = " + str(script_path))

    main_dir = script_path.parent.parent
    # print("main_dir = " + str(main_dir))

    base_dir_script = Path(main_dir, "models")

    try:
        path_bdd_directory = add_folder(base_dir_script, 'BDD')
    except Exception as ex:
        print("Error = " + str(ex))
        path_bdd_directory = ""

    # print("path_bdd_directory = " + str(path_bdd_directory))
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
            # players_table.truncate()  # clear the table first
            self.current_table_object = players_table

        return self

    def insert_serialized_objects_in_current_table(self, value):
        self.serialized_objects = value
        self.current_table_object.insert_multiple(self.serialized_objects)

    def search_item_in_table(self, value):
        self.item_to_search = value
        Player = Query()
        # test = db_table.search(Player.firstname == 'Eli')
        test = self.current_table_object.search(Player.firstname.search(self.item_to_search))

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

    def remove_item(self, items_to_check):
        db = self.current_table_object

        ids = []
        for item in items_to_check:
            doc = db.get(where(item) == items_to_check[item])
            ids.append(doc.doc_id)

        if len(set(ids)) == 1:
            db.remove(doc_ids=[ids[0]])
            print("Item has been removed")

    def set_current_table_name(self, value):
        self.current_table_name = value

        return self

    def get_all_items_in_current_table(self):
        items = self.current_table_object.all()
        return items
