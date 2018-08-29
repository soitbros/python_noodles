def remove_duplicates(y):
    y.sort()
    for x in range(len(y)):
        for b in range(len(y)):
            #print y[x], y[x+1], len(y)
            if x+1 >= len(y):
                return y
            elif y[x] == y[x+1]:
                print y[x+1]
                y.pop(x+1)
                #print y
    return False

print remove_duplicates([983729, 149642, 759581, 372597, 168322, 316553, 372597, 149642, 149642, 149642, 149642, 149642, 906787, 902873, 983729, 901716, 334035, 576690])
