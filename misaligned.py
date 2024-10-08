def generate_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    color_map_list = []
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            color_map_list.append((i * 5 + j, major, minor))
    return color_map_list

def print_color_map(color_map):
    for number, major_color,minor_color in color_map:
         print(f'{number} | {major_color} | {minor_color}')

color_map = generate_color_map()
expected_color_map_list =[(1, 'White', 'Blue'), (2, 'White', 'Orange'), (3, 'White', 'Green'), (4, 'White', 'Brown'), (5, 'White', 'Slate'), (6, 'Red', 'Blue'), (7, 'Red', 'Orange'), 
                (8, 'Red', 'Green'), (9, 'Red', 'Brown'), (10, 'Red', 'Slate'), (11, 'Black', 'Blue'), (12, 'Black', 'Orange'), (13, 'Black', 'Green'), (14, 'Black', 'Brown'), 
                (15, 'Black', 'Slate'), (16, 'Yellow', 'Blue'), (17, 'Yellow', 'Orange'), (18, 'Yellow', 'Green'), (19, 'Yellow', 'Brown'), (20, 'Yellow', 'Slate'), 
                (21, 'Violet', 'Blue'), (22, 'Violet', 'Orange'), (23, 'Violet', 'Green'), (24, 'Violet', 'Brown'), (25, 'Violet', 'Slate')]
assert color_map == expected_color_map_list
print_color_map(color_map)
assert(len(color_map) == 25)
print("All is well (maybe!)\n")
