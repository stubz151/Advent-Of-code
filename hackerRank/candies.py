def min_candies(arr):
    min_values1 = [1] * len(arr)
    min_values2 = [1] * len(arr)
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            min_values1[i] += min_values1[i-1]
    for i in range(len(arr) - 2, -1, -1):
        if arr[i] > arr[i + 1]:
            min_values2[i] += min_values2[i+1]
    min_vals = sum([max(min_values1[i], min_values2[i]) for i in range(0, len(arr))])
    return min_vals


if __name__ == '__main__':
    arr = [4, 6, 4, 5, 6, 2]
    print (min_candies(arr))
