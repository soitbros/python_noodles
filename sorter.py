import random

def swap(t,i,j):
    temp = t[i]
    t[i] = t[j]
    t[j] = temp

def flipper(t):
    i = 0
    while i < range(len(t)-1):
        if i == len(t)-1:
            return t
        elif t[i] > t[i+1]:
            swap(t,i,i+1)
            print 'Starting over!'
            i = 0
        else:
            i += 1

def repeat_flip(t):
    for i in range(len(t)):
        t = flipper(t)
    return t

def random_list(y):
    t = []
    for i in range(y):
        bday = random.randint(1,12)
        t.append(bday)
    return t

#print random_list(20)

#print flipper([10, 5, 12, 3, 8, 4, 11, 3, 3, 2, 3, 1, 11])
print flipper([12, 2, 3, 3, 3, 13, 4, 5, 8, 10, 11, 11, 12])
#print flipper([5, 10, 3, 12, 4, 8, 3, 11, 2, 3, 1, 3, 11])
#print flipper([5, 3, 10, 4, 12, 3, 8, 2, 11, 1, 3, 3, 11])
#print flipper([3, 5, 4, 10, 3, 12, 2, 8, 1, 11, 3, 3, 11])
#print flipper([3, 4, 5, 3, 10, 2, 12, 1, 8, 3, 11, 3, 11])
#print flipper([3, 4, 3, 5, 2, 10, 1, 12, 3, 8, 3, 11, 11])
#print flipper([3, 3, 4, 2, 5, 1, 10, 3, 12, 3, 8, 11, 11])

#print flipper([9, 8, 12, 10, 5, 6])
