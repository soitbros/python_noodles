import math
import sys

epsilon = sys.float_info.epsilon

def square_root(a,x):
    #print "Hiya Midge."
    while True:
        #print "a =",a, "x =", x, "start"
        y = (x + (a/x)) / 2
        #print "a =",a, "x =", x, "y =", y, "abs(y-x) =", abs(y-x), "epsilon =", epsilon, "before check"
        if abs(y-x) < epsilon:
            break
        x = y
        #print "a =",a, "x =", x, "y =", y, "abs(y-x) =", abs(y-x), "epsilon =", epsilon, "after check"
    print a, x, math.sqrt(a), math.sqrt(a) - x

def test_square_root(a,x):
    while a < 10:
        square_root(a,x)
        a = a + 1
        #print a,x


test_square_root(1.0,20.0)
