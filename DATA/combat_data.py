import OBJECTS.attack as _attack

# name, level, xp, gold, max_hp, atk, acc, moves, item drops, drop % chance, is_boss
enemies = {
	'goblin': ["goblin", 1, 20, 5, 100, 2, 80, ['slash'], 'silver scraps', 10],
    'punching bag': ["punching bag", 1, 0, 0, 10000, 0, 0, ['slash']],
	'orc': ["orc", 1, 35, 8, 140, 3, 80, ['slash', 'bash']],
    'bandit': ["bandit", 1, 30, 16, 100, 4, 85, ['slash']],
    'skeleton warrior': ["skeleton warrior", 1, 45, 10, 160, 6, 80, ['slash'], 'iron sword', 5],
    'skeleton archer': ["skeleton archer", 1, 50, 10, 120, 6, 85, ['slash', 'arrow', 'arrow'], 'bow', 5],
    'skeleton mage': ["skeleton mage", 1, 55, 12, 110, 5, 90, ['fireball', 'lightning bolt', 'magic missile']],
    'spider': ["spider", 1, 30, 7, 90, 3, 85, ['bite']],
    'goatman': ["goatman", 1, 50, 7, 150, 3, 80, ['headbutt', 'bash']],
    'zombie': ["zombie", 1, 70, 10, 200, 5, 95, ['headbutt', 'bite']],

    # Bosses
    'the dark lord': ["the dark lord", 1, 3000, 1000, 750, 10, 85, ['cursed flame', 'unholy diver', 'incinerate', 'lightning bolt', 'magic missile'], 'birthday bomb', 100, True],
    'tumor of the forest': ["tumor of the forest", 1, 200, 60, 300, 5, 85, ['bite'], 'ring of poison', 100, True],
    'king megalos': ["king megalos", 1, 400, 80, 450, 5, 65, ['lightning bolt', 'bash', 'smash'], 'helm of megalos', 100, True],
    'king of thieves': ["king of thieves", 1, 400, 200, 400, 6, 90, ['arrow', 'rain of arrows', 'slash', 'smash'], 'magic bow', 100, True],
    'the minotaur': ["the minotaur", 1, 600, 250, 600, 6, 70, ['headbutt', 'smash'], 'mighty battleaxe', 100, True],
    'hideous bogman': ["hideous bogman", 1, 700, 300, 650, 7, 80, ['headbutt', 'smash'], 'pendant of the wastes', 100, True],
}

combat_encounters = {
    'test_fight': ['punching bag'],
    'goblin': ['goblin'],
    'goblin patrol': ['goblin', 'goblin'],
    'elite patrol': ['goblin', 'orc'],
    'goatman': ['goatman'],
    'spider': ['spider'],
    'spiders': ['spider', 'spider'],
    'bandit ambush': ['bandit', 'bandit'],
    'skeleton': ['skeleton warrior'],
    'wastes': ['zombie', 'zombie'],
    'wastes2': ['skeleton archer', 'zombie'],
    'wastes3': ['zombie', 'zombie', 'skeleton warrior'],
    'wastes4': ['zombie', 'skeleton mage'],
    'quarry': ['spider', 'skeleton warrior'],
    'quarry2': ['skeleton warrior', 'skeleton archer'],
    'quarry3': ['skeleton warrior', 'skeleton mage'],
    'quarry4': ['skeleton archer', 'skeleton warrior', 'skeleton mage'],

    # Bosses
    'the dark lord': ['the dark lord'],
    'tumor of the forest': ['tumor of the forest'],
    'king megalos': ['king megalos'],
    'king of thieves': ['king of thieves'],
    'the minotaur': ['the minotaur'],
    'hideous bogman': ['hideous bogman']
}

attacks = {
	'slash': _attack.Attack(5, 100, '{attacker} slashed {target}!', 'single enemy', sound='sword_hit'),
    'bite': _attack.Attack(4, 100, '{attacker} bit {target}!', 'single enemy', sound='blood'),
    'bash': _attack.Attack(7, 85, '{attacker} bashed {target}!', 'single enemy', sound='hit'),
    'smash': _attack.Attack(9, 80, '{attacker} smashed {target}!', 'single enemy', sound='hit'),
    'gash': _attack.Attack(6, 100, '{attacker} lacerated {target}!', 'single enemy', 'bleed', 1, sound='blood'),
    'hemorrhage': _attack.Attack(8, 100, '{attacker} caused {target} to bleed profusely!', 'single enemy', 'bleed', 3, sound='blood'),
    'arrow': _attack.Attack(8, 90, '{attacker} shot {target} with an arrow!', 'single enemy', sound='hit'),
    'rain of arrows': _attack.Attack(8, 100, '{attacker} shot {target} with an arrow!', 'all enemies', sound='hit'),
    'headbutt': _attack.Attack(10, 70, '{attacker} bashed {target} with their head!', 'single enemy', sound='hit'),
	'fireball': _attack.Attack(10, 95, '{attacker} casted fireball!', 'single enemy', sound='fire'),
    'incinerate': _attack.Attack(7, 95, '{attacker} scorched {target}!', 'all enemies', sound='fire'),
    'cursed flame': _attack.Attack(12, 96, '{attacker} casted cursed flame!', 'single enemy', sound='curse'),
    'heal': _attack.Attack(-5, 99999, '{attacker} healed {target}!', 'single ally', sound='heal'),
    'super heal': _attack.Attack(-15, 99999, '{attacker} healed {target}!', 'single ally'),
    'lightning bolt': _attack.Attack(12, 99999, '{attacker} shocked {target}!', 'single enemy', sound='electric'),
    'thunderstorm': _attack.Attack(7, 99999, '{attacker} shocked {target}!', 'all enemies', sound='electric'),
    'unholy diver': _attack.Attack(20, 75, '{attacker} unleashed havoc on {target}!', 'all enemies', sound='curse'),
    'annihilation': _attack.Attack(900, 99999, '{attacker} annihilated {target}!', 'all enemies', sound='magic'),
    'freeze ray': _attack.Attack(8, 95, '{attacker} froze {target}!', 'single enemy', 'freeze', 1, 'ice'),
    'frost blast': _attack.Attack(5, 90, '{attacker} froze {target}!', 'all enemies', 'freeze', 1, 'ice'),
    'deep freeze': _attack.Attack(9, 95, '{attacker} froze {target}!', 'single enemy', 'freeze', 2, 'ice'),
    'magic missile': _attack.Attack(5, 95, '{attacker} launched a magic missile at {target}!', 'single enemy', sound='magic'),
    'poison cloud': _attack.Attack(2, 100, '{attacker} poisoned {target}!', 'all enemies', 'poison', 2, sound='gas'),
    'venom haze': _attack.Attack(5, 100, '{attacker} poisoned {target}!', 'all enemies', 'poison', 3, sound='gas'),
    'bladestorm': _attack.Attack(9, 95, '{target} was caught in a storm of blades by {attacker}!', 'all enemies', 'bleed', 1, sound='sword_hit'),

    # Damage over time status effects
    'bleed': _attack.Attack(20, 99999, '{target} bled!', 'single enemy', sound='blood'),
    'poison': _attack.Attack(40, 99999, "Poison courses through {target}'s veins!", 'single enemy', sound='blood'),
    'freeze': _attack.Attack(5, 99999, "{target} is completely frozen!", 'single enemy', sound='ice')
}
