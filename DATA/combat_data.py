import OBJECTS.attack as _attack

#name, level, xp, gold, max_hp, atk, acc, moves, item drops, drop % chance
enemies = {
	'goblin': ["goblin", 1, 20, 5, 100, 2, 80, ['slash']],
    'punching bag': ["punching bag", 1, 0, 0, 10000, 0, 0, ['slash']],
	'orc': ["orc", 1, 35, 8, 140, 3, 80, ['slash', 'bash']],
    'skeleton warrior': ["skeleton warrior", 1, 45, 10, 160, 4, 75, ['slash', 'gash']],
    'skeleton archer': ["skeleton archer", 1, 50, 10, 120, 5, 85, ['slash', 'arrow', 'arrow']],
    'skeleton mage': ["skeleton mage", 1, 55, 12, 100, 5, 90, ['fireball', 'lightning bolt', 'freeze ray', 'magic missile']],
    'imp': ["imp", 1, 50, 10, 90, 3, 90, ['slash', 'fireball', 'magic missile'], 'inferno scroll', 100],
    'spider': ["spider", 1, 30, 7, 90, 3, 85, ['bite']],
    'blemmyae': ["blemmyae", 1, 50, 10, 240, 10, 80, ['headbutt', 'bash']],
    'manticore': ["manticore", 1, 100, 20, 400, 5, 95, ['headbutt', 'fireball']],
    'the dark lord': ["the dark lord", 1, 1000, 1000, 700, 15, 90, ['cursed fire', 'unholy diver', 'incinerate', 'lightning bolt', 'freeze ray', 'magic missile']],
    'foul tumor': ["foul tumor", 1, 300, 60, 300, 4, 85, ['bite'], 'ring of poison', 100]
}

combat_encounters = {
    'test_fight': ['punching bag'],
    'goblin': ['goblin'],
    'goblin patrol': ['goblin', 'goblin'],
    'elite patrol': ['goblin', 'orc'],
    'spider': ['spider'],
    'dungeon1': ['spider', 'skeleton warrior'],
    'dungeon2': ['skeleton warrior', 'skeleton warrior'],
    'dungeon3': ['skeleton warrior', 'imp', 'spider'],
    'dungeon4': ['orc', 'imp'],
    'the final battle': ['the dark lord'],
    'tumor of the forest': ['foul tumor']
}

attacks = {
	'slash': _attack.Attack(5, 100, '{attacker} slashed {target}!', 'single enemy', sound='sword_hit'),
    'bite': _attack.Attack(4, 100, '{attacker} bit {target}!', 'single enemy', sound='blood'),
    'bash': _attack.Attack(7, 80, '{attacker} bashed {target}!', 'single enemy', sound='hit'),
    'gash': _attack.Attack(9, 100, '{attacker} lacerated {target}!', 'single enemy', 'bleed', 1, sound='blood'),
    'hemorrhage': _attack.Attack(8, 100, '{attacker} caused {target} to bleed profusely!', 'single enemies', 'bleed', 3, sound='blood'),
    'arrow': _attack.Attack(8, 90, '{attacker} shot {target} with an arrow!', 'single enemy', sound='hit'),
    'headbutt': _attack.Attack(10, 90, '{attacker} bashed {target} with their head!', 'single enemy', sound='hit'),
	'fireball': _attack.Attack(10, 95, '{attacker} casted fireball!', 'single enemy', sound='fire'),
    'incinerate': _attack.Attack(7, 95, '{attacker} scorched {target}!', 'all enemies', sound='fire'),
    'cursed fire': _attack.Attack(12, 96, '{attacker} casted cursed fire!', 'single enemy', sound='curse'),
    'heal': _attack.Attack(-5, 99999, '{attacker} healed {target}!', 'single ally'),
    'super heal': _attack.Attack(-15, 99999, '{attacker} healed {target}!', 'single ally'),
    'lightning bolt': _attack.Attack(12, 99999, '{attacker} shocked {target}!', 'single enemy', sound='electric'),
    'thunderstorm': _attack.Attack(7, 99999, '{attacker} shocked {target}!', 'all enemies', sound='electric'),
    'unholy diver': _attack.Attack(30, 75, '{attacker} unleashed havoc on {target}!', 'all enemies', sound='curse'),
    'annihilation': _attack.Attack(900, 99999, '{attacker} annihilated {target}!', 'all enemies'),
    'freeze ray': _attack.Attack(8, 95, '{attacker} froze {target}!', 'single enemy', 'freeze', 1),
    'frost blast': _attack.Attack(5, 90, '{attacker} froze {target}!', 'all enemies', 'freeze', 1),
    'deep freeze': _attack.Attack(9, 95, '{attacker} froze {target}!', 'single enemy', 'freeze', 2),
    'magic missile': _attack.Attack(5, 95, '{attacker} launched a magic missile at {target}!', 'single enemy'),
    'poison cloud': _attack.Attack(2, 100, '{attacker} poisoned {target}!', 'all enemies', 'poison', 2, sound='gas'),

    # Damage over time status effects
    # The player is currently unaffected by debuffs but maybe it's for the best because is it really fun
    # to get stunlocked by an enemy freeze blasting you over and over?
    'bleed': _attack.Attack(15, 99999, '{target} bled!', 'single enemy'),
    'poison': _attack.Attack(40, 99999, "Poison courses through {target}'s veins!", 'single enemy'),
    'freeze': _attack.Attack(5, 99999, "{target} is completely frozen!", 'single enemy')
}
