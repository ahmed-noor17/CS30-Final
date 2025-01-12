import random

for num in range(9, 7):
    print(num)

template = '''"map_title": {
    "map": [],
    "data": {
        "random_encounter_chance": 0,
        "encounters": [],
        "move_time": 0,
    }
}'''

map_title = input("Map title: ")
map_width = int(input("Width: "))
map_height = int(input("Height: "))
map_contents = []
map_edge = []
path_y_position = []
dungeon = True

# Generate the top and bottom edges
for i in range(map_width + 2):
    map_edge.append('---')

map_contents.append(map_edge)
for i in range(map_height):
    path_y_position.append(random.randint(1, map_width))
    map_row = []
    map_row.append('---')
    for i in range(map_width):
        if random.randint(0, 1) == 0 or not dungeon:  # If we're making a dungeon, randomly scatters walls everywhere. The code below the next comment makes the layout not terrible.
            map_row.append('   ')
        else:
            map_row.append('---')
    map_row.append('---')

    map_contents.append(map_row)
map_contents.append(map_edge)

# This will draw a path from the top to the bottom of the dungeon to make sure you can actually get to the end, very cool
if dungeon:
    i = 0
    for pos in path_y_position:
        if i == map_height - 1:
            map_contents[i + 1][path_y_position[i]] = '   '
        elif not i >= map_height - 1:
            for num in range(min(path_y_position[i], path_y_position[i + 1]), max(path_y_position[i], path_y_position[i + 1]) + 1):
                map_contents[i + 1][num] = '   '
        i += 1

print(template.replace('map_title', map_title).replace('"map": []', '"map": ' + str(map_contents).replace('],', '],\n' + " "*11)))