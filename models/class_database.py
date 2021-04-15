from tinydb import TinyDB, Query, where
from pathlib import Path

from utils.basics_operations import add_folder
import time


def create_db_folder():
    base_dir_script = Path(Path.cwd().parent, "models")

    try:
        path_bdd_directory = add_folder(base_dir_script, 'BDD')
    except Exception as ex:
        print("Error = " + str(ex))
        path_bdd_directory = ""

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
        player = Query()
        # test = db_table.search(Player.firstname == 'Eli')
        test = self.current_table_object.search(player.firstname.search(self.item_to_search))
        print("test = " + str(test))

    def update_item(self, name, dico_t):
        id_dico = -1
        for i, dico in enumerate(self.current_table_object.all(), 1):
            if dico["name"] == name:
                id_dico = i
        if id_dico != -1:
            self.current_table_object.update(dico_t, doc_ids=[id_dico])

    def update_player(self, items_to_check, dico_player):
        db = self.current_table_object
        ids = []

        for item in items_to_check:
            doc = db.get(where(item) == items_to_check[item])
            ids.append(doc.doc_id)

        if len(set(ids)) == 1:
            id_dico = ids[0]
            self.current_table_object.update(dico_player, doc_ids=[id_dico])

    def remove_item(self, items_to_check):
        db = self.current_table_object

        ids = []
        for item in items_to_check:
            doc = db.get(where(item) == items_to_check[item])
            ids.append(doc.doc_id)

        if len(set(ids)) == 1:
            db.remove(doc_ids=[ids[0]])
            print("Item has been removed")
        time.sleep(3)

    def set_current_table_name(self, value):
        self.current_table_name = value

        return self

    def get_all_items_in_current_table(self):
        items = self.current_table_object.all()
        return items
