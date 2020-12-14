from common_logic import CommonLogic


def loop_find_trees_count(x_skip, y_skip, input_arr):
    count = 0
    y = 0
    x = 0
    while y < len(input_arr):
        value = input_arr[y]
        while x + x_skip > len(value):
            value = value + value
        if value[x] == '#':
            count += 1
        x += x_skip
        y += y_skip
    return count


def get_value(input_arr):
    return loop_find_trees_count(3, 1, input_arr)


def get_value_second_challenge(input_arr):
    right1down1 = loop_find_trees_count(1, 1, input_arr)
    right3down1 = loop_find_trees_count(3, 1, input_arr)
    Right5down1 = loop_find_trees_count(5, 1, input_arr)
    right7down1 = loop_find_trees_count(7, 1, input_arr)
    right1down2 = loop_find_trees_count(1, 2, input_arr)
    return right1down1 * right1down2 * right7down1 * right3down1 * Right5down1


if __name__ == '__main__':
    print(get_value_second_challenge(CommonLogic.get_input_as_str_arr()))
