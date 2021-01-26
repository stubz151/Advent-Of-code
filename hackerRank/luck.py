#!/bin/python3

import math
import os
import random
import re
import sys
import bisect

# Complete the luckBalance function below.
from common_logic import CommonLogic


def luckBalance(k, contests):
    important_contests = []
    luck_total = 0
    for x in contests:
        luck = int(x[0])
        importance = int(x[1])
        if luck >= 0 and importance == 0:
            luck_total += luck
        elif importance == 1:
            bisect.insort(important_contests, luck)

    if len(important_contests) < k:
        for y in important_contests:
            if y > 0:
                luck_total += y
    else:
        for y in important_contests[len(important_contests) - k:]:
                if y > 0:
                    luck_total += y
    return luck_total


if __name__ == '__main__':
    k = 58
    arr = CommonLogic.get_input_as_int_pairs_arr()

    result = luckBalance(k, arr)
    print(result)
