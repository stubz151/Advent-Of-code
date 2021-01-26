def make_change(denominations, amount):
    solution = [1] + [0] * amount
    for i in denominations:
        for j in range(i, amount + 1):
            solution[j] += solution[j-i]
    return solution[-1]


if __name__ == '__main__':
    denominations, amount = [1, 2, 5], 7
    print(make_change(denominations, amount))
