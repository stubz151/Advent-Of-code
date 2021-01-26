#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
from common_logic import CommonLogic


def getMinimumCost(k, c):
    num_of_friends = k
    length_of_list = len(c)
    array_of_friends = [1] * num_of_friends
    cost = 0
    c = sorted(c)
    if length_of_list == num_of_friends:
        return sum(c)
    friendix = 0
    for i, x in enumerate(reversed(c)):
        cost += x * array_of_friends[friendix]
        array_of_friends[friendix] += 1
        friendix += 1
        if friendix == num_of_friends:
            friendix = 0
        if i == length_of_list - num_of_friends:
            friendix = 0
            array_of_friends = sorted(array_of_friends)
    return cost


if __name__ == '__main__':

    k = 34
    c = CommonLogic.get_input_as_int_arr()
    minimumCost = getMinimumCost(k, c)
    print(minimumCost)
