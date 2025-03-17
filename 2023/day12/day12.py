from common_logic import CommonLogic


def get_value(arr):
    ns_pos = 0
    ew_pos = 0
    cur_dir = 1
    directions = ['N', 'E', 'S', 'W']*1000
    for x in arr:
        command = x[0]
        value = int(x[1:])
        if command == 'F':
            command = directions[cur_dir]
        if command == 'N':
            ns_pos += value
        if command == 'S':
            ns_pos -= value
        if command == 'E':
            ew_pos += value
        if command == 'W':
            ew_pos -= value
        if command == 'L':
            cur_dir -= value//90
        if command == 'R':
            cur_dir += value//90
    return abs(ns_pos) + abs(ew_pos)


def get_value_second_try(arr):
    ns_pos = 0
    ew_pos = 0
    ns_pos_waypoint = 1
    ew_pos_waypoint = 10
    for x in arr:
        command = x[0]
        value = int(x[1:])
        if command == 'F':
            ns_pos = ns_pos + (ns_pos_waypoint * value)
            ew_pos = ew_pos + (ew_pos_waypoint * value)
        if command == 'N':
            ns_pos_waypoint += value
        if command == 'S':
            ns_pos_waypoint -= value
        if command == 'E':
            ew_pos_waypoint += value
        if command == 'W':
            ew_pos_waypoint -= value
        if command == 'L':
            i = 0
            while i < value//90:
                i += 1
                ns_pos_waypoint, ew_pos_waypoint = ew_pos_waypoint, -ns_pos_waypoint
        if command == 'R':
            i = 0
            while i < value//90:
                i += 1
                ns_pos_waypoint, ew_pos_waypoint = -ew_pos_waypoint, ns_pos_waypoint
    return abs(ns_pos) + abs(ew_pos)


if __name__ == '__main__':
    arr = CommonLogic.get_input_as_str_arr()
    print('first question: ' + str(get_value(arr)))
    print('second question: ' + str(get_value_second_try(arr)))
