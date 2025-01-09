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
    'blemmyae': ["blemmyae", 1, 0, 0, 240, 10, 80, ['headbutt', 'bash']],
    'manticore': ["manticore", 1, 0, 0, 400, 5, 95, ['headbutt', 'fireball']]

}

attacks = {
	'slash': _attack.Attack(5, 100, 'slashed {target}!', 'single enemy'),
    'bash': _attack.Attack(7, 80, 'bashed {target}!', 'single enemy'),
	'fireball': _attack.Attack(10, 95, 'casted fireball!', 'single enemy'),
    'incinerate': _attack.Attack(10, 95, 'scorched {target}!', 'all enemies'),
    'headbutt': _attack.Attack(10, 90, 'bashed {target} with their head!', 'single enemy'),
    'heal': _attack.Attack(-5, 99999, 'healed {target}!', 'single ally')
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
                "d": "right"}

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
    player['position'] = list(_map.rooms[player['position'][2]][current_room()]['connections'])


def update_position(axis, value):
    ''' Moves the player. Will not allow movement if the desired
        location is off the map or a negative number.'''
    if axis == "x":
        try:
            try_position = _map.game_map[player['position'][2]][player['position'][1]][player['position'][0] + value]
            if player['position'][0] + value < 0 or try_position == 'X':
                raise IndexError
            player['position'][0] += value
        except IndexError:
            print("You cannot go that way.")
    elif axis == "y":
        try:
            try_position = _map.game_map[player['position'][2]][player['position'][1] - value][player['position'][0]]
            if player['position'][1] - value < 0 or try_position == 'X':
                raise IndexError
            player['position'][1] -= value
        except IndexError:
            print("You cannot go that way.")


def update_map_display():
    ''' Creates and updates a separate map that displays your location
        and the surrounding areas that you can move to.
    '''
    global map_display
    map_display = [
        [current_room(-1, -1), current_room(-1, 0), current_room(-1, +1)],
        [current_room(0, -1), f"*{current_room()}*", current_room(0, +1)],
        [current_room(+1, -1), current_room(+1, 0), current_room(+1, +1)]]
    return tabulate(map_display, tablefmt="rounded_grid").title()


def moving():
    moving = True
    print("You begin moving.")
    while moving:
        try:
            if _map.rooms[player['position'][2]][current_room()]['connections']:
                menu['movement_menu']['enter'] = change_map
        except KeyError:
            try:
                menu['movement_menu'].pop('enter')
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
        print(_map.rooms[player['position'][2]][current_room()]['description'])
    except KeyError:
        pass


def current_room(y_offset=0, x_offset=0):
    return _map.game_map[player['position'][2]][int(player['position'][1]) + y_offset][int(player['position'][0]) + x_offset]  # map, y, x


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
        time.sleep(0.5)


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
        print(f"You encountered a {enemy.title()}!")

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
    for attack in player['character'].moves:
        print(f" - {attack.title()}")
    while True:
        use_move = input("Choose a move: ").lower()
        if use_move in player['character'].moves and use_move in list(attacks.keys()):
            target_list = list(player['enemies'].keys())
            if 'single' in attacks[use_move].target_type:          
                while True:
                    if len(list(player['enemies'].keys())) <= 1:
                        target = target_list[0].lower()  # If only one target on the field, it will be automatically targetted
                    else:
                        for target_enemy in target_list:
                            print(f" - {target_enemy.title()}")
                        target = input("Choose a target: ").lower()
                    if target in list(player['enemies'].keys()):
                        use_attack(attacks[use_move], player['character'], player['enemies'][target])
                        break
            elif 'all ' in attacks[use_move].target_type:
                for target_enemy in target_list:
                    use_attack(attacks[use_move], player['character'], player['enemies'][target_enemy])
                break
            break


def flee_battle():
    global fighting
    fighting = False
    print(f"{player['character'].name.title()} is attempting to flee!")


def use_item():
    print("You cannot use items yet!")
    pass


def use_attack(attack, attacker, target):
    attack_accuracy = attack.acc * attacker.acc/100
    if random.randint(0, 100) <= attack_accuracy:
        attack_damage = attack.damage * attacker.atk
        target.hp -= attack_damage
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
    while True:
        print("\nSave files:")
        for save in list(save_files.keys()):
            print(f" - {save.title()}")
        chosen_save_file = input("Choose a save file: ").lower()
        if chosen_save_file in list(save_files.keys()):
            global current_save_file
            current_save_file = save_files[chosen_save_file]
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
    combat(['orc', 'goblin' , 'goblin' , 'goblin' , 'goblin' , 'goblin' , 'goblin'])


def _quit():
    global playing_game
    print("Press ENTER to confirm exit.")
    if input("(Or any character before ENTER to continue)") == '':
        playing_game = False
        exit("\nSee you next time!\n")
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        return display_menu('main_menu')


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
          "left": left, "right": right},
    "combat_menu": {"attack": attack_menu, "item": use_item, "run": flee_battle}
}


def display_menu(current_menu):
    while True:
        if current_menu == 'main_menu':
            print(game_title)
        if current_menu == 'movement_menu':  # Movement menu is handled elsewhere
            print(update_map_display())
        #print("\nOptions:")  # Prints and takes input for menu options
        for option in menu[current_menu]:
            print(" - " + option.capitalize())
        choice = input("\nChoice: ").lower()
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
            pass


def main():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clears console
    global playing_game
    while playing_game:
        display_menu('main_menu')


# Main ------------------------------------------------------------------------
if __name__ == '__main__':
    while playing_game:
        main()
