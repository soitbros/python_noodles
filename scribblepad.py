#Write a function that reads the file words.txt and builds a list with one element per word. Write two versions of this function, one using the append method and the other using the idiom t = t + [x]. Which one takes longer to run? Why?

def word_list():
    x = []
    fin = open('words.txt')
    for line in fin:
        x.append(line.strip())
    print x

def word_lister():
    x = []
    fin = open('words.txt')
    for line in fin:
        x = x + [line.strip()]
    print x

print word_list()
