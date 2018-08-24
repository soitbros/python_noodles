def gcd(a,b):
    while b != 0:
        print a, b, a%b
        (a,b) = (b, a % b)
    return a

print gcd(900,500)
