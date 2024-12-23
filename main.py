###############################################################################
# Title: REGRESS
# Name: Ahmed Noor, Damian Knourek, Aiden Dielschneider
# Class: CS30
# Assignment: Final Project
# Version: TEST3
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
save_file1 = 'SaveSlot1.txt'
playing_game = True
game_title = '''
 _____ _____ _____ _____ _____ _____ _____
| __  |   __|   __| __  |   __|   __|   __|
|    -|   __|  |  |    -|   __|__   |__   |
|__|__|_____|_____|__|__|_____|_____|_____|\n'''

player = {
	'character': _character.Character("you", 100, 5, 95, ['slash', 'fireball']),
	'position': [1, 4, "house"],  # [x, y, map]
	'inventory': _inventory.Inventory([None]),
    'enemies': {}
}

enemies = {
	'goblin': ["goblin", 50, 5, 80, ['slash']],
	'orc': ["orc", 100, 8, 80, ['slash']]
}

attacks = {
	'slash': _attack.Attack(5, 100, 'slashed!'),
	'fireball': _attack.Attack(10, 99999, 'casted fireball!')
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
    player['position'] = list(_map.rooms[current_room()]['connections'])


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


def moving():
    moving = True
    print("You begin moving.")
    while moving:
        try:
            if _map.rooms[current_room()]['connections']:
                menu['movement_menu']['enter'] = change_map
        except KeyError:
            try:
                menu['movement_menu'].pop('enter')
            except Exception:
                pass
        print(update_map_display() + "\n")  # This is where the menu code starts
        for option in menu["movement_menu"]:  # You can move this to a separate function if you want, Aiden
            print(" - " + option.capitalize())
        choice = input("\nChoice: ").lower()
        if choice == "stop":
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
        print(_map.rooms[current_room()]['description'])


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
    pass


def play():
    with open(save_file1) as file:
        for line in file.readlines():
            if "skipIntroduction" in line:
                temp_line = line
        if temp_line == "skipIntroduction::True\n":
            pass
        elif "n" in input("Would you like to skip the story introduction? (Y/N)").lower():
            return story()
        else:
            with open(save_file1, "r") as file:
                temp_list = file.readlines()
                temp_list[2] = f"skipIntroduction::True\n"
            with open(save_file1, "w") as file:
                file.writelines(temp_list)
    os.system('cls' if os.name == 'nt' else 'clear')
    while playing_game:
        display_menu('game_menu')


def view_character():
    print("Stats:")
    print(player['character'])


def view_inventory():
    print(player['inventory'].contents)


def fight_test():
    combat(['goblin', 'goblin', 'goblin', 'goblin', 'goblin', 'orc'])


def enemy_turn():
    for enemy in list(player['enemies'].keys()):
        enemy_object = player['enemies'][enemy]
        use_attack(attacks[enemy_object.moves[0]], enemy_object, player['character'])
        print(f"{enemy_object.name.title()} took a turn!")



def combat(encounter_enemies):
    for enemy in encounter_enemies:
        enemy_object = _character.Character(enemies[enemy][0], enemies[enemy][1], enemies[enemy][2], enemies[enemy][3], enemies[enemy][4])
        enemy_count = 1
        while enemy_object.name in list(player['enemies'].keys()):
            enemy_count += 1
            if enemy_count > 2:  # This names the enemies if there are multiple of the same type
                enemy_object.name = f"{enemy_object.name[:-2]} {str(enemy_count)}"
            else:
                enemy_object.name = f"{enemy_object.name} {str(enemy_count)}"
        player['enemies'][enemy_object.name] = enemy_object
        print(f"You encountered a {enemy}")

    fighting = True
    while fighting:
        print(f"\nHP: {player['character'].hp}/{player['character'].max_hp}")
        display_menu('combat_menu')
        if len(list(player['enemies'].keys())) <= 0:
            print("You won!")
            fighting = False
            break
        enemy_turn()
        if player['character'].hp <= 0:
            print("You lost!")
            fighting = False
            #game_over()
            break
    player['enemies'].clear()


def attack_menu():
    print("Attacks:")
    for attack in player['character'].moves:
        print(f" - {attack.title()}")
    while True:
        use_move = input("Choose a move: ").lower()
        if use_move in player['character'].moves and use_move in list(attacks.keys()):
            while True:
                #if len(list(player['enemies'].keys())) <= 1:
                    #target = player['enemies'][0]
                #else:
                for target_enemy in list(player['enemies'].keys()):
                    print(f" - {target_enemy.title()}")
                target = input("Choose a target: ").lower()
                if target in list(player['enemies'].keys()):
                    use_attack(attacks[use_move], player['character'], player['enemies'][target])
                    break
            break


def flee_battle():
    print("You cannot flee yet!")
    pass


def use_item():
    print("You cannot use items yet!")
    pass


def use_attack(attack, attacker, target):
    attack_accuracy = attack.acc * attacker.acc/100
    if random.randint(0, 100) <= attack_accuracy:
        attack_damage = attack.damage * attacker.atk
        target.hp -= attack_damage
        print(f"{attacker.name.title()} {attack.use_text}")
        print(f"Dealt {attack_damage} damage!")
        print(f"{target.name.title()} has {target.hp} health remaining!")
        if target.hp <= 0:
            print(f"Defeated {target.name.title()}!")
            if target.name != 'you':
                player['enemies'].pop(target.name)
    else:
        print(f"{attacker.name.title()} missed! What an idiot!")


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

    "combat_menu": {"attack": attack_menu, "item": use_item, "run": flee_battle}
}


def display_menu(current_menu):
    while True:
        if current_menu == 'main_menu':
            print(game_title)
        if current_menu == 'movement_menu':
            print(update_map_display())
        print("\nOptions:")  # Prints and takes input for menu options
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
            print("\n")
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
