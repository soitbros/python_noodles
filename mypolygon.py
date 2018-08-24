try:
    # see if Swampy is installed as a package
    from swampy.TurtleWorld import *
except ImportError:
    # otherwise see if the modules are on the PYTHONPATH
    from TurtleWorld import *

import math

def move(t, length):
    pu(t)
    fd(t, length)
    pd(t)

def pie(t, n, r):
    angle = 360.0 / n
    angle_tri = 180 - ((180 - angle) / 2)
    sine = math.sin(math.radians(angle / 2))
    hypo = r * sine * 2
    #lt(t, 180)
    for i in range(n):
        lt(t, angle_tri)
        fd(t, hypo)
        lt(t, angle_tri)
        fd(t, r)
        lt(t, 180)
        fd(t, r)


world = TurtleWorld()
bob = Turtle()
bob.delay = 0.1

move(bob, -100)
#lt(bob, 180)
pie(bob, 5, 30)

move(bob, -100)
pie(bob, 6, 30)

move(bob, -100)
pie(bob, 7, 30)

die(bob)

world.canvas.dump()

wait_for_user()
