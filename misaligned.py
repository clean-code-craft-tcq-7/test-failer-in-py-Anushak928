def generate_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    return [(i * 5 + j + 1, major, minor) for i, major in enumerate(major_colors) for j, minor in enumerate(minor_colors)]


def print_color_map():
    color_map_for_print = generate_color_map()
    print(f'{"No":<3} | {"Major":<6} | {"Minor":<6}')
    print('-' * 25)
    for num, major, minor in color_map_for_print:
        print(f'{num:<3} | {major:<6} | {minor:<6}')
    return len(color_map_for_print)


# Simple tests
color_map_for_test = generate_color_map()
assert(len(color_map_for_test) == 25)
assert(color_map_for_test[0] == (1, "White", "Blue"))
assert(color_map_for_test[-1] == (25, "Violet", "Slate"))

result = print_color_map()
assert(result == 25)
print("All is well (maybe!)")
