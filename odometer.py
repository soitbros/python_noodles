def palin(num):
    return num == num[::-1]

def odometer(num):
    last_four = str(num)[2:6]
    last_five = str(num + 1)[1:6]
    middle_four = str(num + 2)[1:5]
    all_six = str(num + 3)
    if palin(last_four) == True and palin(last_five) == True and palin(middle_four) and palin(all_six):
        return True

def count():
    i = 100000
    while i < 1000002:
        #print i
        if odometer(i) == True:
            print i
        i += 1

count()
