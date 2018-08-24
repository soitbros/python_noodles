def letter_fix(letter, int):
    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start = ord('a')
    else:
        return letter

    c = ord(letter) - start
    i = (c + int) % 26 + start
    return chr(i)

def rotate_word(word, int):
    word2 = ''
    for c in word:
        word2 += letter_fix(c, int)
        print c, word2
    return word2

print letter_fix('B', -7)
print rotate_word('CHEER', 7)
