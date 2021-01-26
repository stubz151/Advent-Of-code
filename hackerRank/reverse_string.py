def reverse_sentence(word):
    return list(reversed(word.split(" ")))

if __name__ == '__main__':
    word = "hello world"
    print(reverse_sentence(word))
