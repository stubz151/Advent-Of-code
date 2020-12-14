from common_logic import CommonLogic


def get_value(arr):
    count1 = 0
    count3 = 0
    for i in range(0, len(arr) - 1):
        if arr[i + 1] == arr[i] + 1:
            count1 += 1
        if arr[i + 1] == arr[i] + 3:
            count3 += 1
    return count1 * count3


# this is too slow had to try another way, recursion just branches out too far but could look at using
# an in memory structure maybe that contains the values of the nodes it has explored so it doesn't have to revisit
# Going to try traverse the list backwards as we know the value of the nodes then if that doesn't work will try recursion
def get_branch_count(arr):
    count = 0
    if len(arr) == 0:
        return 1
    val = arr[0]
    if len(arr) > 1 and arr[1] == val + 1:
        count += get_branch_count(arr[1:])
        if len(arr) > 2 and arr[2] == val + 2:
            count += get_branch_count(arr[2:]) + 1
            if len(arr) > 3 and arr[3] == val + 3:
                count += get_branch_count(arr[3:]) + 1
    if len(arr) > 1 and arr[1] == val + 2:
        count += 0 + get_branch_count(arr[1:])
        if len(arr) > 2 and arr[2] == val + 3:
            count += get_branch_count(arr[2:]) + 1
    if len(arr) > 1 and arr[1] == val + 3:
        count += get_branch_count(arr[1:])
    return count


def get_value_second(arr):
    return 1 + get_branch_count(arr)


# this way works really well, think I'm going to keep it
def get_value_second_try(arr):
    traversed_nodes_and_count = {
        len(arr) - 1: 1
    }
    for i, e in reversed(list(enumerate(arr[:-1]))):
        diff = arr[i + 1] - e
        if diff == 3:
            traversed_nodes_and_count[i] = traversed_nodes_and_count[i + 1]
        if diff == 2:
            traversed_nodes_and_count[i] = traversed_nodes_and_count[i + 1]
            if 0 <= i - 2 and arr[i + 2] - e == 3:
                traversed_nodes_and_count[i] = traversed_nodes_and_count[i] + traversed_nodes_and_count[i + 2]
        if diff == 1:
            traversed_nodes_and_count[i] = traversed_nodes_and_count[i + 1]
            if arr[i + 2] - e == 2:
                traversed_nodes_and_count[i] = traversed_nodes_and_count[i] + traversed_nodes_and_count[i + 2]
                if arr[i + 3] - e == 3:
                    traversed_nodes_and_count[i] = traversed_nodes_and_count[i] + traversed_nodes_and_count[i + 3]

    num_to_return = traversed_nodes_and_count[0] + traversed_nodes_and_count[1]
    return num_to_return


if __name__ == '__main__':
    sorted_list = sorted(CommonLogic.get_input_as_int_arr())
    sorted_list.append(sorted_list[-1] + 3)
    sorted_list.insert(0, 0)
    print('first question: ' + str(get_value(sorted_list)))
    print('second question: ' + str(get_value_second_try(sorted_list)))
