def generate_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    color_map_list = []
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            color_map_list.append((i * 5 + j, major, minor))
    print(color_map_list)
    return color_map_list

def print_color_map(color_map):
    for number, major_color,minor_color in color_map:
         print(f'{number} | {major_color} | {minor_color}')

color_map = generate_color_map()
print_color_map(color_map)
assert(len(color_map) == 25)
print("All is well (maybe!)\n")
