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
import combat as _combat
import attack as _attack
from tabulate import tabulate
save_file1 = 'SaveSlot1.txt'
playing_game = True
game_title = '''
 _____ _____ _____ _____ _____ _____ _____
| __  |   __|   __| __  |   __|   __|   __|
|    -|   __|  |  |    -|   __|__   |__   |
|__|__|_____|_____|__|__|_____|_____|_____|\n'''

player = {
	'character': _character.Character("john hulk", 100, 5, 95, ['slash', 'fireball']),
	'position': [1, 4, "house"],  # [x, y, map]
	'inventory': _inventory.Inventory([None]),
    'enemies': {}
}

enemies = {
	'goblin': ["goblin", 50, 5, 80, ['heal']],
	'orc': ["orc", 100, 8, 80, ['slash']],
    'blemmyae': ["blemmyae", 150, 10, 80, ['headbutt', 'bash']],
    'manticore': ["manticore", 200, 5, 95, ['headbutt', 'fireball']]

}

attacks = {
	'slash': _attack.Attack(5, 100, 'slashed {target}!'),
    'bash': _attack.Attack(7, 80, 'bashed {target}!'),
	'fireball': _attack.Attack(10, 95, 'casted fireball!'),
    'headbutt': _attack.Attack(10, 90, 'bashed {target} with their head!'),
    'heal': _attack.Attack(-5, 99999, "healed {target}!")
}

# Functions -------------------------------------------------------------------
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
    return tabulate(map_display, tablefmt="grid").title()


move_options = {"w": "up",
                "a": "left",
                "s": "down",
                "d": "right"}


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
        for option in menu["movement_menu"]:  # You can move this to a separate function if you want, Aiden
            print(" - " + option.capitalize())
        choice = input("\nChoice: ").lower()
        print("\n")
        if choice in move_options.keys():
            menu['movement_menu'][move_options[choice]]()
        elif choice == "stop":
            if "n" in input("Would you like to stop moving? (Y/N) ").lower():
                os.system('cls' if os.name == 'nt' else 'clear')
                print("You did not move.")
                print_location(True)
                pass
            else:
                moving = False
                os.system('cls' if os.name == 'nt' else 'clear')
                return display_menu('game_menu')
        elif choice == "quit":
            back = input("Would you like to quit to main menu? (Y/N) ").lower()
            os.system('cls' if os.name == 'nt' else 'clear')
            if "n" in back:
                break
            else:
                return display_menu('main_menu')
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            try:
                menu['movement_menu'][choice]()
            except KeyError:
                print("That is not a direction")
                pass
            print_location()


def print_location(print_description=False):
    ''' Tells the player what room they are in. Can be passed
        a bool to make it describe the room or not.'''
    print(f"You are in the {current_room().capitalize()}")
    if print_description:
        print(_map.rooms[player['position'][2]][current_room()]['description'])


def current_room(y_offset=0, x_offset=0):
    return _map.game_map[player['position'][2]][player['position'][1] + y_offset][player['position'][0] + x_offset]  # map, y, x


def setup():
    os.system('cls' if os.name == 'nt' else 'clear')
    global desired_text_speed
    desired_text_speed = 0.025
    with open(save_file1) as file:  # Reads the speed on file and sets it
        for line in file.readlines():
            if "desiredTextSpeed" in line:
                line = line.strip().split('::')
                desired_text_speed = float(line[1])
    _print("This is the game's current text speed.")
    _print("Would you like to change the text speed? (Y/N) ", newline=False)
    if "n" in input().lower():
        os.system('cls' if os.name == 'nt' else 'clear')
        return None
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
            desired_text_speed = text_speeds[choice]
        elif choice in "quit":
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        else:
            pass
        _print("This is how fast the text will appear. Here is some extra text.")
    with open(save_file1, "r") as file:
        temp_list = file.readlines()  # Temp list of all lines in file
        temp_list[1] = f"desiredTextSpeed::{str(desired_text_speed)}\n"
        with open(save_file1, "w") as file:
            file.writelines(temp_list)  # Updates setting in file
    return None


def _print(text: str, delay=0.025, newline=True):
    try:  # Function prints text with a typing effect. 
        delay = desired_text_speed  # Has to be done this way...
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
    return display_menu('game_menu')


def play():
    with open(save_file1) as file:
        for line in file.readlines():
            if "skipIntroduction" in line:
                temp_line = line
        if temp_line == "skipIntroduction::False\n":
            with open(save_file1, "r") as file:
                temp_list = file.readlines()
                temp_list[2] = f"skipIntroduction::True\n"
            with open(save_file1, "w") as file:
                file.writelines(temp_list)
            if "n" in input("Would you like to skip the story introduction? (Y/N)").lower():
                return story()
    os.system('cls' if os.name == 'nt' else 'clear')
    while playing_game:
        return display_menu('game_menu')


def view_character():
    print("Stats:")
    print(player['character'])
    return display_menu('game_menu')


def view_inventory():
    print(player['inventory'].contents)
    return display_menu('game_menu')


def fight_test():
    _combat.combat(['goblin', 'goblin', 'blemmyae', 'manticore', 'orc'])


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
        "setup": setup,
        "quit": _quit
    },
    "game_menu": {
        "move": moving,
        "fight": fight_test,
        "view character": view_character,
        "inventory": view_inventory
    },
    "movement_menu": {"up": up, "down": down,
          "left": left, "right": right},

    #"combat_menu": {"attack": _combat.attack_menu, "item": _combat.use_item, "run": _combat.flee_battle}
}


def display_menu(current_menu):
    while True:
        if current_menu == 'main_menu':
            print(game_title)
        if current_menu == 'movement_menu':  # Movement menu is handled elsewhere
            print(update_map_display())
        print("\nOptions:")  # Prints and takes input for menu options
        for option in menu[current_menu]:
            print(" - " + option.capitalize())
        print(current_menu)
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
            menu[current_menu][choice]()
            break
        else:
            pass


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    global playing_game
    while playing_game:
        display_menu('main_menu')


# Main ------------------------------------------------------------------------
if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')  # Clears console
    with open(save_file1) as file:
        for line in file.readlines():
            if "setupCompleted" in line:
                temp_line = line
        if temp_line == "setupCompleted::True\n":
            pass
        else:  # Checks for first time boot
            choice = input("Would you like to change the "
                            + "default settings? (Y/N) ").lower()
            if "n" in choice:
                os.system('cls' if os.name == 'nt' else 'clear')
                pass
            else:
                setup()  # Makes user confirm settings before continuing
                file.close()
            with open(save_file1, "r") as file:
                temp_list = file.readlines()
                temp_list[0] = f"setupCompleted::True\n"
                file.close()
            with open(save_file1, "w") as file:
                file.writelines(temp_list)  # Future boots will skip
                file.close()
    while playing_game:
        main()
