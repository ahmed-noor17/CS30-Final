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
        and the surrounding areas that you can move to. This gets
        written to an external text file.
    '''
    global map_display
    map_display = [
        [_map.game_map[player['position'][2]][player['position'][1]-1][player['position'][0]-1], _map.game_map[player['position'][2]][player['position'][1]-1][player['position'][0]], _map.game_map[player['position'][2]][player['position'][1]-1][player['position'][0]+1]],
        [_map.game_map[player['position'][2]][player['position'][1]][player['position'][0]-1], current_room(), _map.game_map[player['position'][2]][player['position'][1]][player['position'][0]+1]],
        [_map.game_map[player['position'][2]][player['position'][1]+1][player['position'][0]-1], _map.game_map[player['position'][2]][player['position'][1]+1][player['position'][0]], _map.game_map[player['position'][2]][player['position'][1]+1][player['position'][0]+1]]]
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
        display_menu('movement_menu')
        print_location(False)
        print("\n")


def print_location(print_description):
    ''' Tells the player what room they are in. Can be passed
        a bool to make it describe the room or not.'''
    print(f"You are in the {current_room().capitalize()}")
    if print_description:
        print(_map.rooms[current_room()]['description'])


def current_room():
    return _map.game_map[player['position'][2]][player['position'][1]][player['position'][0]]


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
    if "n" in input():
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
        _print(
            "This is how fast the text will appear. Here is some extra text.")
    with open(save_file1, "r") as file:
        temp_f_line_list = file.readlines()  # Temp list of all lines in file
        temp_f_line_list[1] = f"desiredTextSpeed::{str(desired_text_speed)}\n"
        with open(save_file1, "w") as file:
            file.writelines(temp_f_line_list)  # Updates setting in file
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
    with open(save_file1) as f:
        for line in f.readlines(3):
            if line == "skipIntroduction::True":
                pass
            elif "n" in input("Would you like to skip the story introduction? (Y/N)"):
                return story()
        with open(save_file1, 'w') as f:
            f.write("skipIntroduction::True")  # Future boots will skip
    os.system('cls' if os.name == 'nt' else 'clear')
    # print("Story...")  # Placeholder text for story introduction
    # time.sleep(2)
    # os.system('cls' if os.name == 'nt' else 'clear')
    # Code below should appear after story text.
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
    os.system('cls' if os.name == 'nt' else 'clear')
    exit("See you next time!")


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
        if choice == "quit" and current_menu != "main_menu":
            back = input("Would you like to quit to main menu? (Y/N) ")
            os.system('cls' if os.name == 'nt' else 'clear')
            if "n" in back:
                break
            else:
                return display_menu('main_menu')
        elif choice in menu[current_menu]:
            print("\n")
            menu[current_menu][choice]()
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    global playing_game
    while playing_game:
        display_menu('main_menu')


# Main ------------------------------------------------------------------------
if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')  # Clears console
    with open(save_file1) as f:
        for line in f.readlines():
            if line == "setupCompleted::True":
                pass
            elif line == "setupCompleted::False":  # Checks for first time boot
                choice = input("Would you like to change the "
                               + "default settings? (Y/N) ").lower()
                if "n" in choice:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    pass
                else:
                    setup()  # Makes user confirm settings before continuing
                    f.close()
                with open(save_file1, 'w') as f:
                    f.write("setupCompleted::True")  # Future boots will skip
    while playing_game:
        main()
