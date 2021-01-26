def can_segement(s, word_dict):
    dp = [True] + [False] * len(s)
    for i in range(1, len(s) + 1):
        print(s[:i])
        for word in word_dict:
            if dp[i]:
                break
            if s[:i].endswith(word):
                dp[i] = dp[i - len(word)]
    return dp[-1]


if __name__ == '__main__':
    c = 'applepenapple'
    word_dict = ['apple', 'pen']
    print(can_segement(c, word_dict))
