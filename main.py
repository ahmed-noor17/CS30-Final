###############################################################################
# Title: REGRESS
# Name: Ahmed Noor, Damian Knourek, Aiden Dielschneider
# Class: CS30
# Assignment: Final Project
# Version: Pre-Alpha v1.0
# Date: December 9th, 2024
###############################################################################
# Imports and Global Variables ------------------------------------------------
import os
import time
import random
import math
import DATA.map_data as _map
import OBJECTS.inventory as _inventory
import OBJECTS.character as _character
import OBJECTS.attack as _attack
from tabulate import tabulate
import DATA.item_data as _item
playing_game = True
fighting = False

game_title = '''
 _____  ______ _____ _____  ______  _____ _____  
|  __ \|  ____/ ____|  __ \|  ____|/ ____/ ____| 
| |__) | |__ | |  __| |__) | |__  | (___| (___   
|  _  /|  __|| | |_ |  _  /|  __|  \___ \ ___ \  
| | \ \| |___| |__| | | \ \| |____ ____) |___) | 
|_|  \_\______\_____|_|  \_\______|_____/_____/\n'''

player_turn_text = '''
 _____ __    _____ __ __ _____ _____    _____ _____ _____ _____ _ 
|  _  |  |  |  _  |  |  |   __| __  |  |_   _|  |  | __  |   | |_|
|   __|  |__|     |_   _|   __|    -|    | | |  |  |    -| | | |_ 
|__|  |_____|__|__| |_| |_____|__|__|    |_| |_____|__|__|_|___|_|\n'''

enemy_turn_text = '''
 _____ _____ _____ _____ __ __    _____ _____ _____ _____ _       
|   __|   | |   __|     |  |  |  |_   _|  |  | __  |   | |_|      
|   __| | | |   __| | | |_   _|    | | |  |  |    -| | | |_       
|_____|_|___|_____|_|_|_| |_|      |_| |_____|__|__|_|___|_|\n'''

game_over_text = '''
 _____ _____ _____ _____    _____ _____ _____ _____ 
|   __|  _  |     |   __|  |     |  |  |   __| __  |
|  |  |     | | | |   __|  |  |  |  |  |   __|    -|
|_____|__|__|_|_|_|_____|  |_____|\___/|_____|__|__|\n'''

credit_text = '''
 _____ _____ _____ ____  _____ _____ _____ _ 
|   __| __  |   __|    \|_   _|_   _|   __|_|
|  |__|    -|   __|  |  |_| |_  | | |__   |_ 
|_____|__|__|_____|____/|_____| |_| |_____|_|\n'''

story_intro_file = os.getcwd() + '/TEXT/STORY/opening.txt'
death_file = os.getcwd() + '/TEXT/STORY/death.txt'

player = {
	'character': _character.Character("if you see this it is a bug!", 1, 0, 0, 100, 10, 95, ['slash', 'fireball']),
	'position': [1, 3, "tutorial"],  # [x, y, map]
	'inventory': _inventory.Inventory([None]),
    'enemies': {},
    'equipment': []
}

#name, level, xp, gold, max_hp, atk, acc, moves
enemies = {
	'goblin': ["goblin", 1, 20, 5, 100, 2, 80, ['slash']],
    'punching bag': ["punching bag", 1, 0, 0, 10000, 0, 0, ['slash']],
	'orc': ["orc", 1, 35, 8, 140, 3, 80, ['slash', 'bash']],
    'skeleton warrior': ["skeleton warrior", 1, 45, 10, 160, 4, 75, ['slash', 'gash']],
    'skeleton archer': ["skeleton archer", 1, 50, 10, 120, 5, 85, ['slash', 'arrow', 'arrow']],
    'skeleton mage': ["skeleton mage", 1, 55, 12, 100, 5, 90, ['fireball', 'lightning bolt', 'freeze ray', 'magic missile']],
    'imp': ["imp", 1, 50, 10, 90, 5, 90, ['slash', 'fireball', 'magic missile']],
    'spider': ["spider", 1, 30, 7, 90, 3, 85, ['bite']],
    'blemmyae': ["blemmyae", 1, 50, 10, 240, 10, 80, ['headbutt', 'bash']],
    'manticore': ["manticore", 1, 100, 20, 400, 5, 95, ['headbutt', 'fireball']],
    'the dark lord': ["the dark lord", 1, 1000, 1000, 700, 15, 90, ['cursed fire', 'unholy diver', 'incinerate', 'lightning bolt', 'freeze ray', 'magic missile']]
}

combat_encounters = {
    'test_fight': ['punching bag'],
    'goblin': ['goblin'],
    'goblin patrol': ['goblin', 'goblin'],
    'elite patrol': ['goblin', 'orc'],
    'dungeon1': ['spider'],
    'dungeon2': ['spider', 'skeleton warrior'],
    'dungeon3': ['skeleton warrior', 'skeleton warrior'],
    'dungeon4': ['skeleton warrior', 'imp', 'spider'],
    'dungeon5': ['orc', 'imp'],
    'the final battle': ['the dark lord']
}

attacks = {
	'slash': _attack.Attack(5, 100, '{attacker} slashed {target}!', 'single enemy'),
    'bite': _attack.Attack(4, 100, '{attacker} bit {target}!', 'single enemy'),
    'bash': _attack.Attack(7, 80, '{attacker} bashed {target}!', 'single enemy'),
    'gash': _attack.Attack(9, 100, '{attacker} lacerated {target}!', 'single enemy', 'bleed', 1),
    'hemorrhage': _attack.Attack(8, 100, '{attacker} caused {target} to bleed profusely!', 'single enemies', 'bleed', 3),
    'arrow': _attack.Attack(8, 90, '{attacker} shot {target} with an arrow!', 'single enemy'),
    'headbutt': _attack.Attack(10, 90, '{attacker} bashed {target} with their head!', 'single enemy'),
	'fireball': _attack.Attack(10, 95, '{attacker} casted fireball!', 'single enemy'),
    'incinerate': _attack.Attack(7, 95, '{attacker} scorched {target}!', 'all enemies'),
    'cursed fire': _attack.Attack(12, 96, '{attacker} casted cursed fire!', 'single enemy'),
    'heal': _attack.Attack(-5, 99999, '{attacker} healed {target}!', 'single ally'),
    'super heal': _attack.Attack(-15, 99999, '{attacker} healed {target}!', 'single ally'),
    'lightning bolt': _attack.Attack(12, 99999, '{attacker} shocked {target}!', 'single enemy'),
    'thunderstorm': _attack.Attack(7, 99999, '{attacker} shocked {target}!', 'all enemies'),
    'unholy diver': _attack.Attack(30, 75, '{attacker} unleashed havoc on {target}!', 'all enemies'),
    'annihilation': _attack.Attack(900, 99999, '{attacker} annihilated {target}!', 'all enemies'),
    'freeze ray': _attack.Attack(8, 95, '{attacker} froze {target}!', 'single enemy', 'freeze', 1),
    'frost blast': _attack.Attack(5, 90, '{attacker} froze {target}!', 'all enemies', 'freeze', 1),
    'deep freeze': _attack.Attack(9, 95, '{attacker} froze {target}!', 'single enemy', 'freeze', 2),
    'magic missile': _attack.Attack(5, 95, '{attacker} launched a magic missile at {target}!', 'single enemy'),
    'poison cloud': _attack.Attack(2, 100, '{attacker} poisoned {target}!', 'all enemies', 'poison', 2),

    # Damage over time status effects
    # The player is currently unaffected by debuffs but maybe it's for the best because is it really fun
    # to get stunlocked by an enemy freeze blasting you over and over?
    'bleed': _attack.Attack(15, 99999, '{target} bled!', 'single enemy'),
    'poison': _attack.Attack(40, 99999, "Poison courses through {target}'s veins!", 'single enemy'),
    'freeze': _attack.Attack(5, 99999, "{target} is completely frozen!", 'single enemy')
}

save_files = {
	'file 1': os.getcwd() + '/SAVE_DATA/SaveSlot1.txt',
    'file 2': os.getcwd() + '/SAVE_DATA/SaveSlot2.txt',
    'file 3': os.getcwd() + '/SAVE_DATA/SaveSlot3.txt'
}

debuff_char = _character.Character("man behind the curtain", 1, 0, 0, 0, 1, 100, [])

text_speed = 0.01
map_cell_character_len = 20
hours_remaining = 72.0

data_to_save = {
    'text_speed': text_speed,
    'skip_introduction': False,
    'player_name': player['character'].name,
    'player_level': player['character'].level,
    'player_xp': player['character'].xp,
    'player_gold': player['character'].gold,
    'player_max_hp': player['character'].max_hp,
    'player_hp': player['character'].hp,
    'player_atk': player['character'].atk,
    'player_acc': player['character'].acc,
    'player_moves': player['character'].moves,
    'player_x_position': player['position'][0],
    'player_y_position': player['position'][1],
    'player_map': player['position'][2],
    'player_inventory': player['inventory'].contents
}

loaded_data = data_to_save.copy()

current_save_file = None

move_options = {"w": "up",
                "a": "left",
                "s": "down",
                "d": "right",
                "north": "up",
                "west": "left",
                "south": "down",
                "east": "right"}

# Movement --------------------------------------------------------------------


def up():
    print("You head north.")
    update_position("y", 1)


def down():
    print("You head south.")
    update_position("y", -1)


def left():
    print("You head west.")
    update_position("x", -1)


def right():
    print("You head east.")
    update_position("x", 1)


def change_map():
    print("Changing map...")
    player['position'] = list(_map.rooms[player['position'][2]][get_room()]['connections'])


def update_position(axis, value):
    ''' Moves the player. Will not allow movement if the desired
        location is off the map or a negative number.'''
    if axis == "x":
        try:
            try_position = get_room(x_offset=value)
            if player['position'][0] + value < 0 or try_position == '---':
                raise IndexError
            player['position'][0] += value
            random_encounter()
        except IndexError:
            print("You cannot go that way.")
    elif axis == "y":
        try:
            try_position = get_room(y_offset=-value)
            if player['position'][1] - value < 0 or try_position == '---':
                raise IndexError
            player['position'][1] -= value
            random_encounter()
        except IndexError:
            print("You cannot go that way.")


def update_map_display(width: int, height: int):
    ''' Creates and updates a separate map that displays your location
        and the surrounding areas that you can move to.
        IMPORTANT: both arguments MUST be uneven and positive.
    '''
    map_display = []
    for h in range(height):
        map_display.append([])
        for w in range(width):
            map_display[h].append(get_room(h-(height//2), w-(width//2), True))
    map_display[height//2][width//2] = f"{get_room()}\n(You)"
    return tabulate(map_display, tablefmt="rounded_grid", stralign='center', rowalign='center').title()


def moving():
    moving = True
    print("You begin moving.")
    while moving:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{math.ceil(hours_remaining)} hours left until destruction...")
        temp_opt_list = []
        try:
            if _map.rooms[player['position'][2]][get_room()]['connections']:
                menu['movement_menu']['enter'] = change_map
            temp_opt_list.append('enter')
        except KeyError:
            try:
                menu['movement_menu'].pop('enter')
            except Exception:
                pass
        try:
            if _map.rooms[player['position'][2]][get_room()]['shop']:
                menu['movement_menu']['shop'] = shopping
            temp_opt_list.append('shop')
        except KeyError:
            try:
                menu['movement_menu'].pop('shop')
            except Exception:
                pass
        try:
            print(_map.rooms[player['position'][2]][get_room()]['description'])
        except KeyError:
            pass
        print(update_map_display(_map.game_map[player['position'][2]]['data']['visibility'], _map.game_map[player['position'][2]]['data']['visibility']))  # This is where the movement menu code starts
        if temp_opt_list != []:
            print("\nOptions:\n")
        for option in temp_opt_list:
            print(f" - {option.title()}")
        choice = input("\nChoice: ").lower()
        if choice == "stop":
            moving = False
            os.system('cls' if os.name == 'nt' else 'clear')
            return
        elif choice == "quit":
            if "n" in input("Would you like to quit to main menu? (Y/N) ").lower():
                break
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                return "quit"
        elif choice in menu['movement_menu'] or choice in move_options.keys():
            os.system('cls' if os.name == 'nt' else 'clear')
            try:
                if choice in menu['movement_menu']:
                    menu['movement_menu'][choice]()
                    expend_time(_map.game_map[player['position'][2]]['data']['move_time'])
                elif choice in move_options.keys():
                    menu['movement_menu'][move_options[choice]]()
                    expend_time(_map.game_map[player['position'][2]]['data']['move_time'])
            except KeyError:
                print("That is not a direction.")
                continue


def expend_time(time_cost):
    global hours_remaining
    hours_remaining -= time_cost
    if hours_remaining <= 0:
        game_over()


def get_room(y_offset=0, x_offset=0, for_display=False):
    try:
        room_name = _map.game_map[player['position'][2]]['map'][int(player['position'][1]) + y_offset][int(player['position'][0]) + x_offset]  # map, y, x
    except IndexError:
        return "/////////////////////\n/////////////////////\n/////////////////////"
    padding = 'ㅤ' * (int(max(map_cell_character_len - len(room_name), 0)/4))  # works now
    if for_display:
        if room_name == "---":
            room_name = "/////////////////////\n/////////////////////\n/////////////////////"
        else:
            room_name = "ㅤ\n" + padding + room_name + padding + "\nㅤ"
    return room_name


def random_encounter():
    roll = random.randint(1, 100)
    if roll <= _map.game_map[player['position'][2]]['data']['random_encounter_chance']:
        map_encounters = _map.game_map[player['position'][2]]['data']['encounters']
        encounter = map_encounters[random.randint(0, len(map_encounters) - 1)]
        combat(combat_encounters[encounter])


# Save/Load -------------------------------------------------------------------


def save_data():
    ''' Writes data to save file.'''
    try:
        with open(current_save_file, 'w') as f:
            for data in list(data_to_save.keys()):
                edited_data = str(data_to_save[data]).replace("'", "").replace('[', '').replace(']', '')
                f.write(f"{data}::{edited_data}\n")
    except Exception:
        print("An error occurred while saving data.")


def load_data():
    try:
        with open(current_save_file, 'r') as f:
            file_list = f.readlines()
            for line in file_list:
                data = line.strip().split('::')
                if ", " in data[1]:
                    data[1] = data[1].split(", ")
                loaded_data[data[0]] = data[1]
        global player
        player['character'] = _character.Character(loaded_data['player_name'], int(loaded_data['player_level']), int(loaded_data['player_xp']), int(loaded_data['player_gold']), int(loaded_data['player_max_hp']), int(loaded_data['player_atk']), int(loaded_data['player_acc']), loaded_data['player_moves'])
        player['position'] = [int(loaded_data['player_x_position']), int(loaded_data['player_y_position']), loaded_data['player_map']]
        player['inventory'] = _inventory.Inventory(list(loaded_data['player_inventory']))
    except FileNotFoundError:
        print("File does not exist.")


# Combat ----------------------------------------------------------------------


def game_over():
    global fighting
    global hours_remaining
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    _print(game_over_text, delay=0.1, print_by_line=True)
    time.sleep(1.5)
    show_story_text(death_file)
    hours_remaining = 72
    player['position'] = [1, 3, "tutorial"]
    player['character'].gold = 0
    player['character'].hp = player['character'].max_hp
    player['inventory'] = _inventory.Inventory([])
    player['enemies'].clear()
    fighting = False


def level_up():
    required_xp = level_formula()
    if player['character'].xp >= required_xp:
        player['character'].level += 1
        player['character'].atk += 1
        player['character'].max_hp += 10
        player['character'].hp = player['character'].max_hp
        print(f"LEVEL UP! YOU ARE NOW LEVEL {player['character'].level}")
        required_xp = level_formula()
        return level_up()
    print(f"EXP to next level up: {required_xp - player['character'].xp}")


def level_formula():
    return (1/5) * player['character'].level**2 * 100


def enemy_turn():
    for enemy in list(player['enemies'].keys()):
        if not fighting:
            break
        enemy_object = player['enemies'][enemy]
        if enemy_object.hp > 0 and not 'freeze' in enemy_object.debuffs:
            _print(f"\n{enemy_object.name.title()} took a turn!")
            use_attack(attacks[enemy_object.moves[random.randint(0, len(enemy_object.moves) - 1)]], enemy_object, player['character'])
        for debuff in list(dict.fromkeys(enemy_object.debuffs)):
            if enemy_object.hp > 0 and not check_for_battle_victory():  # Enemies do not take DOT damage if they are already dead or if they killed the player
                enemy_object.debuffs.remove(debuff)
                use_attack(attacks[debuff], debuff_char, enemy_object)
        time.sleep(0.1)


def combat(encounter_enemies):
    gold_prize = 0
    xp_prize = 0
    for enemy in encounter_enemies:
        enemy_object = _character.Character(enemies[enemy][0], enemies[enemy][1], enemies[enemy][2], enemies[enemy][3], enemies[enemy][4], enemies[enemy][5], enemies[enemy][6], enemies[enemy][7])
        gold_prize += enemy_object.gold
        xp_prize += enemy_object.xp
        enemy_count = 1
        while enemy_object.name in list(player['enemies'].keys()):
            enemy_count += 1
            if enemy_count > 2:  # This names the enemies if there are multiple of the same type
                enemy_object.name = f"{enemy_object.name[:-2]} {str(enemy_count)}"
            else:
                enemy_object.name = f"{enemy_object.name} {str(enemy_count)}"
        player['enemies'][enemy_object.name] = enemy_object
        n = 'n' if enemy[0] in ['a', 'e', 'i', 'o', 'u'] else ''
        _print(f"You've encountered a{n} {enemy.title()}!")
    time.sleep(0.5)

    global fighting
    fighting = True
    while fighting:
        _print(player_turn_text, delay=0.04, print_by_line=True)
        for target_enemy in list(player['enemies'].keys()):
            print(f" > {target_enemy.title()}   ---   (HP: {player['enemies'][target_enemy].hp}/{player['enemies'][target_enemy].max_hp})")
        print(f"\nYour HP: {player['character'].hp}/{player['character'].max_hp}")
        display_menu('combat_menu')
        if check_for_battle_victory(xp_prize, gold_prize):  # This function returns true if the battle is over
            return
        _print(enemy_turn_text, delay=0.04, print_by_line=True)
        enemy_turn()
        if not fighting:  # If the player dies, the enemies disappear, so break before the game "detects" that we've "won"
            break
        if check_for_battle_victory(xp_prize, gold_prize):  # It checks here too for if the player was killed or the enemies died on their own turn
            return
    player['enemies'].clear()


def check_for_battle_victory(xp_prize=0, gold_prize=0):
    global fighting
    if player['character'].hp <= 0:
        print("You lost!")
        fighting = False
        game_over()
        return True
    if len(list(player['enemies'].keys())) <= 0:
        print("\nYou won!")
        print(f"You earned {xp_prize} EXP and {gold_prize}g")
        player['character'].gold += gold_prize
        player['character'].xp += xp_prize
        level_up()
        input("Press any key to continue: ")
        os.system('cls' if os.name == 'nt' else 'clear')
        fighting = False
        return True
    else:
        return False


def attack_menu():
    print("Attacks:")
    num = 1
    for attack in player['character'].moves:
        print(f" {num}. {attack.capitalize()}   ---   (DMG: {attacks[attack].damage * player['character'].atk} ACC: {attacks[attack].acc * player['character'].acc / 100}%)")
        num += 1
    while True:
        use_move = input("Choose a move: ").lower()
        if use_move in player['character'].moves and use_move in list(attacks.keys()):
            choose_attack_target(use_move)
            break
        else:
            try:
                if int(use_move) <= len(player['character'].moves) and int(use_move) >= 1:
                    choose_attack_target(player['character'].moves[int(use_move) - 1])
                    break
            except Exception:  # TODO: Figure out what exception this should be
                pass


def choose_attack_target(use_move):
    while True:
        if 'ally' in attacks[use_move].target_type:
            use_attack(attacks[use_move], player['character'], player['character'])
            break
        else:
            target_list = list(player['enemies'].keys())
        if 'single' in attacks[use_move].target_type:          
            while True:
                if len(list(player['enemies'].keys())) <= 1:
                    target = target_list[0].lower()  # If only one target on the field, it will be automatically targetted
                else:
                    num = 1
                    for target_enemy in target_list:
                        print(f" {num}. {target_enemy.title()}   ---   (HP: {player['enemies'][target_enemy].hp}/{player['enemies'][target_enemy].max_hp})")
                        num += 1
                    target = input("Choose a target: ").lower()
                if target in list(player['enemies'].keys()):
                    use_attack(attacks[use_move], player['character'], player['enemies'][target])
                    break
                else:
                    try:
                        if int(target) <= len(target_list) and int(target) >= 1:
                            use_attack(attacks[use_move], player['character'], player['enemies'][target_list[int(target) - 1]])
                            break
                    except Exception:  # TODO: Figure out what exception this should be
                        pass
            break
        elif 'all ' in attacks[use_move].target_type:
            for target_enemy in target_list:
                use_attack(attacks[use_move], player['character'], player['enemies'][target_enemy])
            break


def flee_battle():
    global fighting
    fighting = False
    _print(f"{player['character'].name.title()} is attempting to flee!")


def use_item():
    usable_items = []
    num = 1
    print("Usable items:\n")
    for item in player['inventory'].contents:
        if item in list(_item.item['consumable'].keys()):
            usable_items.append(item)
            print(f" {num}. {item.title()}")
            num += 1
    if len(usable_items) <= 0:
        print("You do not have any usable items!")
        return display_menu('combat_menu')
    while True:
        use_item = input("Choose an item to use: ").lower()
        if use_item not in usable_items:
            try:
                use_item = int(use_item)
                if 1 <= use_item <= len(usable_items):
                    use_item = usable_items[use_item - 1]
            except ValueError:
                pass
        if use_item in usable_items:
            player['inventory'].contents.remove(use_item)
            choose_attack_target(_item.item['consumable'][use_item]['cast'])
            break
        else:
            pass


def use_attack(attack, attacker, target):
    attack_accuracy = attack.acc * attacker.acc/100
    if random.randint(0, 100) <= attack_accuracy:
        defence_modifier = 1 - (target.defence / (target.defence + 50))
        attack_damage = int(attack.damage * attacker.atk * defence_modifier)
        target.hp = clamp(target.hp - attack_damage, 0, target.max_hp)
        _print(f"\n{attack.use_text.replace('{target}', target.name.title()).replace('{attacker}', attacker.name.title())}")
        _print(f"Dealt {attack_damage} damage!")
        _print(f"{target.name.title()} has {target.hp} health remaining!")
        if not attack.debuff == None:
            for i in range(attack.debuff_stack_amount):
                target.debuffs.append(attack.debuff)
            _print(f"{target.name.title()} is now suffering from {attack.debuff}!")
        if target.hp <= 0:
            print(f"Defeated {target.name.title()}!")
            if target.name != player['character'].name:
                player['enemies'].pop(target.name)
    else:
        print(f"\n{target.name.title()} evaded the attack!")


# Base Functions --------------------------------------------------------------


def setup():
    global text_speed
    os.system('cls' if os.name == 'nt' else 'clear')
    with open(current_save_file) as file:  # Reads the speed on file and sets it
        for line in file.readlines():
            if "text_speed" in line:
                line = line.strip().split('::')
                text_speed = float(line[1])
    _print("This is the game's current text speed.")
    _print("Would you like to change the text speed? (Y/N) ", newline=False)
    if "n" in input().lower():
        os.system('cls' if os.name == 'nt' else 'clear')
        return
    _print("You are changing the text speed.")
    while True:
        print()
        text_speeds = {
            "slow": 0.038,
            "mid": 0.025,
            "fast": 0.012,
            "instant": 0
        }
        choice = input(
            'Choose "Slow", "Mid", "Fast", "Instant" or "Quit": ').lower()
        if choice in list(text_speeds.keys()):
            text_speed = text_speeds[choice]
        elif choice in "quit":
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        else:
            pass
        _print("This is how fast the text will appear. Here is some extra text.")
    with open(current_save_file, "r") as file:
        temp_list = file.readlines()  # Temp list of all lines in file
        temp_list[0] = f"text_speed::{str(text_speed)}\n"
        with open(current_save_file, "w") as file:
            file.writelines(temp_list)  # Updates setting in file
    return None


def _print(text: str, delay=text_speed, newline=True, print_by_line=False):
    ''' Function prints text with a typing effect.
    '''
    punctuation = ['.', '!', '?']
    if delay != 0.0:
        if print_by_line:
            text = text.splitlines()
        for char in text:
            print(char + '\n' * print_by_line, end='', flush=True)
            time.sleep(delay)
            if char == ' ':
                time.sleep(delay)
            elif char == ',':
                time.sleep(delay * 2)
            elif char in punctuation:
                time.sleep(delay + delay * 3)
        if newline:
            print()
    else:
        print(text, flush=not newline)


def story():
    global text_speed
    os.system('cls' if os.name == 'nt' else 'clear')
    show_story_text(story_intro_file)
    while True:
        player['character'].name = input("Enter player name: ")
        confirm = input(f"{player['character'].name}... Is this correct? (Y/N) ").lower()
        if "y" in confirm:
            break
    data_to_save['skip_introduction'] = True


def show_story_text(file):
    try:
        with open(file, 'r') as f:
            print("Press ENTER to continue")
            file_list = f.readlines()
            for line in file_list:
                _print(line, delay=0.002)
                input()
    except FileNotFoundError:
        print("ERROR: Could not find the story text file!")


def play():
    global current_save_file
    while True:
        print("\nSave files:")
        num = 1
        for save in list(save_files.keys()):
            print(f" {num}. {save.title()}")
            num += 1
        chosen_save_file = input("Choose a save file: ").lower()
        try:
            if 1 <= int(chosen_save_file) < num:
                chosen_save_file = list(save_files.keys())[int(chosen_save_file) - 1]
        except ValueError:
            pass
        if chosen_save_file in list(save_files.keys()):
            current_save_file = save_files[chosen_save_file]
            load_data()
            break
    if not loaded_data['skip_introduction'] == 'True':
        story()
    os.system('cls' if os.name == 'nt' else 'clear')
    while playing_game:
        x = display_menu('game_menu')
        if x == 'quit':
            return


def view_character():
    print(f"Time remaining: {hours_remaining} hours\n")
    print("Stats:")
    print(player['character'])


def view_inventory():
    print("Inventory:")
    if player['inventory'].contents == []:
        print("There is nothing in your bag.\n")
        return
    for item in list(dict.fromkeys(player['inventory'].contents)):
        print(f" - {item.title()} (x{player['inventory'].contents.count(item)})")
        


def fight_test():
    combat(combat_encounters['dungeon5'])


def shopping():
    current_shop = _map.rooms[player['position'][2]][get_room()]['shop'].lower()
    print(f"Welcome to {current_shop.upper()}!\n")
    display_menu('shop_menu')
    '''while True:
        num = 1
        print(f"\n{current_shop.upper()}:\n")
        for option in menu['shop_menu']:
            print(f" {num}. {option.title()}")
            num += 1
        print(f" {num}. Quit")
        choice = input("\nChoice: ").lower()
        try:
            choice = int(choice)
            if 1 <= choice < num:
                choice = list(menu['shop_menu'].keys())[choice - 1]
            elif choice == num:
                choice = 'quit'
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                continue
        except ValueError:
            pass   
        if choice == 'quit':
            os.system('cls' if os.name == 'nt' else 'clear')
            return
        elif choice in menu['shop_menu']:
            os.system('cls' if os.name == 'nt' else 'clear')
            menu['shop_menu'][choice]()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')'''


def buy():
    current_shop = _map.rooms[player['position'][2]][get_room()]['shop'].lower()
    while True:
        print(f"Purchasable items:\n")
        num = 1
        for option in shops[current_shop]:
            print(f" {num}. {option.capitalize()}  ---  ({_item.item['consumable'][option]['value']}g)")
            num += 1
        print(f" {num}. Quit")
        print(f"\nYou have {player['character'].gold}g")
        item_choice = input("\nBuy: ").lower()
        try:
            item_choice = int(item_choice)
            if 1 <= item_choice < num:
                item_choice = shops[current_shop][item_choice - 1]
            elif item_choice == num:
                item_choice = 'quit'
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                continue
        except ValueError:
            pass
        if item_choice == 'quit':
            os.system('cls' if os.name == 'nt' else 'clear')
            return
        elif item_choice in shops[current_shop]:
            pass
        else:
            continue
        if _item.item["consumable"][item_choice]["value"] <= player['character'].gold:
            player['character'].gold -= _item.item["consumable"][item_choice]["value"]
            player['inventory'].contents.append(item_choice)
        else:
            _print("\nYou don't have enough gold!")
            input("Press ENTER to continue")
        os.system('cls' if os.name == 'nt' else 'clear')


def sell():
    while True:
        print("Your sellable items:\n")
        num = 1
        for option in player['inventory'].contents:
            print(f" {num}. {option.capitalize()}  ---  (50g)")  # TODO: set item value
            num += 1
        print(f" {num}. Quit")
        print(f"\nYou have {player['character'].gold}g")
        item_choice = input("\nSell: ").lower()
        try:
            item_choice = int(item_choice)
            if 1 <= item_choice < num:
                item_choice = player['inventory'].contents[item_choice - 1]
            elif item_choice == num:
                item_choice = 'quit'
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                continue
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        if item_choice == 'quit':
            os.system('cls' if os.name == 'nt' else 'clear')
            return
        elif item_choice in player['inventory'].contents:
            pass
        player['inventory'].contents.remove(item_choice)
        player['character'].gold += 50  # need item value
        _print(f"\nYou sold {item_choice}")
        input("Press ENTER to continue")
        os.system('cls' if os.name == 'nt' else 'clear')


def equipment():
    display_menu('equipment_menu')


def equip_item():
    equipable_items = []
    print("Equipable items:")
    for item in player['inventory'].contents:
        if item in list(_item.item['equipment'].keys()):
            equipable_items.append(item)
            print(f" - {item}")
    if len(equipable_items) > 0:
        print("You have equipable items!")
    else:
        print("You do not have any equipable items!")


def unequip_item():
    pass


def _quit():
    global playing_game
    print("Press ENTER to confirm exit.")
    if input("(Or any character before ENTER to continue)") == '':
        playing_game = False
        exit("\nSee you next time!\n")
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        return display_menu('main_menu')
    

def credits_menu():
    print(credit_text)
    print("Created as a final project for Ms. Lynn's CS 30 class 2024-2025.\n")
    print("Regress Development Team:\n - Aiden Dielschneider (Developer)\n - Ahmed Noor (Developer)\n - Damian Knourek (Credit pending)")


shops = {
    "dan's thingamabobs": [
        "health potion",
        "magic icicle",
        "inferno scroll",
        "bottled lightning",
        "birthday bomb"]
}


menu = {
    "main_menu": {
        "play": play,
        "credits": credits_menu,
        "quit": _quit
    },
    "game_menu": {
        "move": moving,
        "fight": fight_test,
        "status": view_character,
        "inventory": view_inventory,
        "equipment": equipment,
        "save": save_data
    },
    "equipment_menu": {
        "equip": equip_item,
        "unequip": unequip_item
    },
    "movement_menu": {"up": up, "down": down,
        "left": left, "right": right
    },
    "combat_menu": {
        "attack": attack_menu,
        "item": use_item,
        "run": flee_battle
    },
    "shop_menu": {
        "buy": buy,
        "sell": sell
    }
}


def display_menu(current_menu):
    while True:
        if current_menu == 'main_menu':
            _print(game_title, delay=0.08, print_by_line=True)
        elif current_menu == 'game_menu':
            print(f"{math.ceil(hours_remaining)} hours left until destruction...")
        print()
        option_list = list(menu[current_menu].keys())
        num = 1
        for option in menu[current_menu]:
            print(f" {num}. {option.capitalize()}")
            time.sleep(0.05)
            num += 1
        if current_menu != 'main_menu' and current_menu != 'combat_menu':
            print(f" {num}. Quit")
        choice = input("\nChoice: ").lower()
        try:
            choice = int(choice)
            if 1 <= choice < num:  # Check if the number inputted is an option
                os.system('cls' if os.name == 'nt' else 'clear')
                choice = option_list[choice - 1]
            elif choice == num and current_menu != 'main_menu':
                choice = 'quit'
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                continue
        except ValueError:
            pass
        if choice == "quit" and current_menu != "main_menu"  and current_menu != "combat_menu":
            print("\nWould you like to quit to main menu?")
            if "n" in input("Any unsaved progress will be lost! (Y/N)").lower():
                os.system('cls' if os.name == 'nt' else 'clear')
                break
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                current_menu = 'main_menu'
        elif choice in menu[current_menu]:
            os.system('cls' if os.name == 'nt' else 'clear')
            return menu[current_menu][choice]()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')


def clamp(value, min_value, max_value):
    return max(min_value, min(value, max_value))


def main():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clears console
    global playing_game
    while playing_game:
        display_menu('main_menu')


# Main ------------------------------------------------------------------------
if __name__ == '__main__':
    while playing_game:
        main()
