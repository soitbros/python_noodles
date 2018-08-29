def has_duplicates(y):
    x = 0
    while x < len(y):
        b = x + 1
        while b < len(y):
            if y[x] == y[b]:
                return True
            b += 1
        x += 1
    return False

print has_duplicates([983729, 149642, 759581, 372597, 168322, 316553, 906787, 902873, 983729, 901716, 334035, 576690])
