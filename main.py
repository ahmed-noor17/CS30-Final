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
import keyboard
from tabulate import tabulate
from pygame import mixer
import DATA.map_data as _map
import DATA.item_data as _item
import DATA.shop_data as _shop
import DATA.combat_data as _combat
import DATA.sound_data as _sound
import OBJECTS.inventory as _inventory
import OBJECTS.character as _character
import TEXT.title_text as _title
mixer.init()

playing_game = True
fighting = False
skip_introduction = "False"

story_intro_file = os.getcwd() + '/TEXT/STORY/opening.txt'
death_file = os.getcwd() + '/TEXT/STORY/death.txt'

player = {
    'character': _character.Character(
                name="bug",
                level=1,
                xp=0,
                gold=0,
                max_hp=100,
                atk=10,
                acc=100,
                moves=['slash']),
    'position': [1, 3, "tutorial"],  # [x, y, map]
    'inventory': _inventory.Inventory([]),
    'enemies': {},
    'equipment': {
        "head": "None",
        "torso": "None",
        "weapon": "None",
        "accessory": "None"},
    'defeated bosses': []
}


save_files = {
    'file 1': os.getcwd() + '/SAVE_DATA/SaveSlot1.txt',
    'file 2': os.getcwd() + '/SAVE_DATA/SaveSlot2.txt',
    'file 3': os.getcwd() + '/SAVE_DATA/SaveSlot3.txt'
}
data_to_save = {}
loaded_data = {}
current_save_file = None

debuff_char = _character.Character("debuff man", 1, 0, 0, 0, 1, 100, [])
text_speed = 0.01
map_cell_character_len = 25
max_hours = 168
hours_remaining = 168.0

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
    player['position'] = list(_map.rooms[player['position'][2]][get_room()]
                              ['enter'])
    music_check()


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
            pass
    elif axis == "y":
        try:
            try_position = get_room(y_offset=-value)
            if player['position'][1] - value < 0 or try_position == '---':
                raise IndexError
            player['position'][1] -= value
            random_encounter()
        except IndexError:
            pass


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
    return tabulate(map_display,
                    tablefmt="rounded_grid",
                    stralign='center',
                    rowalign='center').title()


def map_encounter():
    combat(_combat.combat_encounters[_map.rooms[player['position'][2]]
                                     [get_room()]['fight']])


def moving():
    ''' Displays movement options and lets the player move.
    '''
    moving = True
    print("You begin moving.")
    while moving:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{math.ceil(hours_remaining)} hours left until destruction...")
        temp_opt_list = room_attribute_list()
        try:
            print(_map.rooms[player['position'][2]][get_room()]['description'])
        except KeyError:
            pass
        print(update_map_display(
            _map.game_map[player['position'][2]]['data']['visibility'],
            _map.game_map[player['position'][2]]['data']['visibility']))
        print("Move with WASD, type 'stop' to stop.")
        if temp_opt_list != []:  # Movement menu code starts here
            print("\nOptions:\n")
        num = list_menu_options(temp_opt_list, 'movement_menu')
        choice = convert_num_menu(input("\nChoice: ").lower(), num,
                                  'movement_menu')
        if choice == "stop":
            moving = False
            os.system('cls' if os.name == 'nt' else 'clear')
            return
        elif choice == "quit":
            if "n" in input("Quit to main menu? (Y/N) ").lower():
                break
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                return "quit"
        elif choice in menu['movement_menu'] or choice in move_options.keys():
            os.system('cls' if os.name == 'nt' else 'clear')
            try:
                if choice in menu['movement_menu']:
                    menu['movement_menu'][choice]
                elif choice in move_options.keys():
                    menu['movement_menu'][move_options[choice]]
            except KeyError:
                continue
            if choice == 'shop' or choice == 'fight':
                return menu['movement_menu'][choice]()
            if choice in menu['movement_menu']:
                expend_time(_map.game_map[player['position'][2]]['data']
                            ['move_time'])
                menu['movement_menu'][choice]()
            elif choice in move_options.keys():
                expend_time(_map.game_map[player['position'][2]]['data']
                            ['move_time'])
                menu['movement_menu'][move_options[choice]]()


def room_attribute_list():
    ''' Figures out what special attributes the current map tile has
        and adds them to the options menu.
    '''
    room_attributes = {'enter': change_map,
                       'shop': shopping,
                       'fight': map_encounter}
    temp_opt_list = []
    for atr in list(room_attributes.keys()):
        try:
            _map.rooms[player['position'][2]][get_room()][atr]
        except KeyError:
            try:
                menu['movement_menu'].pop(atr)
            except KeyError:
                pass
        else:
            fight_room = _map.rooms[player['position'][2]][get_room()]['fight']
            if atr == 'fight' and fight_room not in player['defeated bosses']:
                menu['movement_menu'][atr] = room_attributes[atr]
                temp_opt_list.append(atr)
    return temp_opt_list


def expend_time(time_cost):
    global hours_remaining
    hours_remaining -= time_cost
    if hours_remaining <= 0:
        _print("Time has run out... The hour of darkness is upon us...")
        game_over()


def get_room(y_offset=0, x_offset=0, for_display=False):
    ''' Gets the name of the room the player is in. Offsets allow getting
        adjacent rooms and for_display formats it for use on the map.
    '''
    try:
        room_name = (_map.game_map[player['position'][2]]['map']
                     [int(player['position'][1]) + y_offset]
                     [int(player['position'][0]) + x_offset])
    except IndexError:
        return "////////////////\n" * 3
    padding = '­' * (int(max(map_cell_character_len - len(room_name), 0)/4))
    if for_display:
        if room_name == "---":
            room_name = "////////////////\n"*3
        else:
            room_name = "­\n" + padding + room_name + padding + "\n­"
    return room_name


def random_encounter():
    ''' Roll for random encounter based on the data of the current map
        in map_data.
    '''
    roll = random.randint(1, 100)
    if roll <= (_map.game_map[player['position'][2]]['data']
                ['random_encounter_chance']):
        map_encounters = (_map.game_map[player['position'][2]]['data']
                          ['encounters'])
        encounter = map_encounters[random.randint(0, len(map_encounters) - 1)]
        combat(_combat.combat_encounters[encounter])


# Save/Load -------------------------------------------------------------------


def save_data():
    ''' Writes data to save file.
    '''
    global data_to_save
    global skip_introduction
    data_to_save = {
        'skip_introduction': skip_introduction,
        'player_name': player['character'].name,
        'player_level': player['character'].level,
        'player_xp': player['character'].xp,
        'player_gold': player['character'].gold,
        'player_hp': player['character'].hp,
        'player_max_hp': player['character'].max_hp,
        'player_hp': player['character'].hp,
        'player_atk': player['character'].atk,
        'player_acc': player['character'].acc,
        'player_moves': player['character'].moves,
        'player_x_position': player['position'][0],
        'player_y_position': player['position'][1],
        'player_map': player['position'][2],
        'player_head': player['equipment']['head'],
        'player_torso': player['equipment']['torso'],
        'player_weapon': player['equipment']['weapon'],
        'player_accessory': player['equipment']['accessory']
    }
    if player['inventory'].contents is not None:
        data_to_save['player_inventory'] = player['inventory'].contents
    if player['defeated bosses'] is not None:
        data_to_save['defeated_bosses'] = player['defeated bosses']

    try:
        with open(current_save_file, 'w') as f:
            for data in list(data_to_save.keys()):
                edited_data = (str(data_to_save[data])
                               .replace("'", "")
                               .replace('[', '')
                               .replace(']', ''))
                f.write(f"{data}::{edited_data}\n")
    except Exception:
        print("An error occurred while saving data.")


def load_data():
    ''' Changes the player's stats to match what is in the save file.
    '''
    global skip_introduction
    try:
        with open(current_save_file, 'r') as f:
            file_list = f.readlines()
            for line in file_list:
                data = line.strip().split('::')
                if ", " in data[1]:
                    data[1] = data[1].split(", ")
                loaded_data[data[0]] = data[1]
        global player
        player['character'] = _character.Character(
            loaded_data['player_name'],
            int(loaded_data['player_level']),
            int(loaded_data['player_xp']),
            int(loaded_data['player_gold']),
            int(loaded_data['player_max_hp']),
            int(loaded_data['player_atk']),
            int(loaded_data['player_acc']),
            loaded_data['player_moves'])
        player['character'].hp = int(loaded_data['player_hp'])
        player['position'] = [
            int(loaded_data['player_x_position']),
            int(loaded_data['player_y_position']),
            loaded_data['player_map']]
        player['equipment']['head'] = loaded_data['player_head']
        player['equipment']['torso'] = loaded_data['player_torso']
        player['equipment']['weapon'] = loaded_data['player_weapon']
        player['equipment']['accessory'] = loaded_data['player_accessory']
        if isinstance(loaded_data['player_inventory'], str):
            player['inventory'] = _inventory.Inventory([])
            player['inventory'].contents.append(
                loaded_data['player_inventory'])
        else:
            player['inventory'] = _inventory.Inventory(
                loaded_data['player_inventory'])
        if isinstance(loaded_data['defeated_bosses'], str):
            player['inventory'].contents.append(
                loaded_data['defeated_bosses'])
        else:
            player['inventory'] = loaded_data['defeated_bosses']
        skip_introduction = loaded_data['skip_introduction']
    except FileNotFoundError:
        print("File does not exist.")


# Combat ----------------------------------------------------------------------


def game_over():
    ''' Does some story text then resets the player to the beginning.'''
    global fighting
    global max_hours
    global hours_remaining
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    _print(_title.game_over_text, delay=0.1, print_by_line=True)
    time.sleep(1.5)
    show_story_text(death_file)
    hours_remaining = max_hours
    player['position'] = [1, 3, "tutorial"]
    player['character'].gold = 0
    player['character'].hp = player['character'].max_hp
    player['inventory'] = _inventory.Inventory([])
    player['enemies'].clear()
    player['defeated bosses'].clear()
    fighting = False


def level_up():
    ''' Increases the player's stats.'''
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
    ''' Makes all enemies attack the player and take DoT damage if
        applicable.
    '''
    for enemy in list(player['enemies'].keys()):
        enemy_object = player['enemies'][enemy]
        enemy_attack = _combat.attacks[enemy_object.moves[random.randint(
                                       0, len(enemy_object.moves) - 1)]]
        if enemy_object.hp > 0 and 'freeze' not in enemy_object.debuffs:
            _print(f"\n{enemy_object.name.title()} took a turn!")
            use_attack(enemy_attack, enemy_object, player['character'])
        for debuff in list(dict.fromkeys(enemy_object.debuffs)):
            if enemy_object.hp > 0 and not player['character'].hp <= 0:
                enemy_object.debuffs.remove(debuff)  # No DOT damage if dead
                use_attack(_combat.attacks[debuff], debuff_char, enemy_object)
        time.sleep(0.1)


def combat(encounter_enemies):
    ''' Handles basically all of the combat.'''
    calculate_player_defence()
    gold_prize = 0
    xp_prize = 0
    item_prize = []
    keyboard.block_key('enter')
    for enemy in encounter_enemies:  # Aiden, explain.
        enemy_object = _character.Character(
            _combat.enemies[enemy][0],
            _combat.enemies[enemy][1],
            _combat.enemies[enemy][2],
            _combat.enemies[enemy][3],
            _combat.enemies[enemy][4],
            _combat.enemies[enemy][5],
            _combat.enemies[enemy][6],
            _combat.enemies[enemy][7])
        try:
            enemy_object.boss = _combat.enemies[enemy][10]
        except IndexError:
            pass  # Enemy is not a boss
        gold_prize += enemy_object.gold
        xp_prize += enemy_object.xp
        try:  # Line below makes random drop chance
            if random.randint(1, 100) <= _combat.enemies[enemy_object.name][9]:
                item_prize.append(_combat.enemies[enemy_object.name][8])
        except IndexError:  # Line above adds drop to prize pool
            pass
        enemy_count = 1
        while enemy_object.name in list(player['enemies'].keys()):
            enemy_count += 1
            if enemy_count > 2:  # Numbers enemies sharing the same name
                enemy_object.name = (
                    f"{enemy_object.name[:-2]}{str(enemy_count)}")
            else:
                enemy_object.name = f"{enemy_object.name} {str(enemy_count)}"
        player['enemies'][enemy_object.name] = enemy_object
        n = 'n' if enemy[0] in ['a', 'e', 'i', 'o', 'u'] else ''
        _print(f"You've encountered a{n} {enemy.title()}!")
    time.sleep(0.5)
    global fighting
    fighting = True
    play_music(["battle1", "battle2"][random.randint(0, 1)])
    while fighting:
        _print(_title.player_turn_text, delay=0.04, print_by_line=True)
        for target_enemy in list(player['enemies'].keys()):
            print(f" > {target_enemy.title()}   ---   "
                  f"(HP: {player['enemies'][target_enemy].hp}"
                  f"/{player['enemies'][target_enemy].max_hp})")
        print(f"\nYour HP: {player['character'].hp}"
              f"/{player['character'].max_hp}")
        if display_menu('combat_menu') == "cancel":
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        if check_for_battle_victory(xp_prize, gold_prize, item_prize):
            music_check()
            return  # Ends function if battle is over
        time.sleep(1)
        _print(_title.enemy_turn_text, delay=0.04, print_by_line=True)
        enemy_turn()
        if check_for_battle_victory(xp_prize, gold_prize, item_prize):
            music_check()
            return  # Also checks here if player was killed or all enemies died
        time.sleep(1)
    music_check()
    player['enemies'].clear()


def check_for_battle_victory(xp_prize=0, gold_prize=0, item_prize=[]):
    ''' Will check if the player has either won or lost. Returns False
        if the battle is still in progress.
    '''
    global fighting
    if player['character'].hp <= 0:
        print("You lost!")
        fighting = False
        game_over()
        return True
    elif len(list(player['enemies'].keys())) <= 0:
        print("\nYou won!")
        print(f"You earned {xp_prize} EXP and {gold_prize}g")
        for item in item_prize:
            print(f"You got {item.capitalize()}!")
            player['inventory'].contents.append(item)
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
    ''' Allows the player to pick an attack to use and displays info.'''
    equipment_moves = []
    for equipment in list(player['equipment'].items()):
        try:
            move = _item.item['equipment'][equipment[1]]['move']
        except KeyError:
            pass
        else:
            if (equipment[1] != "None" and move is not None):
                equipment_moves.append(move)
    player_moves = player['character'].moves + equipment_moves
    print("Attacks:")
    num = 1
    for attack in player_moves:
        curr_atk = _combat.attacks[attack]
        print(f" {num}. {attack.capitalize()}   ---   "
              f"(DMG: {curr_atk.damage * player['character'].atk},"
              f" ACC: {curr_atk.acc * player['character'].acc / 100}%,"
              f" TARGET: {curr_atk.target_type.title()})")
        num += 1
    print(f" {num}. Cancel")
    while True:
        use_move = convert_num_menu(input("Choose a move: ").lower(), num,
                                    list_of_options=player_moves)
        if use_move in player_moves:
            if choose_attack_target(use_move) == "cancel":
                return "cancel"
            break
        elif use_move == "cancel":
            return "cancel"


def choose_attack_target(use_move):
    ''' Allows the player to choose a target to use an attack on.'''
    if 'ally' in _combat.attacks[use_move].target_type:
        use_attack(_combat.attacks[use_move],
                   player['character'], player['character'])
        return
    else:
        target_list = list(player['enemies'].keys())
    if 'single' in _combat.attacks[use_move].target_type:
        while True:
            if len(target_list) <= 1:
                target = target_list[0].lower()  # If one target, target it
            else:
                num = 1
                for target_enemy in target_list:
                    print(f" {num}. {target_enemy.title()}   ---   "
                          f"(HP: {player['enemies'][target_enemy].hp}"
                          f"/{player['enemies'][target_enemy].max_hp})")
                    num += 1
                print(f" {num}. Cancel")
                target = (
                    convert_num_menu(input("Choose a target: ").lower(),
                                     num, list_of_options=target_list))
            if target in target_list:
                use_attack(_combat.attacks[use_move], player['character'],
                           player['enemies'][target])
                break
            elif target == "cancel":
                return "cancel"
    elif 'all ' in _combat.attacks[use_move].target_type:
        for target_enemy in target_list:
            use_attack(_combat.attacks[use_move], player['character'],
                       player['enemies'][target_enemy])


def calculate_player_defence():
    ''' Calculates player defence based on their equipment.'''
    player['character'].defence = 0
    if player['equipment']['head'] != "None":
        player['character'].defence += (
            _item.item['equipment'][player['equipment']['head']]['defence'])
    if player['equipment']['torso'] != "None":
        player['character'].defence += (
            _item.item['equipment'][player['equipment']['torso']]['defence'])


def flee_battle():
    ''' Will end the battle after the next loop.'''
    global fighting
    fighting = False
    _print(f"{player['character'].name.title()} is attempting to flee!")


def use_item():
    ''' Allows the player to pick an item to use.'''
    usable_items = []
    num = 1
    print("Usable items:\n")
    for item in player['inventory'].contents:
        if item in list(_item.item['consumable'].keys()):
            usable_items.append(item)
    unique_usable_items = list(set(usable_items))
    for item in unique_usable_items:
        print(f" {num}. {item.title()} (x{usable_items.count(item)})")
        num += 1
    print(f" {num}. Cancel")
    if len(usable_items) <= 0:
        print("You do not have any usable items!")
        return display_menu('combat_menu')
    while True:
        item_choice = (
            convert_num_menu(input("Choose an item to use: ").lower(), num,
                             list_of_options=unique_usable_items))
        if item_choice in usable_items:
            player['inventory'].contents.remove(item_choice)
            choose_attack_target(_item.item['consumable'][item_choice]['cast'])
            break
        elif item_choice == "cancel":
            return "cancel"
        elif item_choice == "retry":
            continue


def use_attack(attack, attacker, target):
    ''' Damages a target, inflicts debuffs, and checks for kills.'''
    attack_accuracy = attack.acc * attacker.acc/100
    if random.randint(0, 100) <= attack_accuracy:
        defence_modifier = 1 - (target.defence / (target.defence + 50))
        attack_damage = int(attack.damage * attacker.atk * defence_modifier)
        target.hp = clamp(target.hp - attack_damage, 0, target.max_hp)
        attack_text = (attack.use_text.replace('{target}', target.name.title())
                       .replace('{attacker}', attacker.name.title()))
        _print(f"\n{attack_text}")
        play_sound(attack.sound, 0.8)
        _print(f"Dealt {attack_damage} damage!")
        _print(f"{target.name.title()} has {target.hp} health remaining!")
        if attack.debuff is not None:
            for i in range(attack.debuff_stack_amount):
                target.debuffs.append(attack.debuff)
            _print(f"{target.name.title()} is now suffering from "
                   f"{attack.debuff}!")
        if target.hp <= 0:
            print(f"Defeated {target.name.title()}!")
            if target.name != player['character'].name:
                player['enemies'].pop(target.name)
                if target.boss:  # If we killed a boss, remember this.
                    player['defeated bosses'].append(target.name)
    else:
        play_sound('miss')
        print(f"\n{target.name.title()} evaded the attack!")


# Base Functions --------------------------------------------------------------
def music_check():
    if _map.game_map[player['position'][2]]['data']['music'] != 'None':
        play_music(_map.game_map[player['position'][2]]['data']['music'])
    else:
        mixer.music.stop()


def play_sound(sound: str, volume=1.0, fade_out_ms=0):
    sound = (_sound.combat_sfx[sound]
             [random.randint(0, len(_sound.combat_sfx[sound])-1)])
    sound_effect = mixer.Sound(sound)
    sound_effect.set_volume(volume)
    sound_effect.play(fade_ms=fade_out_ms)
    return


def play_music(piece: str, volume=0.5):
    if piece in ['world1', 'world2']:
        mixer.music.set_volume(0.2)
    else:
        mixer.music.set_volume(volume)
    piece = _sound.bgm[piece]
    mixer.music.load(piece)
    mixer.music.play(2, 0, 0)
    pass


def _print(text: str, delay=text_speed, newline=True, print_by_line=False):
    ''' Function prints text with a typing effect.'''
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
    ''' This is the opening to the game.'''
    global text_speed
    global skip_introduction
    os.system('cls' if os.name == 'nt' else 'clear')
    show_story_text(story_intro_file)
    while True:
        _print("Enter player name: ", newline=False)
        player['character'].name = input()
        _print(f"{player['character'].name}... Is this correct? (Y/N) ",
               newline=False)
        confirm = input().lower()
        if "y" in confirm:
            break
    skip_introduction = "True"


def show_story_text(file):
    ''' Reads text from a specified .txt file.'''
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
    ''' Lets the player pick a save file and begin playing.'''
    global current_save_file
    global skip_introduction
    while True:
        print("\nSave files:")
        num = list_menu_options(list(save_files.keys()), 'file_select_menu')
        chosen_save_file = input("Choose a save file: ").lower()
        try:
            if 1 <= int(chosen_save_file) < num:
                chosen_save_file = (list(save_files.keys())
                                    [int(chosen_save_file) - 1])
        except ValueError:
            pass
        if chosen_save_file in list(save_files.keys()):
            current_save_file = save_files[chosen_save_file]
            load_data()
            break
    if skip_introduction != "True":
        story()
    os.system('cls' if os.name == 'nt' else 'clear')
    while playing_game:
        x = display_menu('game_menu')
        if x == 'quit':
            return


def view_character():
    ''' Prints character stats.'''
    calculate_player_defence()
    print(f"Time remaining: {hours_remaining} hours\n")
    print("Stats:")
    print(player['character'])


def view_inventory():
    ''' Displays player inventory.'''
    print("Inventory:")
    if player['inventory'].contents == []:
        print("There is nothing in your bag.\n")
        return
    for item in list(dict.fromkeys(player['inventory'].contents)):
        print(f" - {item.title()} "
              f"(x{player['inventory'].contents.count(item)})")


def fight_test():
    combat(_combat.combat_encounters['dungeon4'])


def shopping():
    display_menu('shop_menu')


def buy():
    ''' Allows the player to choose an item to buy from the shop.'''
    current_shop = (_map.rooms[player['position'][2]][get_room()]
                    ['shop'].lower())
    while True:
        print(f"Purchasable items:\n")
        num = 1
        for option in _shop.shops[current_shop]['wares']:
            print(f" {num}. {option.title()}  ---  "
                  f"({_item.item[sellable(option)][option]['value']}g)")
            num += 1
        print(f" {num}. Quit")
        print(f"\nYou have {player['character'].gold}g")
        item_choice = input("\nBuy: ").lower()
        try:
            item_choice = int(item_choice)
            if 1 <= item_choice < num:
                item_choice = (_shop.shops[current_shop]['wares']
                               [item_choice - 1])
            elif item_choice == num:
                item_choice = 'quit'
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                continue
        except ValueError:
            pass
        if item_choice == 'quit':
            os.system('cls' if os.name == 'nt' else 'clear')
            return display_menu('shop_menu')
        elif item_choice in _shop.shops[current_shop]['wares']:
            pass
        else:
            continue
        item_price = _item.item[sellable(item_choice)][item_choice]["value"]
        item_desc = (_item.item[sellable(item_choice)][item_choice]
                     ['description'])
        _print(f"\nITEM: {item_choice.title()}\nPRICE: {item_price}"
               f"\n{item_desc}\n")
        if 'n' in input("Would you like to buy this item? (Y/N)").lower():
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        if item_price <= player['character'].gold:
            player['character'].gold -= item_price
            player['inventory'].contents.append(item_choice)
        else:
            _print("\nYou don't have enough gold!")
            input("Press ENTER to continue")
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        _print(f"\nYou bought {item_choice.title()}.")
        input("Press ENTER to continue")
        os.system('cls' if os.name == 'nt' else 'clear')


def sell():
    ''' Allows the player to sell one of their items (70% value)'''
    while True:
        print("Your sellable items:\n")
        num = 1
        for option in player['inventory'].contents:
            item_price = (_item.item[sellable(option)][option]
                          ['value'] * 7 // 10)
            print(f" {num}. {option.title()}  ---  ({item_price}g)")
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
            return display_menu('shop_menu')
        elif item_choice in player['inventory'].contents:
            pass
        item_price = (_item.item[sellable(item_choice)][item_choice]
                      ['value'] * 7 // 10)
        confirmation = (input(f"Would you like to sell "
                              f"{item_choice.title()}? (Y/N)").lower())
        if 'n' in confirmation:
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        player['inventory'].contents.remove(item_choice)
        player['character'].gold += item_price
        _print(f"\nYou sold {item_choice.title()}.")
        input("Press ENTER to continue")
        os.system('cls' if os.name == 'nt' else 'clear')


def shop_dialogue():
    ''' Gets a dialogue from the current shop and prints it.'''
    current_shop = (_map.rooms[player['position'][2]][get_room()]
                    ['shop'].lower())
    dialogue = (
        _shop.shops[current_shop]["dialogue"]
        [random.randint(0, len(_shop.shops[current_shop]["dialogue"]) - 1)])
    _print(f'"{dialogue}"')
    return shopping()


def sellable(option):
    ''' Returns the category of item that an item is.'''
    sellable_categories = list(dict.fromkeys(_item.item))[1:]
    for category in sellable_categories:
        try:
            _item.item[category][option]
        except KeyError:
            pass
        else:
            return category


def equipment():
    ''' Shows player's current equipment and opens equip menu.'''
    print(player_equipment())
    display_menu('equipment_menu')


def player_equipment():
    return (f"Current equipment:\nHEAD: {player['equipment']['head'].title()}"
            f"\nTORSO: {player['equipment']['torso'].title()}"
            f"\nWEAPON: {player['equipment']['weapon'].title()}"
            f"\nACCESSORY: {player['equipment']['accessory'].title()}")


def equip_item():
    ''' Allows the player to choose an item to equip.'''
    equipable_items = []
    for item in player['inventory'].contents:
        if item in list(_item.item['equipment'].keys()):
            equipable_items.append(item)
    if len(equipable_items) <= 0:
        print("You have no equipable items!")
        return
    print("Equipable items:")
    num = 1
    for item in equipable_items:
        print(f" {num}. {item.capitalize()}   ---   "
              f"(DEF: {_item.item['equipment'][item]['defence']} "
              f"MOVE: {_item.item['equipment'][item]['move']})")
        num += 1
    while True:
        item_choice = input("Choose an item to equip: ").lower()
        item_to_equip = convert_num_menu(item_choice, num,
                                         list_of_options=equipable_items)
        if item_to_equip in equipable_items:
            item_slot = _item.item['equipment'][item_to_equip]['slot']
            item_in_slot = (player['equipment'][item_slot])
            if item_in_slot == "None":
                player['inventory'].contents.remove(item_to_equip)
                player['equipment'][item_slot] = item_to_equip
            else:
                # Player already has something equipped in this slot
                confirm = input(f"You already have {item_in_slot} equipped! "
                                f"Replace it? (Y/N) ").lower()
                if "y" in confirm:
                    player['inventory'].contents.append(item_in_slot)
                    player['inventory'].contents.remove(item_to_equip)
                    player['equipment'][item_slot] = item_to_equip
                else:
                    pass
        confirm = input("\nContinue equipping? (Y/N) ").lower()
        if 'y' in confirm:
            return equip_item()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            break


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
    print(_title.credit_text)
    print("Created as a final project for Ms. Lynn's CS 30 class 2024-2025.")
    print("""
Regress Development Team:
 - Aiden Dielschneider (Developer)
 - Ahmed Noor (Developer)
 - Damian Knourek (Credit pending)\n""")


menu = {
    "main_menu": {
        "play": play,
        "credits": credits_menu,
        "quit": _quit
    },
    "game_menu": {
        "move": moving,
        "status": view_character,
        "inventory": view_inventory,
        "equipment": equipment,
        "save": save_data
    },
    "equipment_menu": {
        "equip": equip_item,
    },
    "movement_menu": {
        "up": up,
        "down": down,
        "left": left,
        "right": right},
    "combat_menu": {
        "attack": attack_menu,
        "item": use_item,
        "run": flee_battle
    },
    "shop_menu": {
        "buy": buy,
        "sell": sell,
        "talk": shop_dialogue
    }
}


def display_menu(current_menu):
    ''' Displays the menu's options and lets the player pick one. Then,
        it executes the corresponding function.'''
    while True:
        keyboard.block_key('enter')
        if current_menu == 'main_menu':
            mixer.music.stop()
            _print(_title.game_title, delay=0.08, print_by_line=True)
        elif current_menu == 'game_menu':
            print(f"{math.ceil(hours_remaining)} hours left "
                  f"until destruction...")
        elif current_menu == 'shop_menu':
            current_shop = (_map.rooms[player['position'][2]][get_room()]
                            ['shop'].lower())
            print(f"Welcome to {current_shop.title()}.")
            print(_shop.shops[current_shop]['intro'])
        print()
        num = list_menu_options(menu[current_menu], current_menu)
        keyboard.unhook_all()
        choice = convert_num_menu(input("\nChoice: ").lower(), num,
                                  current_menu)
        if choice == 'retry':
            continue
        if (choice == "quit" and
                current_menu not in ['main_menu', 'combat_menu']):
            if current_menu == "game_menu":
                print("\nWould you like to quit to main menu?")
                print("Any unsaved progress will be lost!", end='')
                if "y" in input(" (Y/N) ").lower():
                    os.system('cls' if os.name == 'nt' else 'clear')
                    current_menu = 'main_menu'
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                return
        elif choice == "cancel":
            return "cancel"
        elif choice in menu[current_menu]:
            os.system('cls' if os.name == 'nt' else 'clear')
            return menu[current_menu][choice]()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')


def convert_num_menu(choice, num, current_menu='', list_of_options=[]):
    ''' Converts a number input to a regular text input in the menus.'''
    if current_menu != '' and list_of_options != []:
        raise Exception("The function convert_num_menu "
                        + "needs the 3rd or 4th argument! Not both!")
    elif current_menu != '':
        option_list = list(menu[current_menu].keys())
    elif list_of_options != []:
        option_list = list_of_options
    else:
        raise Exception("The function convert_num_menu "
                        + "needs the 3rd or 4th argument! Not neither!")
    try:
        choice = int(choice)
    except ValueError:
        return choice
    else:
        if 1 <= choice < num:  # Check if the number inputted is an option
            choice = (option_list
                      [choice - 1 + (4 if current_menu == 'movement_menu'
                                     else 0)])
        elif (choice == num and current_menu != 'movement_menu' and
                list_of_options == []):
            choice = 'quit'
        elif choice == num and list_of_options != []:
            choice = 'cancel'
        else:
            return 'retry'
    return choice


def list_menu_options(menu_options: list, current_menu: str = ''):
    ''' Lists menu options.'''
    num = 1
    for option in menu_options:
        print(f" {num}. {option.capitalize()}")
        time.sleep(0.05)
        num += 1
    if current_menu == '':
        exit("current_menu not found!")
    if current_menu not in ['main_menu', 'combat_menu', 'movement_menu',
                            'file_select_menu']:
        print(f" {num}. Quit")
    return num


def clamp(value, min_value, max_value):
    ''' Clamps a value to a range of [min_value, max_value].'''
    return max(min_value, min(value, max_value))


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    global playing_game
    while playing_game:
        display_menu('main_menu')


# Main ------------------------------------------------------------------------
if __name__ == '__main__':
    while playing_game:
        main()
