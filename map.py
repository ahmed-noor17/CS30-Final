map_file = 'map.txt'
from tabulate import tabulate
from main import player_pos

game_map = {
    "house": [['', '', '', '', '', ''],
            ['', None, "backyard", None, None, ''],
            ['', "dining room", "back door", "lounge", None, ''],
            ['', "kitchen", "hallway", "stairwell", None, ''],
            ['', "living room", "foyer", "bedroom", None, ''],
            ['', "bathroom", "entrance hall", "laundry room", "garage", ''],
            ['', '', '', '', '', '']],

    "dungeon": [['', '', '', '', '', '', ''],
        ['', 'witchery room', 'warden office', 'orb vault', 'meeting room', 'dungeon guard room', ''],
        ['', 'experimentation room', 'equipment room', 'hallway', 'dark room', 'solitary confinement', ''],
        ['', 'library', 'hallway', 'stairwell', 'hallway', 'the gargoyle', ''],
        ['', 'portal room', 'workshop', 'hallway', 'prison cell', 'torture room', ''],
        ['', 'chapel','summoning room', 'entrance', 'prison cell', 'prison cell', ''],
        ['', '', '', '', '', '', '']]
}

rooms = {
    "kitchen": {"description": "The kitchen is very tidy."},
    "dining room": {"description": "There is a table and many chairs."},
    "stairwell": {"description": "There is a large staircase."},
    "living room": {"description": "The TV is playing something."},
    "foyer": {"description": "Paintings hang on the walls around you."},
    "bedroom": {"description": "The room is very messy."},
    "bathroom": {"description": "The sink is running."},
    "entrance hall": {"description": "The front door is locked."},
    "garage": {"description": "There are no cars in the garage."},
    "laundry room": {"description": "There are no cars in the garage."},
    "back door": {"description": "This door leads to the dungeon.", "connections": [2, 4, "dungeon"]},
    "hallway": {"description": "A long carpet is rolled out on the floor."},
    "backyard": {"description": "The sun is shining and a peaceful breeze is blowing."},
    "witchery room": {"description": "there's a cauldron and many odd looking plants."},
    "warden office": {"description": "there's a singular desk with a light above, and some paperwork in a scripture you don't recognize."},
    "orb vault": {"description": "you do not what's in the orb vault, but you can sense an orb in there..."},
    "meeting room": {"description": "there's a singular desk with many chairs around."},
    "dungeon guard room": {"description": "there's a few bunk beds around and a game of monopoly on a nightstand."},
    "experimentation room": {"description": "there's a surgical desk with blood all around and some strange tools."},
    "equipment room": {"description": "it seems this is where the guards keep their equipment..."},
    "dark room": {"description": "it is pitch black inside this room, your eyes make out some odd shapes in the corners of the room. You feel a presence looming over you..."},
    "solitary confinement":{"description": "a singular skeleton rests hanged by chains on the wall of this dimly lit room."},
    "library": {"description": "it seems this is where they kept records of experiments. You cannot make sense of any of it."},
    "stairwell": {"description": "it leads upwards, into the darkness. Perhaps you shouldn't venture more..."},
    "the gargoyle": {"description": "a stone statue of a gargoyle pierces your soul with its stare inside this room"},
    "portal room": {"there's a portal on the wall. You do not know where it leads."},
    "workshop": {"description": "there are many unfamiliar tools here, it seems to be a workshop."},
    "prison cell": {"description": "it looks like your average jail cell. "},
    "entrance": {"description": "this leads to your house.", "connections": [1, 4, "house"]},
    "chapel": {"description": "this room seems it's where they worshipped someone... or something...?"},
    "summoning room": {"description": "there's an ominous summoning circle in the middle of the room with candles surrounding it."}
    }


def write_map():
    ''' Function will write map to a file.'''
    try:
        with open(map_file, 'w') as file:
            file.write(tabulate(game_map, tablefmt="grid"))
    except Exception:
        print("Failure to write map.")
    else:
        print("You look at your map.")
    finally:
        read_map()


def read_map():
    try:
        with open(map_file, 'r') as f:
            map = f.read()
    except Exception:
        print("You could not read your map.")
    else:
        print(map)
    finally:
        print("This is the map.")