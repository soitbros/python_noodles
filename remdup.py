def remove_duplicates(t):
    s = t[:]
    s.sort()
    for i in range(len(s)):
        if s[i] == s[i + 1]:
            print s[i]
            del s[i + 1]
        print s

print remove_duplicates([5, 5, 3, 7, 12, 12, 9, 11, 11, 12, 11, 2, 3, 9, 9, 7, 2, 1, 9, 4])
