import os
basedir = os.path.abspath(os.path.dirname(__file__))

STATS = {
    "armor pen": "armorperlevel",
    "ad": "attackdamage",
    "mpen per level": "mpperlevel",
    "attack speed offset": "attackspeedoffset",
    "mpen": "mp",
    "armor": "armor",
    "hp": "hp",
    "health regen per level": "hpregenperlevel",
    "attack speed per level": "attackspeedperlevel",
    "attack range": "attackrange",
    "move speed": "movespeed",
    "ad per level": "attackdamageperlevel",
    "mana regen per level": "mpregenperlevel",
    "crit per level": "critperlevel",
    "mr per level": "spellblockperlevel",
    "crit": "crit",
    "mana regen": "mpregen",
    "mr": "spellblock",
    "hp regen": "hpregen",
    "hp per level": "hpperlevel",
}

QUIPS = [
    "This will carry you at least all the way to Silver III.",
    "The gods of randomness have spoken.",
    "Was there really any other option?",
    "I think this is your new main.",
    "I heard this is the secret OP pick."
]

TAGS = [
    "Mage",
    "Tank",
    "Assassin",
    "Support",
    "Fighter",
    "Marksman"
]

CHAMP_DATA = "http://ddragon.leagueoflegends.com/cdn/6.24.1/data/en_US/champion.json"

OPGG_URL = "https://na.op.gg"