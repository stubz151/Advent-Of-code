#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

def calc_production(arr, day):
    produced = 0
    for x in arr:
        produced += day // x

    return produced

# Complete the pairs function below.
def pairs(k, arr):
    arr.sort()
    upper_bound = (k // len(arr)) * arr[-1]
    lower_bound = (k // len(arr)) * arr[0]

    while lower_bound < upper_bound:
        middle_bound = (upper_bound + lower_bound) // 2
        a = calc_production(arr, middle_bound)
        if a > k:
            upper_bound = middle_bound
        else:
            lower_bound = middle_bound + 1
    return lower_bound


if __name__ == '__main__':
    k = 30

    arr = [1, 5, 3]

    result = pairs(k, arr)
    print(result)
