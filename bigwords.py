def big_words(int):
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if len(word) > int:
            print word

def has_no_e(word):
    for letter in word:
        if letter == 'e':
            return False
    return True

def has_no_e_big():
    fin = open('words.txt')
    count = 0.0
    count_no_e = 0.0
    for line in fin:
        word = line.strip()
        count += 1.0
        if word.find('e') == - 1:
            print word
            count_no_e += 1.0
    print (count_no_e/count)

def avoids(word, forbid):
    for e in forbid:
        if word.find(e) >= 0:
            return False
    return True

def avoids_big_words(forbid):
    fin = open('words.txt')
    count = 0
    counter = 0
    for line in fin:
        count += 1
        word = line.strip()
        if avoids(word, forbid) == True:
            print word
            counter += 1
    print ((1.0 * counter)/(1.0 * count))

def uses_only(word, okay):
    for e in word:
        if e not in okay:
            return False
    return True

def uses_only_words(okay):
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if uses_only(word, okay) == True:
            print word

def uses_all(word, shebang):
    return uses_only(shebang, word)

def uses_all_words(shebang):
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if uses_all(word, shebang) == True:
            print word

#uses_all_words('aeiou')

def is_abecedarian(word):
    prior = word[0]
    for e in word:
        if e < prior:
            return False
        prior = e
    return True

def wordlist():
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if is_abecedarian(word) == True:
            print word

wordlist()
