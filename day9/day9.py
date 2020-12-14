from common_logic import CommonLogic


def check_value_is_in_preamble(arr, val):
    for i, x in enumerate(arr):
        for inner_index, y in enumerate(arr):
            if x + y == val:
                if inner_index != i:
                    return True
    return False


def get_value(arr):
    pre_amble_arr = arr[0:25]
    for x in arr[25:]:
        if check_value_is_in_preamble(pre_amble_arr, x):
            pre_amble_arr.append(x)
            pre_amble_arr = pre_amble_arr[1:]
        else:
            return x


def get_value_second_question(arr):
    first_weakness = get_value(arr)
    for i, x in enumerate(arr):
        arr_of_adders = []
        for y in arr[i:]:
            if sum(arr_of_adders) > first_weakness:
                break
            if sum(arr_of_adders) == first_weakness:
                return min(arr_of_adders) + max(arr_of_adders)
            arr_of_adders.append(y)


if __name__ == '__main__':
    print(get_value_second_question(CommonLogic.get_input_as_int_arr()))
