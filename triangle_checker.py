def is_triangle(a,b,c):
    if (c <= a + b) and (a <= b + c) and (b <= a + c):
        print 'Yeah'
    else:
        print 'Nah'

def prompty():
    prompt = 'a?\n'
    a = int(raw_input(prompt))
    prompt = 'b?\n'
    b = int(raw_input(prompt))
    prompt = 'c?\n'
    c = int(raw_input(prompt))

    is_triangle(a,b,c)

prompty()
