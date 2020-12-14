from common_logic import CommonLogic


def get_value(arr):
    changed = True
    while(changed):
        changed = False
        for i,x in enumerate(arr):
           for inner_i, y in enumerate(x):
               if y == 'L':
                   if 0 < y < len(x) - 1:
                       if x[inner_i - 1] == '#'  and x[inner_i + 1] == '#':

                   else:
                       changed = True
                       y == '#'

def get_value_second_try(arr):
    pass


if __name__ == '__main__':
    arr = CommonLogic.get_input_as_int_arr()
    print('first question: ' + str(get_value(arr)))
    print('second question: ' + str(get_value_second_try(arr)))
