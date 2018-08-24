import random

def birthdays(y):
    t = []
    for i in range(y):
        bday = str(random.randint(1,12)) + '-' + str(random.randint(1,31))
        t.append(bday)
    return t

def has_duplicates(y):
    x = 0
    m = birthdays(y)
    while x < len(m):
        b = x + 1
        while b < len(m):
            if m[x] == m[b]:
                return True
            b += 1
        x += 1
    return False

#print has_duplicates()

def birthday_probability(x,y):
    times = 0
    pluses = 0
    while x > 0:
        if has_duplicates(y) == True:
            pluses += 1
        times += 1
        x -= 1
    total = (1.0 * pluses / times)
    return total

print birthday_probability(1000,23)
print birthday_probability(1000,70)
