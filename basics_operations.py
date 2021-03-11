# -*- coding: utf-8 -*-
import os
import os.path
from datetime import datetime

# BASIC OPERATIONS

def add_folder(path_root_folder, name_new_folder):
    tempo_new_folder = os.path.join(path_root_folder, name_new_folder)
    if not os.path.exists(tempo_new_folder):
        try:
            os.makedirs(tempo_new_folder)
        except:
            print('This folder already exist')
    return tempo_new_folder

def get_curent_date_time():
    format_date = "%Y-%m-%d %H:%M:%S"
    now = datetime.now()

    current_time = now.strftime(format_date)
    return current_time



