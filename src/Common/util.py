import json
from os import read

from Common import constants

def read_settings():
    with open(constants.SETTINGS_PATH, encoding='utf-8') as f:
        settings = json.load(f)
    return settings

def get_excel_settings():
    settings = read_settings()
    return settings['excel_settings']

def get_mail_settings():
    settings = read_settings()
    return settings['mail_settings']

def save_settings(settings):
    with open(constants.SETTINGS_PATH, 'w', encoding='utf-8') as f:
        json.dump(settings, f, indent=4)