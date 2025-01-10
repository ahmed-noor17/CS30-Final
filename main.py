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
import map as _map
import inventory as _inventory
import character as _character
import attack as _attack
from tabulate import tabulate
playing_game = True
fighting = False

game_title = '''
 _____ _____ _____ _____ _____ _____ _____
| __  |   __|   __| __  |   __|   __|   __|
|    -|   __|  |  |    -|   __|__   |__   |
|__|__|_____|_____|__|__|_____|_____|_____|\n'''

story_file = 'opening.txt'

player = {
	'character': _character.Character("if you see this it is a bug!", 1, 0, 0, 100, 10, 95, ['slash', 'fireball']),
	'position': [1, 3, "tutorial"],  # [x, y, map]
	'inventory': _inventory.Inventory([None]),
    'enemies': {}
}

#name, level, xp, gold, max_hp, atk, acc, moves
enemies = {
	'goblin': ["goblin", 1, 20, 5, 100, 2, 80, ['slash']],
	'orc': ["orc", 1, 35, 8, 140, 3, 80, ['slash']],
    'spider': ["spider", 1, 30, 7, 90, 3, 85, ['bite']],
    'blemmyae': ["blemmyae", 1, 0, 0, 240, 10, 80, ['headbutt', 'bash']],
    'manticore': ["manticore", 1, 0, 0, 400, 5, 95, ['headbutt', 'fireball']]
}

combat_encounters = {
    'test_fight': ['goblin', 'goblin', 'orc'],
    'aoe_test': ['goblin', 'goblin', 'goblin', 'goblin', 'goblin', 'goblin'],
    'hard_fight': ['manticore', 'orc', 'orc', 'goblin']
}

attacks = {
	'slash': _attack.Attack(5, 100, 'slashed {target}!', 'single enemy'),
    'bite': _attack.Attack(5, 100, 'bit {target}!', 'single enemy'),
    'bash': _attack.Attack(7, 80, 'bashed {target}!', 'single enemy'),
	'fireball': _attack.Attack(10, 95, 'casted fireball!', 'single enemy'),
    'incinerate': _attack.Attack(5, 95, 'scorched {target}!', 'all enemies'),
    'headbutt': _attack.Attack(10, 90, 'bashed {target} with their head!', 'single enemy'),
    'heal': _attack.Attack(-5, 99999, 'healed {target}!', 'single ally')
}

consumables = {
    'health potion': 'heal',
    'inferno orb': 'incinerate'
}

save_files = {
	'file 1': 'SaveSlot1.txt',
    'file 2': 'SaveSlot2.txt',
    'file 3': 'SaveSlot3.txt'
}

text_speed = 0.01

data_to_save = {
    'text_speed': text_speed,
    'skip_introduction': None,
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


def update_map_display():
    ''' Creates and updates a separate map that displays your location
        and the surrounding areas that you can move to.
    '''
    global map_display
    map_display = [
        [get_room(-2, -2, True), get_room(-2, -1, True),    get_room(-2, 0, True), get_room(-2, +1, True), get_room(-2, +2, True)],
        [get_room(-1, -2, True), get_room(-1, -1, True),    get_room(-1, 0, True), get_room(-1, +1, True), get_room(-1, +2, True)],
        [get_room(+0, -2, True), get_room(+0, -1, True), f"*{get_room()}*\n(You)", get_room(+0, +1, True), get_room(+0, +2, True)],
        [get_room(+1, -2, True), get_room(+1, -1, True),    get_room(+1, 0, True), get_room(+1, +1, True), get_room(+1, +2, True)],
        [get_room(+2, -2, True), get_room(+2, -1, True),    get_room(+2, 0, True), get_room(+2, +1, True), get_room(+2, +2, True)]]
    return tabulate(map_display, tablefmt="rounded_grid", stralign='center', rowalign='center').title()


def moving():
    moving = True
    print("You begin moving.")
    while moving:
        try:
            if _map.rooms[player['position'][2]][get_room()]['connections']:
                menu['movement_menu']['enter'] = change_map
        except KeyError:
            try:
                menu['movement_menu'].pop('enter')
            except Exception:
                pass
        try:
            if _map.rooms[player['position'][2]][get_room()]['shop']:
                menu['movement_menu']['shop'] = shopping
        except KeyError:
            try:
                menu['movement_menu'].pop('shop')
            except Exception:
                pass
        print(update_map_display() + "\n")  # This is where the movement menu code starts
        for option in menu["movement_menu"]:
            print(" - " + option.capitalize())
        print(" - Stop")
        choice = input("\nChoice: ").lower()
        if choice == "stop":
            if "n" in input("Would you like to stop moving? (Y/N) ").lower():
                os.system('cls' if os.name == 'nt' else 'clear')
                print("You did not move.")
                print_location_description()
                pass
            else:
                moving = False
                os.system('cls' if os.name == 'nt' else 'clear')
                return
        elif choice == "quit":
            back = input("Would you like to quit to main menu? (Y/N) ").lower()
            os.system('cls' if os.name == 'nt' else 'clear')
            if "n" in back:
                break
            else:
                return
        elif choice in menu['movement_menu'] or choice in move_options.keys():
            os.system('cls' if os.name == 'nt' else 'clear')
            try:
                if choice in menu['movement_menu']:
                    menu['movement_menu'][choice]()
                elif choice in move_options.keys():
                    menu['movement_menu'][move_options[choice]]()
            except KeyError:
                print("That is not a direction")
                pass
            print_location_description()
        else:
            pass


def print_location_description():
    ''' Tells the player the decription of the room
        they are currently in.'''
    try:
        print(_map.rooms[player['position'][2]][get_room()]['description'])
    except KeyError:
        pass


def get_room(y_offset=0, x_offset=0, for_display=False):
    try:
        room_name = _map.game_map[player['position'][2]]['map'][int(player['position'][1]) + y_offset][int(player['position'][0]) + x_offset]  # map, y, x
    except IndexError:
        return '---'
    padding = ' ' * (len(room_name)//2)  # Doesn't work
    if for_display and room_name != '---':
        if len(room_name) <= 8:
            room_name = padding + room_name + padding
        room_name = room_name + "\n"
    return room_name


def random_encounter():
    roll = random.randint(1, 100)
    if roll <= _map.game_map[player['position'][2]]['data']['random_encounter_chance']:
        encounter = _map.game_map[player['position'][2]]['data']['encounters'][0]
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
    _print("You suddenly find yourself back at the beginning of the game wow you 'regressed' haha!")
    player['position'] = [1, 3, "tutorial"]
    player['character'].gold = 0
    player['character'].hp = player['character'].max_hp
    player['inventory'] = _inventory.Inventory([None])


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
        enemy_object = player['enemies'][enemy]
        _print(f"\n{enemy_object.name.title()} took a turn!")
        use_attack(attacks[enemy_object.moves[random.randint(0, len(enemy_object.moves) - 1)]], enemy_object, player['character'])
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
        vowels = ['a', 'e', 'i', 'o', 'u']
        if enemy[0] in vowels:
            n = 'n'
        else:
            n = ''
        print(f"You've encountered a{n} {enemy.title()}!")

    global fighting
    fighting = True
    while fighting:
        print(f"\nHP: {player['character'].hp}/{player['character'].max_hp}")
        display_menu('combat_menu')
        if len(list(player['enemies'].keys())) <= 0:
            print("\nYou won!")
            print(f"You earned {xp_prize} EXP and {gold_prize}g")
            player['character'].gold += gold_prize
            player['character'].xp += xp_prize
            level_up()
            input("Press any key to continue: ")
            os.system('cls' if os.name == 'nt' else 'clear')
            fighting = False
            break
        enemy_turn()
        if player['character'].hp <= 0:
            print("You lost!")
            fighting = False
            game_over()
            break
    player['enemies'].clear()


def attack_menu():
    print("Attacks:")
    num = 1
    for attack in player['character'].moves:
        print(f" {num}. {attack.capitalize()}")
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
                        print(f" {num}. {target_enemy.title()}")
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
    print(f"{player['character'].name.title()} is attempting to flee!")


def use_item():
    usable_items = []
    for item in player['inventory'].contents:
        if item in list(consumables.keys()):
            usable_items.append(item)
            print(f" - {item.title()}")
    if len(usable_items) <= 0:
        print("You do not have any usable items!")
        return display_menu('combat_menu')
    print("Usable items:")
    while True:
        use_item = input("Choose an item to use: ").lower()
        if use_item in usable_items:
            player['inventory'].contents.remove(use_item)
            choose_attack_target(consumables[use_item])
            break


def use_attack(attack, attacker, target):
    attack_accuracy = attack.acc * attacker.acc/100
    if random.randint(0, 100) <= attack_accuracy:
        attack_damage = attack.damage * attacker.atk
        target.hp = clamp(target.hp - attack_damage, 0, target.max_hp)
        _print(f"\n{attacker.name.title()} {attack.use_text.replace('{target}', target.name.title())}")
        _print(f"Dealt {attack_damage} damage!")
        _print(f"{target.name.title()} has {target.hp} health remaining!")
        if target.hp <= 0:
            print(f"Defeated {target.name.title()}!")
            if target.name != player['character'].name:
                player['enemies'].pop(target.name)
    else:
        print(f"{target.name.title()} evaded the attack!")


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


def _print(text: str, delay=0.025, newline=True):
    try:  # Function prints text with a typing effect. 
        delay = text_speed  # Has to be done this way...
    except NameError:
        pass
    punctuation = ['.', '!', '?']
    if delay != 0.0:
        for char in text:
            print(char, end='', flush=True)
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
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        with open(story_file, 'r') as f:
            file_list = f.readlines()
            for line in file_list:
                _print(line)
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
        if chosen_save_file in list(save_files.keys()):
            current_save_file = save_files[chosen_save_file]
            load_data()
            break
        elif chosen_save_file in '123':
            current_save_file = list(save_files.items())[int(chosen_save_file) - 1][1]
            load_data()
            break
    story()
    os.system('cls' if os.name == 'nt' else 'clear')
    while playing_game:
        display_menu('game_menu')


def view_character():
    print("Stats:")
    print(player['character'])
    #return display_menu('game_menu')


def view_inventory():
    print(player['inventory'].contents)
    #return display_menu('game_menu')


def fight_test():
    combat(combat_encounters['test_fight'])


def shopping():
    current_shop = _map.rooms[player['position'][2]][get_room()]['shop'].lower()
    print(f"{current_shop.title()}:\n")
    for option in shops[current_shop]:
            print(f" - {option.capitalize()}  ---  (${shops[current_shop][option]})")
    input()
    pass


def buy():
    pass


def sell():
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


shops = {"dan's thingamabobs": {"health potion": 4,
                                "steel sword": 56,
                                "inferno orb": 112}}


menu = {
    "main_menu": {
        "play": play,
        "quit": _quit
    },
    "game_menu": {
        "move": moving,
        "fight": fight_test,
        "view character": view_character,
        "inventory": view_inventory,
        "save": save_data
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
            print(game_title)
        if current_menu == 'movement_menu':  # Movement menu is handled elsewhere
            print(update_map_display())
        option_list = list(menu[current_menu].items())
        num: int = 1
        for option in menu[current_menu]:
            print(f" {num}. {option.capitalize()}")
            num += 1
        choice = input("\nChoice: ").lower()
        try:
            choice = int(choice)
        except ValueError:
            pass
        os.system('cls' if os.name == 'nt' else 'clear')
        if choice == "quit" and current_menu != "main_menu":
            back = input("Would you like to quit to main menu? (Y/N) ").lower()
            os.system('cls' if os.name == 'nt' else 'clear')
            if "n" in back:
                break
            else:
                current_menu = 'main_menu'
        elif choice in menu[current_menu]:
            os.system('cls' if os.name == 'nt' else 'clear')
            return menu[current_menu][choice]()
        else:
            try:
                if int(choice) <= num and int(choice) >= 1:  # Check if the number inputted is an option
                    os.system('cls' if os.name == 'nt' else 'clear')
                    return option_list[int(choice) - 1][1]()
            except ValueError:
                pass
            pass


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
