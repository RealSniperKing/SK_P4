# coding: utf-8
from datetime import datetime

def ask_user(message, type_var, default_value):
    # EDIT MESSAGE
    if default_value is not "":
        message += " (default value = " + str(default_value) + ") :"
    else:
        message += " :"

    # CHECK RESPONSE
    user_input = input(message) or default_value
    alert, user_input = ask_user_alert(user_input, type_var)

    # IF BAD RESPONSE
    while alert is True:
        user_input = input(message) or default_value
        alert, user_input = ask_user_alert(user_input, type_var)

    return user_input


def ask_user_alert(response, type_var):
    try:
        response = type_var(response)
        if response != "":
            alert = False
        else:
            alert = True
            print("--> Please enter none empty element")
    except:
        print("--> Please enter a " + str(type_var) + " value")
        alert = True
    return alert, response


def date_time_controller(user_input, format_date):
    while type(user_input) != datetime:
        try:
            user_input = datetime.strptime(user_input, format_date)
        except:
            print("Please write date in this format : yyyy-mm-dd")
            user_input = ask_user('Enter tournament date start yyyy-mm-dd', str, "")
    return user_input

