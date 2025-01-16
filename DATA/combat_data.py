import OBJECTS.attack as _attack
import os

#name, level, xp, gold, max_hp, atk, acc, moves, item drops, drop % chance
enemies = {
	'goblin': ["goblin", 1, 20, 5, 100, 2, 80, ['slash']],
    'punching bag': ["punching bag", 1, 0, 0, 10000, 0, 0, ['slash']],
	'orc': ["orc", 1, 35, 8, 140, 3, 80, ['slash', 'bash']],
    'bandit': ["bandit", 1, 30, 16, 100, 4, 85, ['slash']],
    'skeleton warrior': ["skeleton warrior", 1, 45, 10, 160, 5, 80, ['slash', 'gash']],
    'skeleton archer': ["skeleton archer", 1, 50, 10, 120, 6, 85, ['slash', 'arrow', 'arrow']],
    'skeleton mage': ["skeleton mage", 1, 55, 12, 100, 5, 90, ['fireball', 'lightning bolt', 'freeze ray', 'magic missile']],
    'imp': ["imp", 1, 50, 10, 90, 3, 90, ['slash', 'fireball', 'magic missile'], 'inferno scroll', 100],
    'spider': ["spider", 1, 30, 7, 90, 3, 85, ['bite']],
    'goatman': ["goatman", 1, 50, 10, 200, 5, 80, ['headbutt', 'bash']],
    'manticore': ["manticore", 1, 100, 20, 400, 5, 95, ['headbutt', 'fireball']],
    'the dark lord': ["the dark lord", 1, 1000, 1000, 700, 15, 90, ['cursed fire', 'unholy diver', 'incinerate', 'lightning bolt', 'freeze ray', 'magic missile']],
    'foul tumor': ["foul tumor", 1, 300, 60, 300, 5, 85, ['bite'], 'ring of poison', 100],
    'resurrected king megalos': ["resurrected king megalos", 1, 500, 75, 500, 6, 85, ['lightning bolt', 'bash', 'smash'], 'helm of megalos', 100]
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
    'skeleton': ['skeleton warrior'],
    'skeletons': ['skeleton warrior', 'skeleton archer'],
    'skeletons2': ['skeleton warrior', 'skeleton mage'],
    'skeletons3': ['skeleton archer', 'skeleton warrior', 'skeleton mage'],
    'the final battle': ['the dark lord'],
    'tumor of the forest': ['foul tumor'],
    'bandit ambush': ['bandit', 'bandit'],
    'king megalos': ['resurrected king megalos']
}

attacks = {
	'slash': _attack.Attack(5, 100, '{attacker} slashed {target}!', 'single enemy', sound='sword_hit'),
    'bite': _attack.Attack(4, 100, '{attacker} bit {target}!', 'single enemy', sound='blood'),
    'bash': _attack.Attack(7, 85, '{attacker} bashed {target}!', 'single enemy', sound='hit'),
    'smash': _attack.Attack(9, 80, '{attacker} smashed {target}!', 'single enemy', sound='hit'),
    'gash': _attack.Attack(6, 100, '{attacker} lacerated {target}!', 'single enemy', 'bleed', 1, sound='blood'),
    'hemorrhage': _attack.Attack(8, 100, '{attacker} caused {target} to bleed profusely!', 'single enemies', 'bleed', 3, sound='blood'),
    'arrow': _attack.Attack(8, 90, '{attacker} shot {target} with an arrow!', 'single enemy', sound='hit'),
    'rain of arrows': _attack.Attack(8, 90, '{attacker} shot {target} with an arrow!', 'all enemies', sound='hit'),
    'headbutt': _attack.Attack(10, 70, '{attacker} bashed {target} with their head!', 'single enemy', sound='hit'),
	'fireball': _attack.Attack(10, 95, '{attacker} casted fireball!', 'single enemy', sound='fire'),
    'incinerate': _attack.Attack(7, 95, '{attacker} scorched {target}!', 'all enemies', sound='fire'),
    'cursed flame': _attack.Attack(12, 96, '{attacker} casted cursed flame!', 'single enemy', sound='curse'),
    'heal': _attack.Attack(-5, 99999, '{attacker} healed {target}!', 'single ally', sound='heal'),
    'super heal': _attack.Attack(-15, 99999, '{attacker} healed {target}!', 'single ally'),
    'lightning bolt': _attack.Attack(12, 99999, '{attacker} shocked {target}!', 'single enemy', sound='electric'),
    'thunderstorm': _attack.Attack(7, 99999, '{attacker} shocked {target}!', 'all enemies', sound='electric'),
    'unholy diver': _attack.Attack(30, 75, '{attacker} unleashed havoc on {target}!', 'all enemies', sound='curse'),
    'annihilation': _attack.Attack(900, 99999, '{attacker} annihilated {target}!', 'all enemies', sound='magic'),
    'freeze ray': _attack.Attack(8, 95, '{attacker} froze {target}!', 'single enemy', 'freeze', 1, 'ice'),
    'frost blast': _attack.Attack(5, 90, '{attacker} froze {target}!', 'all enemies', 'freeze', 1, 'ice'),
    'deep freeze': _attack.Attack(9, 95, '{attacker} froze {target}!', 'single enemy', 'freeze', 2, 'ice'),
    'magic missile': _attack.Attack(5, 95, '{attacker} launched a magic missile at {target}!', 'single enemy', sound='magic'),
    'poison cloud': _attack.Attack(2, 100, '{attacker} poisoned {target}!', 'all enemies', 'poison', 2, sound='gas'),

    # Damage over time status effects
    # The player is currently unaffected by debuffs but maybe it's for the best because is it really fun
    # to get stunlocked by an enemy freeze blasting you over and over?
    'bleed': _attack.Attack(15, 99999, '{target} bled!', 'single enemy', sound='blood'),
    'poison': _attack.Attack(40, 99999, "Poison courses through {target}'s veins!", 'single enemy', sound='blood'),
    'freeze': _attack.Attack(5, 99999, "{target} is completely frozen!", 'single enemy', sound='ice')
}

combat_sfx = {
        'blood': [os.getcwd() + '/SOUND/blood-splat-6295.mp3'],
        'sword_hit': [os.getcwd() + '/SOUND/sword-sound-effect-1-234987.mp3',
                      os.getcwd() + '/SOUND/sword-sound-effect-2-234986.mp3'],
        'sword_miss': [os.getcwd() + '/SOUND/sword-swing-whoosh-sound-effect-1-241824.mp3',
                       os.getcwd() + '/SOUND/sword-swing-whoosh-sound-effect-2-241823.mp3'],
        'hit': [os.getcwd() + '/SOUND/punch-or-kick-sound-effect-1-239696.mp3',
                os.getcwd() + '/SOUND/punch-or-kick-sound-effect-2-239695.mp3'],
        'miss': [os.getcwd() + '/SOUND/woosh-230554.mp3'],
        'fire': [os.getcwd() + '/SOUND/fireball-whoosh-2-179126.mp3'],
        'electric': [os.getcwd() + '/SOUND/electric-impact-37128.mp3'],
        'gas': [os.getcwd() + '/SOUND/yt1s.com - Smoke Grenade Sound Effect Free Sound Effect Download.mp3'],
        'curse': [os.getcwd() + '/SOUND/631769__robinhood76__11095-ancestor-curse-spell.wav'],
        'ice': [os.getcwd() + '/SOUND/yt1s.com - Ice Crack Freeze Sound Effect.mp3'],
        'magic': [os.getcwd() + '/SOUND/deathmagic-94937.mp3'],
        'heal': [os.getcwd() + '/SOUND/621206__eminyildirim__holy-protection-skill-buff.mp3']
    }
