from views.ask_user_module import ask_user
from views.display_operations import show_menu, convert_dico_to_df, clear
import time

def edit_match_results(value):
    array = [[0.5, 0.5], [1, 0], [0, 1]]
    return array[value]


class Matchs_edit:
    def __init__(self, matchs):
        self.matchs = matchs

        self.items = None
        self.current_player_id = None
        self.current_match_id = None
        self.mode = None

    def show(self, items, round_name):
        clear()
        print(round_name)
        convert_dico_to_df(items)
        self.items = items

        return self

    def get_match(self):
        match_number = 0
        while match_number not in range(1, len(self.items) + 1):
            match_number = ask_user("Enter match number to edit", int)

        choice = "0"
        choices = {"1": "- Enter 1 to edit score\n",
                   "2": "- Enter 2 to edit rankingA\n",
                   "3": "- Enter 3 to edit rankingB\n"}
        while choice not in choices:
            choice = show_menu("PLAYER CHOICE", ''.join(choices.values()), False)

        self.current_match_id = int(match_number) - 1

        if choice == "2":
            self.current_player_id = 0
        elif choice == "3":
            self.current_player_id = 1

        if choice == "1":
            self.mode = "score"
        elif choice == "2" or choice == "3":
            self.mode = "ranking"

        return self

    def edit(self):
        if self.mode == "score":
            self.score_mode()
        elif self.mode == "ranking":
            self.ranking_mode()

        return self

    def score_mode(self):
        choice = "0"
        choices = {"1": "- Enter 1 to assign this score : A = 0.5 | B = 0.5\n",
                   "2": "- Enter 2 to assign this score : A = 1 | B = 0\n",
                   "3": "- Enter 3 to assign this score : A = 0 | B = 1\n"}
        while choice not in choices:
            choice = show_menu("SCORE CHOICE", ''.join(choices.values()), False)

        result = edit_match_results(int(choice) - 1)
        self.matchs[self.current_match_id].set_score_player_1(result[0])
        self.matchs[self.current_match_id].set_score_player_2(result[1])
        self.matchs[self.current_match_id].empty_result = False

        return self

    def ranking_mode(self):
        new_ranking = ask_user("Enter new ranking value", int)
        self.matchs[self.current_match_id].set_ranking_player(self.current_player_id, new_ranking)

        return self

    def check_results(self):
        edited_results = []
        for match in self.matchs:
            if not match.empty_result:
                edited_results.append(match)

        return edited_results
