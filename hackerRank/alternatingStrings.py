def alternatingCharacters(s):
    deletions = 0
    for i in range(1, len(s) - 1):
        if s[i - 1] == s[i]:
            deletions += 1
    return deletions

if __name__ == '__main__':
    s = "ABABABAB"
    result = alternatingCharacters(s)
    print(result)
