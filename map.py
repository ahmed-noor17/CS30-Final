map_file = 'map.txt'
from tabulate import tabulate

game_map = {
    "house": [['X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', "backyard", 'X', 'X', 'X'],
            ['X', "dining room", "back door", "lounge", 'X', 'X'],
            ['X', "kitchen", "hallway", "stairwell", 'X', 'X'],
            ['X', "living room", "foyer", "bedroom", 'X', 'X'],
            ['X', "bathroom", "entrance hall", "laundry room", "garage", 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X']],

    "dungeon": [['X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'witchery room', 'warden office', 'orb vault', 'meeting room', 'dungeon guard room', 'X'],
        ['X', 'experimentation room', 'equipment room', 'hallway', 'dark room', 'solitary confinement', 'X'],
        ['X', 'library', 'hallway', 'stairwell', 'hallway', 'the gargoyle', 'X'],
        ['X', 'portal room', 'workshop', 'hallway', 'prison cell', 'torture room', 'X'],
        ['X', 'chapel','summoning room', 'entrance', 'prison cell', 'prison cell', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X']],

    "ironwood": [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'black market', '', 'north entrance', '', 'X', 'X', 'X'],
        ['X', 'tavern', '', 'common area', '', 'well', 'sewer entrance', 'X'],
        ['X', 'house', 'market', 'market', 'stairs', '', 'X', 'X'],
        ['X', 'house', 'market', 'X', '', 'X', 'X', 'X'],
        ['X', 'house', 'house', 'X', 'house', '', 'restaurant', 'X'],
        ['X', 'west entrance', '', 'X', 'fountain', '', 'barracks', 'X'],
        ['X', '???', 'X', 'house', '', 'townhall', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]
}

rooms = {
    'house': {
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
        "backyard": {"description": "The sun is shining and a peaceful breeze is blowing."}},
    'dungeon': {
        "witchery room": {"description": "There's a cauldron and many odd looking plants."},
        "warden office": {"description": "There's a singular desk with a light above, and some paperwork in a scripture you don't recognize."},
        "orb vault": {"description": "You do not what's in the orb vault, but you can sense an orb in there..."},
        "meeting room": {"description": "There's a singular desk with many chairs around."},
        "dungeon guard room": {"description": "There's a few bunk beds around and a game of monopoly on a nightstand."},
        "experimentation room": {"description": "There's a surgical desk with blood all around and some strange tools."},
        "equipment room": {"description": "It seems this is where the guards keep their equipment..."},
        "dark room": {"description": "It is pitch black inside this room, your eyes make out some odd shapes in the corners of the room. You feel a presence looming over you..."},
        "solitary confinement":{"description": "A singular skeleton rests hanged by chains on the wall of this dimly lit room."},
        "library": {"description": "It seems this is where they kept records of experiments. You cannot make sense of any of it."},
        "stairwell": {"description": "It leads upwards, into the darkness. Perhaps you shouldn't venture more..."},
        "the gargoyle": {"description": "A stone statue of a gargoyle pierces your soul with its stare inside this room"},
        "portal room": {"description": "There's a portal on the wall. You do not know where it leads."},
        "workshop": {"description": "There are many unfamiliar tools here, it seems to be a workshop."},
        "prison cell": {"description": "It looks like your average jail cell. "},
        "entrance": {"description": "This leads to your house.", "connections": [1, 4, "house"]},
        "chapel": {"description": "This room seems it's where they worshipped someone... or something...?"},
        "summoning room": {"description": "There's an ominous summoning circle in the middle of the room with candles surrounding it."}},
    'ironwood': {
        "black market": {"description": "this should be the description"},  # Ironwood
        "north entrance": {"description": "this should be the description"},
        "tavern": {"description": "this should be the description"},
        "common area": {"description": "this should be the description"},
        "well": {"description": "this should be the description"},
        "sewer entrance": {"description": "this should be the description"},
        "house": {"description": "this should be the description"},
        "market": {"description": "this should be the description"},
        "stairs": {"description": "this should be the description"},
        "west entrance": {"description": "this should be the description"},
        "fountain": {"description": "this should be the description"},
        "restaurant": {"description": "this should be the description"},
        "barracks": {"description": "this should be the description"},
        "townhall": {"description": "this should be the description"},
        "???": {"description": "???"}},
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