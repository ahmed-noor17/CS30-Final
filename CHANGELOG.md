# CHANGELOG

All notable changes made to the project will be documented here.


## 6 DECEMBER, 2024:

**Ahmed:**

Made a test build to test prerequisite functionalities.

- Music
- Sound effects
- Typewriter printing effect (for dialogue)


## 8 DECEMBER, 2024:

**Ahmed:**

- Got a semi-functional menu set up, with a big ASCII title.
- Made a settings menu where you can change text speed.


## 9 DECEMBER, 2024:

**Aiden:**

- Made some functions more efficient.
- Added a proper menu system.
- You can now go to "play" and there's a placeholder story introduction.

**Ahmed:**

- Cleaned up some of the code.
- Changing text speed in setting now saves to file.
- Made sure no errors could be produced.

**All:**

Decided against adding music, for now.


## 11 DECEMBER, 2024:

**Aiden:**

There is now a map movement system with placeholder maps.


## 12 DECEMBER, 2024:

**Ahmed:**

Updated map system to display a local map at all times while moving.

**Aiden:**

Assisted with bug fixing.


## 13 DECEMBER, 2024:

**Ahmed & Aiden:**

Fixed bugs


## 16 DECEMBER, 2024:

**Ahmed:**

Now checks if user has done the story intro

**Aiden:**

Added files for the attack and character classes


## 17 DECEMBER, 2024:

**Aiden**

- Added inventory
- Added under-construction combat and fixed movement
- Updated combat to have basic functionality


## 18 DECEMBER, 2024:

**Aiden**

- Updated combat to better support multiple enemies
- Added functionality for enemies atacking the player and fixed enemy naming

**Ahmed**

Partly made map


## 22 DECEMBER, 2024:

**Ahmed**

- Movement uses its own menu now and has been fixed
- Fixed bugs and improved performance when saving


# 23 DECEMBER, 2024:

**Ahmed**

Fixed setup menu bug and skip intro bug


# 25 DECEMBER, 2024:

**Ahmed**

Character and inventory bug fix, easy moving, and map update


# 6 JANUARY, 2025:

**Aiden**

- Made some small adjustments to combat
- Moved combat function to a module


# 7 JANUARY, 2025:

**Aiden**

- Made some small changes to saving
- Tiny fixes with save files
- Updated saving and loading (still can't save)


# 8 JANUARY, 2025:

**Aiden**

- Edited save files
- Fixed map position saving
- Fixed and added a lot of stuff relating to menu bugs
- Fixes relating to saving the game
- Combat fixes
- Added gold and experience points and their systems
- Added a game over
- Adjusted player stats
- Created a to-do list
- Added Area Of Effect attacks
- Added the ability to flee from battles
- Added consumable items during combat

**Ahmed**

- Ironwood map fix
- Inventory fix
- Cleaned comments
- Fixed saving
- Added and edited maps
- Added a tutorial map
- Updated to-do list
- Added shopping (doesn't work)


# 9 JANUARY, 2025:

**Aiden**

- Added random combat encounters
- Combat can now be done with just number keys.
- Adjusted enemies and made useful stats more visible during combat
- HP can no longer be more than max hp or less than 0 after an attack
- Fixed a weird save file glitch where it would load the wrong one
- Added numbered menus to item usage
- Made inventory viewing more presentable

**Ahmed**

- Fixes for movement and numbered menus
- Tried to make moving easier on eyes (didn't work)
- Made file selecting numbered


# 10 JANUARY, 2025:

**Aiden**

- Added attacks, enemies and items
- Made moving on map easier on eyes (added padding)
- Added story introduction dialogue
- Tweaked and fixed text speed
- Added a time system that when game ends

**Ahmed**

- Added buying from shops
- Improved readability of map by making all cells a similar size
- Fixed various bugs relating to shopping


# 11 JANUARY, 2025:

**Aiden**

- Added debuffs (damage over time and freezing) that can be applied to enemies by attacks
- Fixed a bug relating to winning using damage over time effects.
- Updated combat visuals
- Made inventory group items together when printing. e.g Iron Sword (x2)
- Added defence (reduces incoming damage)
- Made death sequence print text from a file and added new text
- Added credits screen

**Ahmed**

- Made it print "quit" as an option in the display_menu function
- Made it show valid options while moving (fight, shop, etc.)
- Fixed a bug relating to the player's inventory resetting on death
- Added the ability to sell items to shopkeepers.
- Changed combat to work with items being moved to item_data.py
- Changed player default name
- Fixed a bug relating to buying items from shops


# 12 JANUARY, 2025:

**Aiden**

- Made a map making tool to help speed up future map creation
- Added more maps
- Added large ascii text during combat to show when the player/enemy turn begins
- Updated _print() to allow printing large pieces of text line by line
- Made the size of the map adjustable for each map in map_data.py

**Ahmed**

- Made it so the map's width and height can be adjusted easily
- Added item and map descriptions
- Reduced nesting in display_map
- Made it print enemy and player health info every turn
- Organized files into folders
- Fixed a bug relating to selling items


# 13 JANUARY, 2025:

**Aiden**

- Added equipment and made the player be able to inherit new moves and defence from their equipment
- Fixed a bug relating to save data not saving properly
- Reformatted shopping to work with the display_menu() function
- Added dialogue to shops

**Ahmed**

- Uploaded sound files
- Fixed weird map text wrapping issues
- Improved consistency of map movement controls
- Fixed a bug where fleeing would instantly end the battle
- Made it print the movement controls when you begin moving
- Made it save your equipment to the save file
- Improved equip menus
- Fixed a bug where menus would kick you to the main menu when you exited them


# 14 JANUARY, 2025:

**Aiden**

- Made enemies able to drop items with a customizable random drop chance
- Added the Old Woods location

**Ahmed**

- Added sound effect system
- Added the Mount Megalos location
- Made shops print descriptions of items you are buying/selling and added confirmation prompts
- Rewrote movement function to fix issues with try/except
- Cleaned up code in display_menu() and moving()


# 15 JANUARY, 2025:

**Damian**

- Filled in the map for the City of Thieves location

**Aiden**

- Removed unnecessary maps in the files
- Added connections between all the new maps and the world map
- Added the bandit enemy
- Added King Megalos boss fight and related items
- Added the Tower of Doom location

**Ahmed**

- Made attacks print information about them when you are selecting them
- Added sound effects during combat
- Added music files and music implementation


# 16 JANUARY, 2025:

**Damian**

- Added more enemies

**Aiden**

- Added more bosses and boss drops
- Made it remember which bosses you have defeated so that you cannot fight them again

**Ahmed**

- Added new equipment items
- Reduced trailing whitespace
- Adjusted music volume


# 17 JANUARY, 2025:

**Ahmed**

- Added a function that makes numbered lists
- Did some PEP8 code styling
- Formatted save files
- Fixed a crash that could occur during combat


# 18 JANUARY, 2025:

**Aiden**

- Cleaned up main.py
- Added docstrings in main.py
- Moved shop data to a new shop_data.py file
- Reformatted some code for readability/simplicity
- Added the Wastes location
- Edited death.txt to fit with some of the newly added story
- Made defeated bosses save to the save file
- Added some story text
- Added victory.txt (will display when winning the game)
- Added user_documentation.txt
- Updated CHANGELOG.md

**Ahmed**

- Made it so that the player can cancel attacks and item usage
- Fixed an issue where you could not cancel buying/selling due to .lower()
- Made all lines 79 characters or less in length
- Made main.py adhere to PEP8 guidelines
- Added battle music
- Made music play at proper times
- Fixed a bug where the player could fight the same boss multiple times
- Fixed a crash that could occur during combat
- Updated CHANGELOG.md