def double_find(word):
    i = 0
    while i < len(word)-1:
        if len(word) < i+6:
            return False
        elif word[i] == word[i+1] and word[i+2] == word[i+3] and word[i+4] == word[i+5]:
            return True
        i += 1

def double_finder():
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if double_find(word) == True:
            print word

double_finder()
