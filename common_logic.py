from typing import List
class CommonLogic:
    @staticmethod
    def get_input_as_int_arr():
        with open('input', 'r') as f:
            data = f.read()
            res = [int(i) for i in data.split()]
            return res

    @staticmethod
    def get_input_as_int_pairs_arr():
        with open('input', 'r') as f:
            data = f.read()
            arr = [i.split() for i in data.splitlines()]
        return arr

    @staticmethod
    def get_input_as_str_arr():
        with open('input', 'r') as f:
            data = f.read()
        res = [str(i) for i in data.splitlines()]
        return res

    @staticmethod
    def get_input_as_batches():
        with open('input', 'r') as f:
            data = f.read()
        concat_arr = ''
        res = []
        for x in data.split("\n"):
            if x == '':
                concat_arr = concat_arr[:len(concat_arr)-1]
                res.append(concat_arr)
                concat_arr = ''
            else:
                concat_arr += x + ' '
        return res

    @staticmethod
    def binary_search(arr: List, number, low, high):
        if low > high:
            return low
        mid = (low + high) // 2
        if number > arr[mid]:
            return CommonLogic.binary_search(arr, number, mid + 1, high)
        if number < arr[mid]:
            return CommonLogic.binary_search(arr, number, low, mid - 1)
        return mid

    @staticmethod
    def insert_sorted(arr: List, number):
        if len(arr) == 0:
            return [number]
        pointer = CommonLogic.binary_search(arr, number, 0, len(arr) - 1)

        return arr[:pointer] + [number] + arr[pointer:]

    @staticmethod
    def open():
        with open('input.txt', 'r') as fh:
            return fh
