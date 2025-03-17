from common_logic import CommonLogic


def get_count(arr):
    count = 0
    for x in arr:
        x = x.replace(" ", "")
        myset = set(x)
        count += len(myset)
    return count


def get_count_second_question(arr):
    count = 0
    for x in arr:
        line = x.split(' ')
        for y in line[0]:
            if (x.count(y)) == len(line):
                count +=1
    return count


if __name__ == '__main__':
    print(get_count_second_question(CommonLogic.get_input_as_batches()))
