# -*- coding: utf-8 -*-
import os
import os.path
from datetime import datetime, date, timedelta

# BASIC OPERATIONS


def add_folder(path_root_folder, name_new_folder):
    tempo_new_folder = os.path.join(path_root_folder, name_new_folder)
    if not os.path.exists(tempo_new_folder):
        try:
            os.makedirs(tempo_new_folder)
        except:
            print('This folder already exist')
    return tempo_new_folder


def get_curent_date_time(format_date="%Y-%m-%d %H:%M:%S"):
    now = datetime.now()

    current_time = now.strftime(format_date)
    return current_time


def date_type():
    return datetime


def convert_string_to_date_time(user_input, format_date="%Y-%m-%d %H:%M:%S"):
    try:
        user_input_converted = datetime.strptime(user_input, format_date)
        return user_input_converted
    except:
        user_input = ""
        return user_input


def add_days_to_date_time(user_input, input_days):
    tournament_date_end = user_input + timedelta(days=input_days)

    return tournament_date_end


def convert_date_time_to_string(value, format_date="%Y-%m-%d %H:%M:%S"):
    str_date_time = value.strftime(format_date)
    return str_date_time