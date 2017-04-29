__author__ = 'KTGoldwolf'

import json
import requests
import config
import random

champions = {}
names = {}
marksman = {}
mage = {}
fighter = {}
tank = {}
assassin = {}
support = {}
loaded = False


def get_raw_champion_data():
    rawdata = requests.get(config.CHAMP_DATA)
    data = json.loads(rawdata.content.decode())
    global champions
    global loaded
    champions = data.get("data")
    print("Loaded champion data!")
    loaded = True
    return champions


def reload():
    get_raw_champion_data()


def load_champion_data():
    if loaded is False:
        get_raw_champion_data()
    data = champions
    for champion in data:
        internal_name = champion
        proper_name = data.get(champion).get("name")
        tags = data.get(champion).get("tags")
        entry = {
            "internal_name": internal_name,
            "proper_name": proper_name,
            "tags": tags
        }
        names[internal_name] = entry
        if "Mage" in tags:
            mage[internal_name] = entry
        if "Tank" in tags:
            tank[internal_name] = entry
        if "Assassin" in tags:
            assassin[internal_name] = entry
        if "Support" in tags:
            support[internal_name] = entry
        if "Fighter" in tags:
            fighter[internal_name] = entry
        if "Marksman" in tags:
            marksman[internal_name] = entry
    return names


def get_random_champion_name():
    if loaded is False:
        get_raw_champion_data()
    names = load_champion_data()
    return names[random.choice(list(names))]

def get_random_marksman():
    if loaded is False:
        get_raw_champion_data()
    return marksman[random.choice(list(marksman))]


def get_random_mage():
    if loaded is False:
        get_raw_champion_data()
    return mage[random.choice(list(mage))]

def get_random_fighter():
    if loaded is False:
        get_raw_champion_data()
    return fighter[random.choice(list(fighter))]


def get_random_tank():
    if loaded is False:
        get_raw_champion_data()
    return tank[random.choice(list(tank))]


def get_random_assassin():
    if loaded is False:
        get_raw_champion_data()
    return assassin[random.choice(list(assassin))]

def get_random_support():
    if loaded is False:
        get_raw_champion_data()
    return support[random.choice(list(support))]

def get_a_quip():
    quips = config.QUIPS
    return random.choice(quips)