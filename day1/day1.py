from common_logic import CommonLogic


def get_value(input_arr):
    for first_i, first_value in enumerate(input_arr):
        split_arr = input_arr[first_i+1:len(input_arr)]
        for second_i, second_value in enumerate(split_arr):
            second_split_arr = input_arr[second_i+1:len(split_arr)]
            for third_i, third_value in enumerate(second_split_arr):
                if first_value + second_value + third_value == 2020:
                    return first_value * second_value * third_value


if __name__ == '__main__':
    print(get_value(CommonLogic.get_input_as_int_arr()))
