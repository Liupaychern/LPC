layers = input("Enter the number of layers (2 to 5) = ")
side_length = input("Enter the side length of the top layer = ")
growth = input("Enter the growth of each layer = ")
trunk_width = input("Enter the trunk width (odd number, 3 to 9) = ")
trunk_height = input("Enter the trunk height (4 to 10) = ")

layers = int(layers)
side_length = int(side_length)
growth = int(growth)
trunk_width = int(trunk_width)
trunk_height = int(trunk_height)

# calculate the last bottom
final_side_length = side_length + (layers - 1) * growth
final_bottom_length = 2 * final_side_length - 1

# print the first #
print("#")
current_layer = 1
while current_layer <= layers:
    base = 3
    while base <= 2 * (side_length) - 1:
        # 3 -> 5 -> 3*(side_length)-1
        space = (final_bottom_length - base) // 2
        if base == 2 * (side_length) - 1:
            print(" " * space + "#" * base)
        else:
            print(" " * space + "#" + "@" * (base - 2) + "#")
        base = base + 2
    side_length = side_length + growth
    current_layer = current_layer + 1

