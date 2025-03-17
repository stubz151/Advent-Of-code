from common_logic import CommonLogic


def get_value(number):
    starting_num = 127
    starting_row = 7
    for i, val in enumerate(number[:len(number) - 3]):
        if val == 'F':
            num_to_min = pow(2, len(number) - i - 4)
            starting_num -= num_to_min
    for i, val in enumerate(number[len(number) - 3:]):
        if val == 'L':
            num_to_min = pow(2, len(number) - i - 8)
            starting_row -= num_to_min
    return (starting_num * 8) + starting_row


def get_highest_value(input_arr):
    highest_num = get_value(input_arr[0])
    for x in input_arr:
        if get_value(x) > highest_num:
            highest_num = get_value(x)
    return highest_num


def get_seat(input_arr):
    seat_arr = []
    for x in input_arr:
        seat_arr.append(get_value(x))
    seat_arr.sort()
    seat_number = -1
    print(seat_arr)
    for i, x in enumerate(seat_arr[:len(seat_arr) - 1]):
        if seat_arr[i+1] != x + 1:
            seat_number = x + 1
            break
    return seat_number


if __name__ == '__main__':
    print(get_seat(CommonLogic.get_input_as_str_arr()))
