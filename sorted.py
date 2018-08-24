def is_sorted(t):
    orig = t[:]
    t.sort()
    x = 0
    while x < len(t):
        if orig[x] == t[x]:
            x += 1
        else:
            return False
        return True

print is_sorted([1,2,2,3,4,5,6,7,8,11])
print is_sorted(['b','a'])
