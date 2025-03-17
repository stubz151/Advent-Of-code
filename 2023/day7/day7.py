import re

from common_logic import CommonLogic
from contextlib import redirect_stdout



def pretty(d, indent=0):
   for key, value in d.items():
      print('\t' * indent + str(key))
      if isinstance(value, dict):
         pretty(value, indent+1)
      else:
         print('\t' * (indent+1) + str(value))


def get_count_of_bags_with_goldbag_from_dict(dict_of_bags):
    ##keep a list of all bags that can hold shiny gold bag to avoid unnesscary traversals
    hasAccessToShinyGoldBagList = []
    keysAlreadyIn = []
    shouldRestart = True
    while shouldRestart:
        shouldRestart = False
        for key in keysAlreadyIn:
            del dict_of_bags[key]
            keysAlreadyIn = []
        for key in dict_of_bags:
            if key in hasAccessToShinyGoldBagList:
                shouldRestart = True
                keysAlreadyIn.append(key)
                break
            if any(i in hasAccessToShinyGoldBagList for i in dict_of_bags[key]):
                shouldRestart = True
                hasAccessToShinyGoldBagList.append(key)
                break
            if any('hinygold' in s for s in dict_of_bags[key]):
                shouldRestart = True
                hasAccessToShinyGoldBagList.append(key)
                break

    return len(hasAccessToShinyGoldBagList)


def get_value(arr):
    contains_dict = {}
    for y, line in enumerate(arr):
        arr[y] = arr[y].replace(' ', '')
        arr[y] = arr[y].replace('.', '')
        arr[y] = arr[y].replace('bag', '')
        arr[y] = arr[y].replace('s', '')
        value = re.split('contain|contains', arr[y])
        for i, word in enumerate(value):
            value[i] = ''.join(i for i in word if not i.isdigit())
        if value[0] in contains_dict:
            contains_dict[value[0]] = contains_dict[value[0]] + value[1].split(',')
        else:
            contains_dict[value[0]] = value[1].split(',')
    count = get_count_of_bags_with_goldbag_from_dict(contains_dict)
    return count


def get_count_of_bags_in_bag(bags, bag_to_count):
    count = 0
    for bag in bags[bag_to_count]:
        if bag[1:len(bag)] not in bags:
            count += int(bag[0])
        else:
            count = count + int(bag[0]) + (int(bag[0]) * get_count_of_bags_in_bag(bags, bag[1:len(bag)]))
    return count


def get_value_second_question(arr):
    contains_dict = {}
    for y, line in enumerate(arr):
        arr[y] = arr[y].replace(' ', '')
        arr[y] = arr[y].replace('.', '')
        arr[y] = arr[y].replace('bag', '')
        arr[y] = arr[y].replace('s', '')
        value = re.split('contain|contains', arr[y])
        bags_it_contains = value[1].split(',')
        for x in bags_it_contains:
            if not x.isnumeric():
                x = '1' + x
        if value[0] in contains_dict:
            contains_dict[value[0]] = contains_dict[value[0]] + value[1].split(',')
        else:
            if value[1] != 'noother':
                contains_dict[value[0]] = value[1].split(',')
    count = get_count_of_bags_in_bag(contains_dict, 'hinygold')

    return count

if __name__ == '__main__':
    print(get_value_second_question(CommonLogic.get_input_as_str_arr()))
