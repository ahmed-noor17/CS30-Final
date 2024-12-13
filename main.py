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
import map as _map
from tabulate import tabulate
save_file1 = 'SaveSlot1.txt'
playing_game = True
game_title = '''
 _____ _____ _____ _____ _____ _____ _____
| __  |   __|   __| __  |   __|   __|   __|
|    -|   __|  |  |    -|   __|__   |__   |
|__|__|_____|_____|__|__|_____|_____|_____|\n'''

player_pos = [1, 4, "house"]  # [x, y, map]


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
    global player_pos
    print("Changing map...")
    player_pos = list(_map.rooms[current_room()]['connections'])


def update_position(axis, value):
    ''' Moves the player. Will not allow movement if the desired
        location is off the map or a negative number.'''
    if axis == "x":
        try:
            try_position = _map.game_map[player_pos[2]][player_pos[1]][player_pos[0] + value]
            if player_pos[0] + value < 0 or try_position == None or try_position == '':
                raise IndexError
            player_pos[0] += value
        except IndexError:
            print("You cannot go that way.")
    elif axis == "y":
        try:
            try_position = _map.game_map[player_pos[2]][player_pos[1] - value][player_pos[0]]
            if player_pos[1] - value < 0 or try_position == None or try_position == '':
                raise IndexError
            player_pos[1] -= value
        except IndexError:
            print("You cannot go that way.")


def update_map_display():
    ''' Creates and updates a separate map that displays your location
        and the surrounding areas that you can move to. This gets
        written to an external text file.
    '''
    global map_display
    map_display = [
        [_map.game_map[player_pos[2]][player_pos[1]-1][player_pos[0]-1], _map.game_map[player_pos[2]][player_pos[1]-1][player_pos[0]], _map.game_map[player_pos[2]][player_pos[1]-1][player_pos[0]+1]],
        [_map.game_map[player_pos[2]][player_pos[1]][player_pos[0]-1], f'*{_map.game_map[player_pos[2]][player_pos[1]][player_pos[0]]}*', _map.game_map[player_pos[2]][player_pos[1]][player_pos[0]+1]],
        [_map.game_map[player_pos[2]][player_pos[1]+1][player_pos[0]-1], _map.game_map[player_pos[2]][player_pos[1]+1][player_pos[0]], _map.game_map[player_pos[2]][player_pos[1]+1][player_pos[0]+1]]]
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
        moving = ("y" in input("Contiune moving? y/n: "))
        print("\n")


def print_location(print_description):
    ''' Tells the player what room they are in. Can be passed
        a bool to make it describe the room or not.'''
    print(f"You are in the {current_room().capitalize()}")
    if print_description:
        print(_map.rooms[current_room()]['description'])


def current_room():
    return _map.game_map[player_pos[2]][player_pos[1]][player_pos[0]]


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


def play():
    # SHOULD CHECK IF THERE IS A SAVE FILE HERE (to skip intro)
    os.system('cls' if os.name == 'nt' else 'clear')
    # print("Story...")  # Placeholder text for story introduction
    # time.sleep(2)
    # os.system('cls' if os.name == 'nt' else 'clear')
    # Code below should appear after story text.
    while playing_game:
        display_menu('game_menu')
        # r = display_menu('game_menu')
        # if r in ['game_menu', None]:
        #     r = 'game_menu'
        #     pass
        # else:
        #     return display_menu(r)


def _quit():
    global playing_game
    print("Press ENTER to confirm exit.")
    if input("(Or any character before ENTER to continue)") == '':
        playing_game = False
    os.system('cls' if os.name == 'nt' else 'clear')


menu = {
    "main_menu": {
        "play": play,
        "setup": setup,
        "quit": _quit
    },
    "game_menu": {
        "move": moving
    },
    "movement_menu": {"up": up, "down": down,
          "left": left, "right": right}
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
            back = input("Would you like to quit to main menu? (Y/N)")
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
    exit("See you next time!")
