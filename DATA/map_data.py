game_map = {
    "ironwood": {
        "map": [['---', '---', '---', '---', '---', '---', '---', '---'],
                ['---', 'black market', '   ', 'north entrance', '   ', '---', '---', '---'],
                ['---', 'tavern', '   ', 'common area', '   ', 'well', 'sewer entrance', '---'],
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

    "sewer": {
        "map": [['---', '---', '---', '---', '---', '---', '---', '---', '---', '---'],
                ['---', 'to ironwood', '   ', '   ', '   ', '   ', '   ', '   ', 'mysterious door', '---'],
                ['---', '---', '---', '---', '---', '---', '---', '---', '---', '---']],
        "data": {
            "random_encounter_chance": 0,
            "encounters": [],
            "move_time": 0,
            "visibility": 5,
            "music": "None"
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
                ['---', '   ', '   ', '   ', '   ', '   ', '   ', '   ', 'riverfell', '   ', '   ', '---'],
                ['---', '   ', 'the wastes', '   ', '   ', '   ', '   ', '   ', '   ', '---', '---', '---'],
                ['---', '   ', '---', '---', '---', '   ', '   ', '---', '---', '   ', '---', '---'],
                ['---', '---', '---', '---', '---', '   ', '---', '---', '---', '---', '---', '---'],
                ['---', '---', '---', '---', '---', '   ', '   ', 'tower of doom', '---', '---', '---', '---'],
                ['---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---']],
        "data": {
            "random_encounter_chance": 3,
            "encounters": ['goblin', 'goblin patrol', 'elite patrol'],
            "move_time": 0.5,
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
                ['---', '---', '---', '   ', '   ', '   ', '   ', 'enormous fossil', '---'],
                ['---', '---', 'enormous fossil', '   ', '   ', '   ', '   ', '   ', '---'],
                ['---', '---', '   ', '   ', '   ', '   ', '---', '   ', '---'],
                ['---', 'cave entrance', '   ', '---', 'mountain gate', '   ', '---', '   ', '---'],
                ['---', '---', '---', '---', '---', '---', '---', '---', '---']],
        "data": {
            "random_encounter_chance": 0,
            "encounters": [],
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
            "encounters": ['spider'],
            "move_time": 0,
            "visibility": 5,
            "music": "world1"
        }
    },

    "city of thieves": {
        "map": [['---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---'],
                ['---', '---', '---', '---', 'thieves guild', '   ', '   ', '   ', '   ', '---', '---', '---', '---', '---', '---', '---', '---'],
                ['---', 'house', '---', '   ', '---', '---', '   ', 'house', 'house', '   ', '---', '---', '---', '---', '---', '---', '---'],
                ['---', 'house', 'house', '---', '---', '   ', '   ', 'house', '---', '---', '   ', '   ', '   ', '   ', '   ', '---', '---'],
                ['---', '---', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', 'market', '   ', '   ', 'house', 'house', '   ', '---'],
                ['---', 'black market', '---', '---', '---', '---', '   ', '   ', '   ', '   ', '   ', '   ', 'house', 'house', '   ', 'town hall', '---'],
                ['---', '   ', '---', '   ', 'tavern', '---', '   ', '   ', '   ', '   ', '   ', 'market', 'house', 'house', '   ', '   ', '---'],
                ['---', '---', '   ', '---', '   ', '   ', '   ', '   ', 'market', 'fountain', '   ', '   ', '   ', '   ', '   ', '   ', '---'],
                ['---', '---', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '---', '   ', '---', '---', '---'],
                ['---', '   ', '   ', '   ', '   ', '   ', '   ', 'house', '   ', '   ', '   ', '   ', '   ', '---', '---', '---', '---'],
                ['---', 'pile of garbage', '   ', 'tax office', 'house', 'house', 'house', '   ', 'market', 'house', 'house', '   ', '   ', '   ', '   ', '   ', '---'],
                ['---', '---', '   ', '   ', '   ', '   ', '   ', '   ', 'house', 'house', '   ', '   ', 'house', 'house', '   ', '   ', '---'],
                ['---', '---', '   ', '---', '---', '   ', '   ', '   ', '   ', '   ', '   ', '---', '---', '---', 'house', '---', '---'],
                ['---', '   ', '   ', '---', '---', '---', '---', '---', 'stairs', '---', '   ', '   ', '   ', 'house', 'house', 'house', '---'],
                ['---', '---', '   ', 'entrance', '---', '---', '---', '---', 'dock', '---', '---', '---', '   ', '---', 'house', 'house', '---'],
                ['---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---']],
        "data": {
            "random_encounter_chance": 3,
            "encounters": ['bandit ambush', 'spider'],
            "move_time": 0,
            "visibility": 5,
            "music": "world2"
            }
    },

    "the wastes": {
        "map": [['---', '---', '---', '---', '---', '---', '---', '---', '---', '---'],
                ['---', 'graveyard', '   ', '---', '   ', '---', '   ', '   ', '---', '---'],
                ['---', '   ', '   ', '   ', '   ', '---', '---', '   ', '---', '---'],
                ['---', '   ', 'the bog', '   ', '   ', '   ', '   ', '   ', '   ', '---'],
                ['---', '   ', '   ', '   ', '   ', '---', '   ', '---', '   ', '---'],
                ['---', '   ', '   ', '   ', '   ', 'dilapidated hut', '   ', '   ', '---', '---'],
                ['---', '   ', 'graveyard', '   ', '   ', '   ', '   ', '---', '---', '---'],
                ['---', '   ', '---', '---', '---', '   ', '   ', '   ', '---', '---'],
                ['---', '---', '---', '---', '---', '   ', '   ', '   ', '   ', '---'],
                ['---', '---', '---', '---', 'entrance', '   ', 'sister of the lost', '   ', '---', '---'],
                ['---', '---', '---', '---', '---', '---', '---', '---', '---', '---']],
        "data": {
            "random_encounter_chance": 8,
            "encounters": ['spider', 'dungeon1', 'skeleton' 'skeletons', 'skeletons2', 'skeletons3'],
            "move_time": 0,
            "visibility": 5,
            "music": "world1"
        }
    },

    "the quarry": {
        "map": [['---', '---', '---', '---', '---', '---', '---', '---', '---'],
                ['---', '   ', '   ', '   ', '---', '   ', '   ', '   ', '---'],
                ['---', '   ', '   ', '   ', '   ', '---', '---', '   ', '---'],
                ['---', '   ', '   ', '   ', '   ', '   ', '---', '   ', '---'],
                ['---', '---', '   ', '   ', '   ', '---', '   ', '   ', '---'],
                ['---', '   ', '   ', '   ', '---', '---', '   ', '   ', '---'],
                ['---', '---', '   ', '   ', '   ', '   ', '---', '---', '---'],
                ['---', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '---'],
                ['---', '---', '   ', '   ', '---', '   ', '   ', '---', '---'],
                ['---', '---', '---', '   ', '---', '---', '---', '---', '---'],
                ['---', '---', '---', '---', '---', '---', '---', '---', '---']],
        "data": {
            "random_encounter_chance": 0,
            "encounters": ['skeleton', 'skeletons', 'skeletons2', 'skeletons3'],
            "move_time": 0,
            "visibility": 3,
            "music": "world1"
        }
    },

    "the caves": {
        "map": [['---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---'],
                ['---', '   ', '   ', '   ', '---', '---', '---', '   ', '---', '   ', '---', '---'],
                ['---', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '---', '   ', '---'],
                ['---', '   ', '---', '   ', '---', '---', '   ', '   ', '   ', '   ', '   ', '---'],
                ['---', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '---'],
                ['---', '---', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '---', '---'],
                ['---', '   ', '---', '---', '   ', '---', '   ', '---', '   ', '   ', '   ', '---'],
                ['---', '---', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '---'],
                ['---', '   ', '---', '   ', '---', '   ', '   ', '   ', '---', '---', '   ', '---'],
                ['---', '   ', '---', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '---'],
                ['---', '   ', '---', '   ', '   ', '   ', '   ', '---', '   ', '   ', '   ', '---'],
                ['---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---']],
        "data": {
            "random_encounter_chance": 0,
            "encounters": [],
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
        "sewer entrance": {"description": "A run-down wooden door on the side of a hill and a sewer on the other side.", "enter": [1, 1, "sewer"]},
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
    "sewer": {
        "to ironwood": {"description": "This leads back to Ironwood.", "enter": [6, 2, "ironwood"]},
        "mysterious door": {"description": "This door doesn't seem to belong here...", "enter": [6, 2, "ironwood"]}
    },
    "city of thieves": {
        "entrance": {"description": "An unmanned gate.", "enter": [1, 5, "world"]}
    },
    "world": {
        "ironwood" : {"description": "The peaceful capital of Sveragard", "enter": [3, 1, 'ironwood']},
        "the old woods" : {"description": "An ancient curse echoes...", "enter": [2, 25, 'the old woods']},
        "mount megalos" : {"description": "The foot of an impossibly tall mountain.", "enter": [4, 8, 'mount megalos']},
        "city of thieves" : {"description": "A city built on a legacy of cutthroat thievery.", "enter": [3, 14, 'city of thieves']},
        "the wastes" : {"description": "A desolate, toxic swamp that doesn't take kindly to outsiders.", "enter": [4, 9, 'the wastes']},
        "the quarry" : {"description": "A mineshaft long sealed due to unstable dark energy.", "enter": [3, 9, 'the quarry']},
        "tower of doom" : {"description": "The heart of this world's disasters. Enter if you dare...", "enter": [1, 1, 'tower of doom']},
        "riverfell" : {"description": "The ruins of what was once a beautiful city.", "enter": [0, 0, 'riverfell']}
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
        "mountain gate": {"description": "The entrance to mount megalos.", "enter": [4, 4, "world"]},
        "to the peak": {"description": "An unfathomably tall staircase going to the peak of the mountain.", "enter": [3, 5, "mount megalos peak"]},
        "big shiny rock": {"description": "A rock. Big and shiny. Big shiny rock."},
        "hot springs": {"description": "Maybe if the world wasn't ending you'd have time to relax here."},
        "enormous fossil": {"description": "You shudder to imagine what kind of creature this once was."},
        "statue of megalos": {"description": "A statue depicting a long lost king."},
        "cave entrance": {"description": "A yawning chasm beckons you to enter."},
    },

    "mount megalos peak": {
        "corpse of king megalos": {"description": "The dead king beckons you to fight.", "fight": "king megalos"},
        "to the foot": {"description": "An unfathomably tall staircase going to the peak of the mountain.", "enter": [1, 1, "mount megalos"]},
    },

    "the wastes": {
        "entrance": {"description": "Exits the wastes. Probably the best choice.", "enter": [2, 9, "world"]},
        "sister of the lost": {"description": "A woman covered head to toe in black leather garments is humming.", "shop": "sister of the lost"},
        "graveyard": {"description": "Looks incredibly ancient. Somehow feels slightly peaceful."},
        "dilapidated hut": {"description": "Has been utterly claimed by the wastes. Vine tendrils are pulling it into the ground."},
        "the bog": {"description": "A gurgling pool of purple liquid. Something is in there...", "fight": 'hideous bogman'}
    },

    "tower of doom": {
        "entrance": {"description": "A massive ornate door.", "fight": "king megalos"},
        "magic elevator": {"description": "A small circular platform that can carry you to the upper level.", "enter": [1, 5, "dark lord chamber"]},
    },

    "dark lord chamber": {
        "the dark lord": {"description": "The end of this adventure.", "fight": "the dark lord"},
        "entrance": {"description": "Leads back to the lower level of the tower.", "enter": [8, 1, "tower of doom"]},
    }
}
