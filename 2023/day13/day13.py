from common_logic import CommonLogic


def get_value(arr):
    cur_time = int(arr[0])
    earliest_time = 999999999999
    min_bus_id = None
    dif = None
    for x in arr[1].split(','):
        if x == 'x':
            continue
        pos_time = 0
        while pos_time < cur_time:
            pos_time += int(x)
        if pos_time < earliest_time:
            earliest_time = pos_time
            min_bus_id = int(x)
            dif = pos_time - cur_time

    return min_bus_id * dif

##too long try again
def get_value_second_try(arr):
    arr = arr[1].split(',')
    dict_num_pos = {}
    for i, x in enumerate(arr):
        if x == 'x':
            continue
        else:
            dict_num_pos[x] = i
    attempt = 0
    value = None
    while True:
        attempt += 1
        for i, x in enumerate(dict_num_pos.keys()):
            if i == 0:
                value = int(x) * attempt
                continue
            if x == 'x':
                continue
            if (value + dict_num_pos[x]) % int(x) != 0:
                break
        else:
            return value

##chinese number theory and googling got me here
def second_question_trytwo(arr):
    busses = ["x" if x == "x" else int(x) for x in arr[1].split(",")]
    mods = {bus: -i % bus for i, bus in enumerate(busses) if bus != "x"}
    print(mods)
    vals = list(reversed(sorted(mods)))
    val = mods[vals[0]]
    r = vals[0]
    for b in vals[1:]:
        while val % b != mods[b]:
            val += r
        r *= b
    return val

if __name__ == '__main__':
    arr = CommonLogic.get_input_as_str_arr()
    #print('first question: ' + str(get_value(arr)))
    print('second question: ' + str(second_question_trytwo(arr)))
