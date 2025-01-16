game_map = {
    "house": {
        "map": [['---', '---', '---', '---', '---', '---'],
                ['---', '---', "backyard", '---', '---', '---'],
                ['---', "dining room", "back door", "lounge", '---', '---'],
                ['---', "kitchen", "hallway", "stairwell", '---', '---'],
                ['---', "living room", "foyer", "bedroom", '---', '---'],
                ['---', "bathroom", "entrance hall", "laundry room", "garage", '---'],
                ['---', '---', '---', '---', '---', '---']],
        "data": {
            "random_encounter_chance": 0,
            "encounters": [],
            "move_time": 0,
            "visibility": 5
        }
    },

    "dungeon": {
        "map": [['---', '---', '---', '---', '---', '---', '---'],
                ['---', 'witchery room', 'warden office', 'orb vault', 'meeting room', 'dungeon guard room', '---'],
                ['---', 'experimentation room', 'equipment room', 'hallway', 'dark room', 'solitary confinement', '---'],
                ['---', 'library', 'hallway', 'stairwell', 'hallway', 'the gargoyle', '---'],
                ['---', 'portal room', 'workshop', 'hallway', 'prison cell', 'torture room', '---'],
                ['---', 'chapel','summoning room', 'entrance', 'prison cell', 'prison cell', '---'],
                ['---', '---', '---', '---', '---', '---', '---']],
        "data": {
            "random_encounter_chance": 50,
            "encounters": ['dungeon1', 'dungeon2', 'dungeon3', 'dungeon4', 'spider'],
            "move_time": 0,
            "visibility": 5
        }
    },

    "ironwood": {
        "map": [['---', '---', '---', '---', '---', '---', '---', '---'],
                ['---', 'black market', '   ', 'north entrance', '   ', '---', '---', '---'],
                ['---', 'tavern', '   ', 'common area', '   ', 'well', 'sewer entrance', '---'],
                ['---', '   ', 'common area', 'yggdrasil', 'common area', '   ', '---', '---'],
                ['---', 'house', 'market', 'market', 'stairs', '   ', '---', '---'],
                ['---', 'house', 'market', '---', '   ', '---', '---', '---'],
                ['---', 'house', 'house', '---', 'house', '   ', 'house', '---'],
                ['---', 'west entrance', '   ', '---', 'fountain', 'park', 'town hall', '---'],
                ['---', '???', '---', 'barracks', 'house', 'south entrance', 'house', '---'],
                ['---', '---', '---', '---', '---', '---', '---', '---']],
        "data": {
            "random_encounter_chance": 0,
            "encounters": [],
            "move_time": 0,
            "visibility": 5
        }
    },

    "tutorial": {
        "map": [['---', '---', '---'],
                ['---', 'spirit gate', '---'],
                ['---', '   ', '---'],
                ['---', '   ', '---'],
                ['---', '---', '---']],
        "data": {
            "random_encounter_chance": 0,
            "encounters": [],
            "move_time": 0,
            "visibility": 5
        }
    },

    "world": {
        "map": [['---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---'],
                ['---', 'the old woods', '   ', '   ', '   ', '---', '   ', '   ', '   ', 'the quarry', '---', '---'],
                ['---', '   ', '   ', 'ironwood', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '---'],
                ['---', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '---'],
                ['---', '   ', '   ', '   ', 'mount megalos', '   ', '   ', '   ', '   ', '---', '---', '---'],
                ['---', 'city of thieves', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '---'],
                ['---', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '---'],
                ['---', '---', '   ', '   ', '   ', '   ', 'riverfell', '   ', '   ', '   ', '   ', '---'],
                ['---', '---', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '---'],
                ['---', '   ', '   ', 'ancient monument', '   ', '   ', '   ', 'great lake', '   ', '   ', '   ',  '---'],
                ['---', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '---'],
                ['---', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '---'],
                ['---', '   ', 'the wastes', '   ', '   ', '   ', '   ', '   ', '   ', '---', '---', '---'],
                ['---', '---', '---', '---', '---', '   ', '---', '---', '---', '---', '---', '---'],
                ['---', '---', '---', '---', '---', '   ', '---', '---', '---', '---', '---', '---'],
                ['---', '---', '---', '---', '---', '   ', '   ', 'tower of doom', '---', '---', '---', '---'],
                ['---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---']],
        "data": {
            "random_encounter_chance": 3,
            "encounters": ['goblin', 'goblin patrol', 'elite patrol'],
            "move_time": 0.5,
            "visibility": 5
        }
    },
    "mount megalos": {
        "map": [['---', '---', '---', '---', '---', '---', '---', '---', '---'],
                ['---', 'to the peak', '   ', '---', 'hot spring', '---', '---', 'hermit of\nthe mountain', '---'],
                ['---', '   ', '   ', '   ', '   ', '---', '---', '---', '---'],
                ['---', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '---'],
                ['---', 'big shiny rock', '   ', 'statue of megalos', '   ', '   ', '   ', '   ', '---'],
                ['---', '---', '---', '   ', '   ', '   ', '   ', 'enormous fossil', '---'],
                ['---', '---', 'enormous fossil', '   ', '   ', '   ', '   ', '   ', '---'],
                ['---', '---', '   ', '   ', '   ', '   ', '---', '   ', '---'],
                ['---', 'cave entrance', '   ', '---', 'mountain gate', '   ', '---', '   ', '---'],
                ['---', '---', '---', '---', '---', '---', '---', '---', '---']],
        "data": {
            "random_encounter_chance": 0,
            "encounters": [],
            "move_time": 0,
            "visibility": 5
        }
    },
    "the old woods": {
        "map": [['---', '---', '---', '---', '---', '---', '---', '---'],
                ['---', 'tumor of the forest', '   ', '   ', '   ', '---', '---', '---'],
                ['---', '   ', '   ', '   ', '   ', '   ', '---', '---'],
                ['---', '   ', 'sickly tree', '   ', '   ', 'wise tree', '   ', '---'],
                ['---', '   ', '   ', '   ', '   ', '   ', '   ', '---'],
                ['---', '---', '---', '   ', '---', '   ', '---', '---'],
                ['---', '---', '   ', '   ', '   ', '   ', '   ', '---'],
                ['---', '---', '   ', '---', '---', '   ', '   ', '---'],
                ['---', '---', '   ', '   ', '   ', '   ', '   ', '---'],
                ['---', '   ', '   ', '   ', '   ', 'entrepreneurial tree', '   ', '---'],
                ['---', '   ', '   ', '   ', '   ', '   ', '   ', '---'],
                ['---', '   ', 'ancient tree', '   ', '   ', '   ', '   ', '---'],
                ['---', '   ', '   ', '   ', '   ', '   ', '   ', '---'],
                ['---', '   ', '   ', '   ', '---', '   ', '   ', '---'],
                ['---', '   ', '   ', '   ', '---', '   ', '---', '---'],
                ['---', '   ', '   ', '   ', '   ', '---', '---', '---'],
                ['---', 'shy tree', '---', '   ', '   ', '   ', '---', '---'],
                ['---', '---', '---', '   ', '   ', '---', '---', '---'],
                ['---', '---', '   ', '   ', '   ', '   ', '---', '---'],
                ['---', '   ', '---', '   ', '   ', '   ', '   ', '---'],
                ['---', '---', '   ', '   ', '   ', '   ', '   ', '---'],
                ['---', '   ', 'gangly tree', '   ', '   ', '   ', '---', '---'],
                ['---', '   ', '   ', '   ', '   ', '---', '---', '---'],
                ['---', '   ', '   ', '   ', '   ', '   ', '---', '---'],
                ['---', '---', '   ', '   ', '   ', '   ', '   ', '---'],
                ['---', '---', 'forest entrance', '---', '   ', '---', '---', '---'],
                ['---', '---', '---', '---', '---', '---', '---', '---']],
        "data": {
            "random_encounter_chance": 8,
            "encounters": ['spider'],
            "move_time": 0,
            "visibility": 5
        }
    },

    "city of thieves": {
    "map": [['---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---'],
            ['---', '---', '---', '---', '   ', '   ', '   ', '   ', '   ', '---', '---', '---', '---', '---', '---', '---', '---'],
            ['---', '   ', '---', '   ', '---', '---', '   ', '   ', '   ', '   ', '---', '---', '---', '---', '---', '---', '---'],
            ['---', '   ', '   ', '---', '---', '   ', '   ', '   ', '---', '---', '   ', '   ', '   ', '   ', '   ', '---', '---'],
            ['---', '---', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '---', '---', '---', '---', '---', '---', '---', '---'],
            ['---', '---', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '---'],
            ['---', '   ', '---', '---', '---', '---', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '---'],
            ['---', '   ', '---', '   ', '   ', '---', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '---'],
            ['---', '---', '   ', '---', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '---'],
            ['---', '---', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '---', '   ', '---', '---', '---'],
            ['---', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '---', '---', '---', '---'],
            ['---', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '---'],
            ['---', '---', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '---'],
            ['---', '---', '   ', '---', '---', '   ', '   ', '   ', '   ', '   ', '   ', '---', '---', '---', '   ', '---', '---'],
            ['---', '   ', '   ', '---', '---', '---', '---', '---', '   ', '---', '   ', '   ', '   ', '   ', '   ', '   ', '---'],
            ['---', '---', '   ', '   ', '---', '---', '---', '---', '   ', '---', '---', '---', '   ', '---', '   ', '   ', '---'],
            ['---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---']],
    "data": {
        "random_encounter_chance": 0,
        "encounters": [],
        "move_time": 0,
        "visibility": 5
        }
    }

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
        "hallway": {"description": "A long carpet is rolled out on the floor."},
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
        "black market": {"description": "All the merchants stay in strategic spots to hide from guards.", "shop": "black market"},
        "north entrance": {"description": "The northern entrance to Ironwood. Can also be an exit.", "connections": [3, 2, "world"]},
        "tavern": {"description": "The cheers of drunk men echo throughout the night."},
        "common area": {"description": "Ancient paths and benches and arches said to be constructed by the first settlers."},
        "yggdrasil": {"description": "The oldest and biggest tree in town. Sitting next to it gives a great sense of calm."},
        "well": {"description": "The primary source of water for years to come."},
        "sewer entrance": {"description": "A run-down wooden door on the side of a hill and a sewer on the other side."},
        "house": {"description": "The place of dwelling for a citizen of Ironwood."},
        "market": {"description": "Stalls bustling with merchants looking to make a living.", "shop": "dan's thingamabobs"},
        "stairs": {"description": "Leads upwards to the richer neighbourhood and downwards to the poorer."},
        "west entrance": {"description": "The western entrance to Ironwood. Can also be an exit.", "connections": [3, 2, "world"]},
        "fountain": {"description": "Constructed by those with some knowledge in magic, the water flows unnaturally."},
        "park": {"description": "Has a pond with some ducks with benches surrounding it."},
        "south entrance": {"description": "The southern entrance to Ironwood. Can also be an exit.", "connections": [3, 2, "world"]},
        "restaurant": {"description": "this should be the description"},
        "barracks": {"description": "Houses guards and soldiers in training."},
        "townhall": {"description": "Where Lord Svallen works tirelessly for the people of Ironwood."},
        "???": {"description": "???"}},
    "world": {
        "ironwood" : {"description": "ironwood", "connections": [3, 1, 'ironwood']},
        "the old woods" : {"description": "an ancient curse echoes...", "connections": [2, 25, 'the old woods']},
        "mount megalos" : {"description": "the foot of an impossibly tall mountain.", "connections": [4, 8, 'mount megalos']}
    },
    "tutorial": {
        "spirit gate" : {"description": "This gate leads to the real world...", "connections": [3, 3, "ironwood"]},
        },
    "the old woods": {
        "forest entrance" : {"description": "The only place where the woods aren't suffocatingly dense.", "connections": [1, 1, "world"]},
        "gangly tree" : {"description": '"My, my, a visitor? In this part of the woods?"'},
        "shy tree" : {"description": '"H-hey! Go away!"'},
        "ancient tree" : {"description": '"You should not be here, traveler... The woods are in pain..."'},
        "wise tree" : {"description": '"Something is poisoning the forest..."'},
        "sickly tree" : {"description": '"Please... that thing is killing us..."'},
        "entrepreneurial tree" : {"description": 'This tree has bent itself into a makeshift shop table.', "shop": "tree's shop"},
        "tumor of the forest": {"description": "A pulsating purple mass, sucking the life out of the surrounding forest.", "fight": 'tumor of the forest'}
        }
    }
