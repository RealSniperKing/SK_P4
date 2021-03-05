# -*- coding: utf-8 -*-
import os
import os.path


# BASIC OPERATIONS

def add_folder(path_root_folder, name_new_folder):
    tempo_new_folder = os.path.join(path_root_folder, name_new_folder)
    if not os.path.exists(tempo_new_folder):
        try:
            os.makedirs(tempo_new_folder)
        except:
            print('This folder already exist')
    return tempo_new_folder


