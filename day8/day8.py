from common_logic import CommonLogic


def get_value(instruction_arr):
    prev_i = []
    acc = 0
    i = 0
    while i < len(instruction_arr) - 1:
        if i in prev_i:
            return acc
        else:
            prev_i.append(i)
        instruction = instruction_arr[i].split(' ')[0]
        if instruction == 'nop':
            i += 1
            continue
        if instruction == 'acc':
            acc += int(instruction_arr[i].split(' ')[1])
            i += 1
            continue
        if instruction == 'jmp':
            i += int(instruction_arr[i].split(' ')[1])
            continue


def loop_through_and_check_if_arr_works(instruction_arr):
    prev_i = []
    acc = 0
    i = 0
    while i < len(instruction_arr):
        if i == len(instruction_arr):
            return True, acc
        if i in prev_i:
            return False, 0
        else:
            prev_i.append(i)
        instruction = instruction_arr[i].split(' ')[0]
        if instruction == 'nop':
            i += 1
            continue
        if instruction == 'acc':
            acc += int(instruction_arr[i].split(' ')[1])
            i += 1
            continue
        if instruction == 'jmp':
            i += int(instruction_arr[i].split(' ')[1])
            continue
    return True, acc


def get_value_second_question(instruction_arr):
    i = 0
    last_swap_pos = -1
    while i < len(instruction_arr):
        tuple_out = loop_through_and_check_if_arr_works(instruction_arr)
        if tuple_out[0]:
            return tuple_out[1]

        if last_swap_pos != -1:
            last_swop = instruction_arr[last_swap_pos]
            if last_swop.split(' ')[0] == 'nop':
                new_instruction = 'jmp ' + last_swop.split(' ')[1]
                instruction_arr[last_swap_pos] = new_instruction
                last_swap_pos = -1
            elif last_swop.split(' ')[0] == 'jmp':
                new_instruction = 'nop ' + last_swop.split(' ')[1]
                instruction_arr[last_swap_pos] = new_instruction
                last_swap_pos = -1

        instruction = instruction_arr[i]
        if instruction.split(' ')[0] == 'nop':
            new_instruction = 'jmp ' + instruction.split(' ')[1]
            instruction_arr[i] = new_instruction
            last_swap_pos = i
        elif instruction.split(' ')[0] == 'jmp':
            new_instruction = 'nop ' + instruction.split(' ')[1]
            instruction_arr[i] = new_instruction
            last_swap_pos = i
        i += 1


if __name__ == '__main__':
    print(get_value_second_question(CommonLogic.get_input_as_str_arr()))
