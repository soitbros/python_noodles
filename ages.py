def ages(age, kid):
    if kid < 10:
        kid = str(kid).zfill(2)
    else:
        kid = str(kid)
    age = str(age)
    return age[::-1] == kid

def generate(adult):
    kid = 0
    count = 0
    while adult < 120:
        if ages(adult, kid) == True:
            count += 1
            if count == 6:
                print str(adult)[::-1]
        adult += 1
        kid += 1

def growup():
    adult = 10
    while adult < 120:
        generate(adult)
        adult += 1

growup()
