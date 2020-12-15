from common_logic import CommonLogic
import numpy as np
import sys

np.set_printoptions(threshold=sys.maxsize)


def check_adjacent_seats(arr, x_pos, y_pos):
    count = 0
    #up
    if x_pos != 0 and arr[x_pos - 1][y_pos] == '#':
        count += 1
    #up left
    if x_pos != 0 and y_pos != 0 and arr[x_pos - 1][y_pos - 1] == '#':
        count += 1
    #up right
    if x_pos != 0 and y_pos < len(arr[x_pos - 1]) - 1 and arr[x_pos - 1][y_pos + 1] == '#':
        count += 1
    #left
    if y_pos != 0 and arr[x_pos][y_pos - 1] == '#':
        count += 1
    #right
    if y_pos < len(arr[x_pos]) - 1 and arr[x_pos][y_pos + 1] == '#':
        count += 1
    #down
    if x_pos < len(arr) - 1 and arr[x_pos + 1][y_pos] == '#':
        count += 1
    #down left
    if x_pos < len(arr) - 1 and y_pos != 0 and arr[x_pos + 1][y_pos - 1] == '#':
        count += 1
    #down right
    if x_pos < len(arr) - 1 and y_pos < len(arr[x_pos + 1]) - 1 and arr[x_pos + 1][y_pos + 1] == '#':
        count += 1
    return count

def play_the_game(arr):
    matrix = [list(row) for row in arr]
    changed = True
    while changed:
        cloned_matrix = [row[:] for row in matrix]
        changed = False
        for i, x in enumerate(cloned_matrix):
            for inner_i, y in enumerate(x):
                if y == 'L' and check_adjacent_seats(cloned_matrix, i, inner_i) == 0:
                    changed = True
                    matrix[i][inner_i] = '#'
                elif y == '#' and check_adjacent_seats(cloned_matrix, i, inner_i) >= 4:
                    changed = True
                    matrix[i][inner_i] = 'L'
        print(np.matrix(matrix))
    return matrix


def Up(arr, x_pos, y_pos):
    value = arr[x_pos - 1][y_pos]
    if value == '.' and x_pos > 1:
        return Up(arr, x_pos - 1, y_pos)
    elif value == '#':
        return True
    return False


def Down(arr, x_pos, y_pos):
    value = arr[x_pos + 1][y_pos]
    if value == '.' and x_pos < len(arr) - 2:
        return Down(arr, x_pos + 1, y_pos)
    elif value == '#':
        return True
    return False


def Left(arr, x_pos, y_pos):
    value = arr[x_pos][y_pos - 1]
    if value == '.' and y_pos > 1:
        return Left(arr, x_pos, y_pos - 1)
    elif value == '#':
        return True
    return False


def Right(arr, x_pos, y_pos):
    value = arr[x_pos][y_pos + 1]
    if value == '.' and y_pos < len(arr[x_pos]) - 2:
        return Right(arr, x_pos, y_pos + 1)
    elif value == '#':
        return True
    return False


def UpLeft(arr, x_pos, y_pos):
    value = arr[x_pos - 1][y_pos - 1]
    if value == '.' and x_pos > 1 and y_pos > 1:
        return UpLeft(arr, x_pos - 1, y_pos - 1)
    elif value == '#':
        return True
    return False


def UpRight(arr, x_pos, y_pos):
    value = arr[x_pos - 1][y_pos + 1]
    if value == '.' and x_pos > 1 and y_pos < len(arr[x_pos - 1]) - 2:
        return UpRight(arr, x_pos - 1, y_pos + 1)
    elif value == '#':
        return True
    return False


def DownLeft(arr, x_pos, y_pos):
    value = arr[x_pos + 1][y_pos - 1]
    if value == '.' and x_pos < len(arr) - 2 and y_pos > 1:
        return DownLeft(arr, x_pos + 1, y_pos - 1)
    elif value == '#':
        return True
    return False


def DownRight(arr, x_pos, y_pos):
    value = arr[x_pos + 1][y_pos + 1]
    if value == '.' and x_pos < len(arr) - 2 and y_pos < len(arr[x_pos + 1]) - 2:
        return DownRight(arr, x_pos + 1, y_pos + 1)
    elif value == '#':
        return True
    return False


def check_adjacent_seats_part_two(arr, x_pos, y_pos):
    count = 0
    #up
    if x_pos != 0 and Up(arr,x_pos,y_pos):
        count += 1
    #up left
    if x_pos != 0 and y_pos != 0 and UpLeft(arr, x_pos, y_pos):
        count += 1
    #up right
    if x_pos != 0 and y_pos < len(arr[x_pos - 1]) - 1 and UpRight(arr, x_pos, y_pos):
        count += 1
    #left
    if y_pos != 0 and Left(arr, x_pos, y_pos):
        count += 1
    #right
    if y_pos < len(arr[x_pos]) - 1 and Right(arr, x_pos, y_pos):
        count += 1
    #down
    if x_pos < len(arr) - 1 and Down(arr, x_pos, y_pos):
        count += 1
    #down left
    if x_pos < len(arr) - 1 and y_pos != 0 and DownLeft(arr, x_pos, y_pos):
        count += 1
    #down right
    if x_pos < len(arr) - 1 and y_pos < len(arr[x_pos + 1]) - 1 and DownRight(arr,x_pos, y_pos):
        count += 1
    return count


def play_the_game_part_2(arr):
    matrix = [list(row) for row in arr]
    changed = True
    while changed:
        cloned_matrix = [row[:] for row in matrix]
        changed = False
        for i, x in enumerate(cloned_matrix):
            for inner_i, y in enumerate(x):
                if y == 'L' and check_adjacent_seats_part_two(cloned_matrix, i, inner_i) == 0:
                    changed = True
                    matrix[i][inner_i] = '#'
                elif y == '#' and check_adjacent_seats_part_two(cloned_matrix, i, inner_i) >= 5:
                    changed = True
                    matrix[i][inner_i] = 'L'
        print(np.matrix(cloned_matrix))
    return matrix








def get_value_second_try(arr):
    mat = play_the_game_part_2(arr)
    print(np.matrix(mat))
    count = 0
    for x in mat:
        for y in x:
            if y == '#':
                count += 1
    return count


def get_value(arr):
    mat = play_the_game(arr)
    count = 0
    for x in mat:
        for y in x:
            if y == '#':
                count += 1
    return count


if __name__ == '__main__':
    arr = CommonLogic.get_input_as_str_arr()
    print('second question: ' + str(get_value_second_try(arr)))
