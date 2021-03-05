# coding: utf-8

# from bdd_operations import create_bdd_folder, create_bdd_table, insert_objects_in_table

class Player():
    def __init__(self, name, firstname, birthday, gender, ranking):
        self.name = name
        self.firstname = firstname
        self.birthday = birthday
        self.gender = gender
        self.ranking = ranking

        self.serialized_player_var = {}

    def serialized(self):
        self.serialized_player_var = {"name": self.name, "firstname": self.firstname, "birthday": str(self.birthday),
                                 "gender": self.gender, "ranking": self.ranking}
        return self.serialized_player_var