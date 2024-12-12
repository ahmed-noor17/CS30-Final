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
save_file1 = 'SaveSlot1.txt'
playing_game = True
game_title = '''
 _____ _____ _____ _____ _____ _____ _____
| __  |   __|   __| __  |   __|   __|   __|
|    -|   __|  |  |    -|   __|__   |__   |
|__|__|_____|_____|__|__|_____|_____|_____|\n'''
game_map = {"house": [[None, "backyard", None, None],
       ["dining room", "back door", "lounge", None],
       ["kitchen", "hallway", "stairwell", None],
       ["living room", "foyer", "bedroom", None],
       ["bathroom", "entrance hall", "laundry room", "garage"]],

"dungeon": [['witchery room','warden office','orb vault','meeting room','dungeon guard room'],
        ['experimentation room','equipment room','hallway','dark room','solitary confinement'],
        ['library','hallway','stairwell','hallway','the gargoyle'],
        ['portal room','workshop','hallway','prison cell','torture room'],
        ['chapel','summoning room','entrance','prison cell','prison cell']]

}
rooms = {
    "kitchen": {"description": "The kitchen is very tidy."},
    "dining room": {"description": "There is a table and many chairs."},
    "stairwell": {"description": "There is a large staircase."},
    "living room": {"description": "The TV is playing something."},
    "foyer": {"description": "Paintings hang on the walls around you."},
    "bedroom": {"description": "The room is very messy."},
    "bathroom": {"description": "The sink is running."},
    "entrance hall": {"description": "The front door is locked."},
    "garage": {"description": "There are no cars in the garage."},
    "laundry room": {"description": "There are no cars in the garage."},
    "back door": {"description": "This door leads to the dungeon.", "connections": [2, 4, "dungeon"]},
    "hallway": {"description": "A long carpet is rolled out on the floor."},
    "backyard": {"description": "The sun is shining and a peaceful breeze is blowing."},
    "witchery room": {"description": "there's a cauldron and many odd looking plants."},
    "warden office": {"description": "there's a singular desk with a light above, and some paperwork in a scripture you don't recognize."},
    "orb vault": {"description": "you do not what's in the orb vault, but you can sense an orb in there..."},
    "meeting room": {"description": "there's a singular desk with many chairs around."},
    "dungeon guard room": {"description": "there's a few bunk beds around and a game of monopoly on a nightstand."},
    "experimentation room": {"description": "there's a surgical desk with blood all around and some strange tools."},
    "equipment room": {"description": "it seems this is where the guards keep their equipment..."},
    "dark room": {"description": "it is pitch black inside this room, your eyes make out some odd shapes in the corners of the room. You feel a presence looming over you..."},
    "solitary confinement":{"description": "a singular skeleton rests hanged by chains on the wall of this dimly lit room."},
    "library": {"description": "it seems this is where they kept records of experiments. You cannot make sense of any of it."},
    "stairwell": {"description": "it leads upwards, into the darkness. Perhaps you shouldn't venture more..."},
    "the gargoyle": {"description": "a stone statue of a gargoyle pierces your soul with its stare inside this room"},
    "portal room": {"there's a portal on the wall. You do not know where it leads."},
    "workshop": {"description": "there are many unfamiliar tools here, it seems to be a workshop."},
    "prison cell": {"description": "it looks like your average jail cell. "},
    "entrance": {"description": "this leads to your house.", "connections": [1, 4, "house"]},
    "chapel": {"description": "this room seems it's where they worshipped someone... or something...?"},
    "summoning room": {"description": "there's an ominous summoning circle in the middle of the room with candles surrounding it."}
    }
player_pos = [1, 4, "house"]  # [x, y, map]

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
    player_pos = list(rooms[current_room()]['connections'])


def update_position(axis, value):
    ''' Moves the player. Will not allow movement if the desired
        location is off the map or a negative number.'''
    if axis == "x":
        try:
            try_position = game_map[player_pos[2]][player_pos[1]][player_pos[0] + value]
            if player_pos[0] + value < 0 or try_position == None:
                raise IndexError

            player_pos[0] += value
        except IndexError:
            print("You cannot go that way.")
    else:
        try:
            try_position = game_map[player_pos[2]][player_pos[1] - value][player_pos[0]]
            if player_pos[1] - value < 0 or try_position == None:
                raise IndexError

            player_pos[1] -= value
        except IndexError:
            print("You cannot go that way.")


def moving():
    moving = True
    print("You begin moving.")
    while moving:
        try:
            # The room we are in has a connection to another map
            print(rooms[current_room()]['connections'])
            menu['movement_menu']['enter'] = change_map
        except KeyError:
            # The room we are in has no connections to other maps
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
        print(rooms[current_room()]['description'])


def current_room():
    return game_map[player_pos[2]][player_pos[1]][player_pos[0]]


# Functions -------------------------------------------------------------------
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
    print("Story...")  # Placeholder text for story introduction
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    # Code below should appear after story text.
    while playing_game:
        r = display_menu('game_menu')
        if r in ['game_menu', None]:
            r = 'game_menu'
            pass
        else:
            return display_menu(r)


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
                current_menu = 'main_menu'
                return current_menu
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
