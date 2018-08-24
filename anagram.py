def is_anagram(a,b):
    a = list(a)
    a.sort()
    b = list(b)
    b.sort()
    x = 0
    while x < len(a):
        if len(a) != len(b):
            return False
        elif a[x] == b[x]:
            x += 1
        else:
            return False
        return True

print is_anagram('guinness', 'genuinec')
