game_map = {
    "ironwood": {
        "map": [['---', '---', '---', '---', '---', '---', '---', '---'],
                ['---', 'black market', '   ', 'north entrance', '   ', '---', '---', '---'],
                ['---', 'tavern', '   ', 'common area', '   ', 'well', 'sewer', '---'],
                ['---', '   ', 'common area', 'yggdrasil', 'common area', '   ', '---', '---'],
                ['---', 'house', 'magic shop', 'market', 'stairs', '   ', '---', '---'],
                ['---', 'house', 'blacksmith shop', '---', '   ', '---', '---', '---'],
                ['---', 'house', 'house', '---', 'house', '   ', 'house', '---'],
                ['---', 'west entrance', '   ', '---', 'fountain', 'park', 'town hall', '---'],
                ['---', '???', '---', 'barracks', 'house', 'south entrance', 'house', '---'],
                ['---', '---', '---', '---', '---', '---', '---', '---']],
        "data": {
            "random_encounter_chance": 0,
            "encounters": [],
            "move_time": 0,
            "visibility": 5,
            "music": "world2"
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
            "visibility": 5,
            "music": "None"
        }
    },

    "world": {
        "map": [['---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---'],
                ['---', 'the old woods', '   ', '   ', '   ', '---', '   ', '   ', '   ', '   ', '---', '---'],
                ['---', '   ', '   ', 'ironwood', '   ', '   ', '   ', '   ', '   ', 'the quarry', '   ', '---'],
                ['---', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '---'],
                ['---', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '---', '---', '---'],
                ['---', 'city of thieves', '   ', '   ', 'mount megalos', '   ', '   ', '   ', '   ', '   ', '   ', '---'],
                ['---', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '---'],
                ['---', '---', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '---'],
                ['---', '   ', '   ', '   ', '   ', '   ', '   ', '   ', 'riverfell ruins', '   ', '   ', '---'],
                ['---', '   ', 'the wastes', '   ', '   ', '   ', '   ', '   ', '   ', '---', '---', '---'],
                ['---', '   ', '---', '---', '---', '   ', '   ', '---', '---', '   ', '---', '---'],
                ['---', '---', '---', '---', '---', '   ', '---', '---', '---', '---', '---', '---'],
                ['---', '---', '---', '---', '---', '   ', '   ', 'tower of doom', '---', '---', '---', '---'],
                ['---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---']],
        "data": {
            "random_encounter_chance": 3,
            "encounters": ['goblin', 'goblin patrol', 'elite patrol'],
            "move_time": 1,
            "visibility": 5,
            "music": "world1"
        }
    },
    "mount megalos": {
        "map": [['---', '---', '---', '---', '---', '---', '---', '---', '---'],
                ['---', 'to the peak', '   ', '---', 'hot spring', '---', '---', 'hermit of\nthe mountain', '---'],
                ['---', '   ', '   ', '   ', '   ', '---', '---', '---', '---'],
                ['---', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '---'],
                ['---', 'big shiny rock', '   ', 'statue of megalos', '   ', '   ', '   ', '   ', '---'],
                ['---', '---', '---', 'scholar', '   ', '   ', '   ', 'enormous fossil', '---'],
                ['---', '---', 'enormous fossil', '   ', '   ', '   ', '   ', '   ', '---'],
                ['---', '---', '   ', '   ', '   ', '   ', '---', '   ', '---'],
                ['---', 'cave entrance', '   ', '---', 'mountain gate', '   ', '---', '   ', '---'],
                ['---', '---', '---', '---', '---', '---', '---', '---', '---']],
        "data": {
            "random_encounter_chance": 5,
            "encounters": ['goatman', 'elite patrol'],
            "move_time": 0,
            "visibility": 5,
            "music": "world1"
        }
    },

    "mount megalos peak": {
        "map": [['---', '---', '---', '---', '---', '---'],
                ['---', '   ', '   ', 'corpse of king megalos', '   ', '---'],
                ['---', '   ', '   ', '   ', '   ', '---'],
                ['---', '   ', '---', '   ', '   ', '---'],
                ['---', '---', '   ', '   ', '---', '---'],
                ['---', '   ', '---', 'to the foot', '---', '---'],
                ['---', '---', '---', '---', '---', '---']],
        "data": {
            "random_encounter_chance": 0,
            "encounters": [],
            "move_time": 0,
            "visibility": 5,
            "music": "None"
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
            "encounters": ['spider', 'spiders'],
            "move_time": 0,
            "visibility": 5,
            "music": "world1"
        }
    },

    "city of thieves": {
        "map": [['---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---'],
                ['---', '---', '---', '---', 'thieves guild', '   ', '   ', '   ', '   ', '---', '---', '---'],
                ['---', 'house', '---', '   ', '---', '---', '   ', 'house', 'house', '   ', '---', '---'],
                ['---', 'house', 'house', '---', '---', '   ', '   ', 'house', '---', '---', '   ', '---'],
                ['---', '---', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', 'market', '---'],
                ['---', 'market', '---', '---', '---', '---', '   ', '   ', '   ', '   ', '   ', '---'],
                ['---', '   ', '---', '   ', 'tavern', '---', '   ', '   ', '   ', '   ', '   ', '---'],
                ['---', '---', '   ', '---', '   ', '   ', '   ', '   ', 'market', 'fountain', '   ', '---'],
                ['---', '---', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '---'],
                ['---', '   ', '   ', '   ', '   ', '   ', '   ', 'house', '   ', '   ', '   ', '---'],
                ['---', 'pile of garbage', '   ', 'sheriff office', 'house', 'house', 'house', '   ', 'market', 'house', 'house', '---'],
                ['---', '---', '   ', '   ', '   ', '   ', '   ', '   ', 'house', 'house', '   ', '---'],
                ['---', '---', '   ', '---', '---', '   ', '   ', '   ', '   ', '   ', '   ', '---'],
                ['---', '   ', '   ', '---', '---', '---', '---', '---', 'stairs', '---', '   ', '---'],
                ['---', '---', '   ', 'entrance', '---', '---', '---', '---', 'dock', '---', '---', '---'],
                ['---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---']],
        "data": {
            "random_encounter_chance": 4,
            "encounters": ['bandit ambush', 'spider'],
            "move_time": 0,
            "visibility": 5,
            "music": "world2"
            }
    },

    "the wastes": {
        "map": [['---', '---', '---', '---', '---', '---', '---', '---', '---', '---'],
                ['---', 'graveyard', '   ', '---', '   ', '---', '   ', '   ', '---', '---'],
                ['---', '   ', '   ', '   ', 'mausoleum', '---', '---', '   ', '---', '---'],
                ['---', '   ', 'the bog', '   ', '   ', '   ', '   ', '   ', '   ', '---'],
                ['---', '   ', '   ', '   ', '   ', '---', '   ', '---', '   ', '---'],
                ['---', '   ', '   ', '   ', '   ', 'dilapidated hut', '   ', '   ', '---', '---'],
                ['---', '   ', 'graveyard', '   ', '   ', '   ', '   ', '---', '---', '---'],
                ['---', 'pile of candles', '---', '---', '---', '   ', '   ', '   ', '---', '---'],
                ['---', '---', '---', '---', '---', '   ', '   ', '   ', '   ', '---'],
                ['---', '---', '---', '---', 'entrance', '   ', 'sister of the lost', '   ', '---', '---'],
                ['---', '---', '---', '---', '---', '---', '---', '---', '---', '---']],
        "data": {
            "random_encounter_chance": 8,
            "encounters": ['skeleton', 'wastes', 'wastes2', 'wastes3', 'wastes4'],
            "move_time": 0,
            "visibility": 5,
            "music": "world1"
        }
    },

    "the quarry": {
        "map": [['---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---'],
                ['---', 'west entrance', '   ', '   ', '---', '---', '---', '   ', '---', '   ', '---', '---'],
                ['---', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', 'east entrance', '---'],
                ['---', '   ', '---', '   ', '---', '---', '   ', '   ', 'friendly gnome', '   ', '   ', '---'],
                ['---', 'abandoned dig site', '   ', 'old minecart', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '---'],
                ['---', '---', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '---', '---'],
                ['---', '   ', '---', '---', '   ', '---', 'the minotaur', '---', '   ', '   ', '   ', '---'],
                ['---', '---', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', 'abandoned dig site', '---'],
                ['---', '   ', '   ', '   ', '---', '   ', '   ', '   ', '---', '---', '   ', '---'],
                ['---', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '---'],
                ['---', 'root of yggdrasil', '---', '   ', 'pile of boulders', '   ', '   ', '---', '   ', '   ', '   ', '---'],
                ['---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---']],
        "data": {
            "random_encounter_chance": 5,
            "encounters": ['quarry', 'quarry2', 'quarry3', 'quarry4'],
            "move_time": 0,
            "visibility": 3,
            "music": "None"
        }
    },

    "tower of doom": {
        "map": [['---', '---', '---', '---', '---', '---', '---', '---', '---', '---'],
                ['---', 'entrance', '   ', '   ', '   ', '   ', '   ', '   ', 'magic elevator', '---'],
                ['---', '---', '---', '---', '---', '---', '---', '---', '---', '---']],
        "data": {
            "random_encounter_chance": 0,
            "encounters": [],
            "move_time": 0,
            "visibility": 5,
            "music": "None"
        }
    },

    "dark lord chamber": {
        "map": [['---', '---', '---'],
                ['---', 'the dark lord', '---'],
                ['---', '   ', '---'],
                ['---', '   ', '---'],
                ['---', '   ', '---'],
                ['---', 'entrance', '---'],
                ['---', '---', '---']],
        "data": {
            "random_encounter_chance": 0,
            "encounters": [],
            "move_time": 0,
            "visibility": 5,
            "music": "None"
        }
    },

}

rooms = {
    'ironwood': {
        "black market": {"description": "All the merchants stay in strategic spots to hide from guards.", "shop": "black market"},
        "north entrance": {"description": "The northern entrance to Ironwood. Can also be an exit.", "enter": [3, 2, "world"]},
        "tavern": {"description": "The cheers of drunk men echo throughout the night."},
        "common area": {"description": "Ancient paths and benches and arches said to be constructed by the first settlers."},
        "yggdrasil": {"description": "The oldest and biggest tree in town. Sitting next to it gives a great sense of calm."},
        "well": {"description": "The primary source of water for years to come."},
        "sewer": {"description": "A run-down sewer coming out of the side of a hill."},
        "house": {"description": "The place of dwelling for a citizen of Ironwood."},
        "market": {"description": "Stalls bustling with merchants looking to make a living."},
        "magic shop": {"description": "A peculiar shop with all sorts scents coming from it.", "shop": "dan's thingamabobs"},
        "blacksmith shop": {"description": "A humble blacksmith shop. You can feel the heat emanating from it.", "shop": "blacksmith"},
        "stairs": {"description": "Leads upwards to the richer neighbourhood and downwards to the poorer."},
        "west entrance": {"description": "The western entrance to Ironwood. Can also be an exit.", "enter": [3, 2, "world"]},
        "fountain": {"description": "Constructed by those with some knowledge in magic, the water flows unnaturally."},
        "park": {"description": "Has a pond with some ducks with benches surrounding it."},
        "south entrance": {"description": "The southern entrance to Ironwood. Can also be an exit.", "enter": [3, 2, "world"]},
        "restaurant": {"description": "this should be the description"},
        "barracks": {"description": "Houses guards and soldiers in training."},
        "townhall": {"description": "Where Lord Svallen works tirelessly for the people of Ironwood."},
        "???": {"description": "???"}
    },
    "city of thieves": {
        "entrance": {"description": "An unmanned gate.", "enter": [1, 5, "world"]},
        "house": {"description": "Centuries of break-ins have rendered the doors and windows utterly useless."},
        "market": {"description": "In any other city, this would be called a black market."},
        "pile of garbage": {"description": "A reeking pile of filth and trash."},
        "sheriff office": {"description": "The front door is covered in blood. There's a 'now hiring' sign hanging from it."},
        "stairs": {"description": "These stairs lead up to the docks."},
        "dock": {"description": "The dock is lined with pirate ships."},
        "tavern": {"description": "Drunkards are hanging from the windows, on the tables, and sprawled on the street."},
        "fountain": {"description": "Unsurprisingly, this fountain doesn't have any coins in it."},
        "thieves guild": {"description": "The dark underbelly of this already dark city. The king doesn't take kindly to strangers.", "fight": 'king of thieves'},
    },
    "world": {
        "ironwood" : {"description": "The peaceful capital of Sveragard", "enter": [3, 1, 'ironwood']},
        "the old woods" : {"description": "An ancient curse echoes...", "enter": [2, 25, 'the old woods']},
        "mount megalos" : {"description": "The foot of an impossibly tall mountain.", "enter": [4, 8, 'mount megalos']},
        "city of thieves" : {"description": "A city built on a legacy of cutthroat thievery.", "enter": [3, 14, 'city of thieves']},
        "the wastes" : {"description": "A desolate, toxic swamp that doesn't take kindly to outsiders.", "enter": [4, 9, 'the wastes']},
        "the quarry" : {"description": "A mineshaft long sealed due to unstable dark energy.", "enter": [10, 2, 'the quarry']},
        "tower of doom" : {"description": "The heart of this world's disasters. Enter if you dare...", "enter": [1, 1, 'tower of doom']},
        "riverfell ruins" : {"description": "The ruins of what was once a beautiful city."}
    },
    "tutorial": {
        "spirit gate" : {"description": "This gate leads to the real world...", "enter": [3, 3, "ironwood"]},
    },
    "the old woods": {
        "forest entrance" : {"description": "The only place where the woods aren't suffocatingly dense.", "enter": [1, 1, "world"]},
        "gangly tree" : {"description": '"My, my, a visitor? In this part of the woods?"'},
        "shy tree" : {"description": '"H-hey! Go away!"'},
        "ancient tree" : {"description": '"You should not be here, traveler... The woods are in pain..."'},
        "wise tree" : {"description": '"Something is poisoning the forest..."'},
        "sickly tree" : {"description": '"Please... that thing is killing us..."'},
        "entrepreneurial tree" : {"description": 'This tree has bent itself into a makeshift shop table.', "shop": "tree's shop"},
        "tumor of the forest": {"description": "A pulsating purple mass, sucking the life out of the surrounding forest.", "fight": 'tumor of the forest'}
    },
    "mount megalos": {
        "mountain gate": {"description": "The entrance to mount megalos.", "enter": [4, 5, "world"]},
        "to the peak": {"description": "An unfathomably tall staircase going to the peak of the mountain.", "enter": [3, 5, "mount megalos peak"]},
        "big shiny rock": {"description": "A rock. Big and shiny. Big shiny rock."},
        "hot springs": {"description": "Maybe if the world wasn't ending you'd have time to relax here."},
        "enormous fossil": {"description": "You shudder to imagine what kind of creature this once was."},
        "statue of megalos": {"description": "A statue depicting a long lost king."},
        "cave entrance": {"description": "A yawning chasm beckons you to enter.", "enter": [1, 1, "the quarry"]},
        "scholar" : {"description": 'He is frantically scribbling things down on paper.', "shop": "scholar"},
    },

    "mount megalos peak": {
        "corpse of king megalos": {"description": "The dead king beckons you to fight.", "fight": "king megalos"},
        "to the foot": {"description": "An unfathomably tall staircase going to the foot of the mountain.", "enter": [1, 1, "mount megalos"]},
    },

    "the quarry": {
        "friendly gnome": {"description": "The gnome seems like he has something to sell you.", "shop": "gnome"},
        "east entrance": {"description": "The light at the end of the tunnel.", "enter": [9, 2, "world"]},
        "west entrance": {"description": "The tunnel is painted with murals depicting some important figure.", "enter": [1, 8, "mount megalos"]},
        "the minotaur": {"description": "The minotaur stands before you.", "fight": "the minotaur"},
        "abandoned dig site": {"description": "Some old and tattered tents are still set up here."},
        "pile of boulders": {"description": "It looks like a deadly cave-in happened here."},
        "old minecart": {"description": "Was probably once used to haul rocks to the surface"},
        "root of yggdrasil": {"description": "The root emits a lovely natural light."},
    },

    "the wastes": {
        "entrance": {"description": "Exits the wastes. Probably the best choice.", "enter": [2, 9, "world"]},
        "sister of the lost": {"description": "A woman covered head to toe in black leather garments is humming.", "shop": "sister of the lost"},
        "graveyard": {"description": "Looks incredibly ancient. Somehow feels slightly peaceful."},
        "pile of candles": {"description": "Despite the howling winds, the candles are all still lit."},
        "mausoleum": {"description": "The building has been totally boarded up. 'THE DEAD WILL RETURN' is etched on it."},
        "dilapidated hut": {"description": "Has been utterly claimed by the wastes. Vine tendrils are pulling it into the ground."},
        "the bog": {"description": "A gurgling pool of purple liquid. Something is in there...", "fight": 'hideous bogman'}
    },

    "tower of doom": {
        "entrance": {"description": "A massive ornate door.", "enter": [7, 12, "world"]},
        "magic elevator": {"description": "A small circular platform that can carry you to the upper level.", "enter": [1, 5, "dark lord chamber"]},
    },

    "dark lord chamber": {
        "the dark lord": {"description": "The end of this adventure.", "fight": "the dark lord"},
        "entrance": {"description": "Leads back to the lower level of the tower.", "enter": [8, 1, "tower of doom"]},
    }
}
