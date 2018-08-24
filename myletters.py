try:
    # see if Swampy is installed as a package
    from swampy.TurtleWorld import *
except ImportError:
    # otherwise see if the modules are on the PYTHONPATH
    from TurtleWorld import *

import math

def line(t, length, angle):
    lt(t, angle)
    fd(t, length)

def arc(t, length, angle):
    arc_length = 2 * math.pi * length * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    rt(t, step_angle/2)
    for i in range(n):
        fd(t, step_length)
        rt(t, step_angle)
    rt(t, step_angle/2)

def move(t, length):
    pu(t)
    fd(t, length)
    pd(t)

def draw_a(bob, size):
    angle = 70
    comp_angle = 360 - (2 * angle)
    line(bob, size, angle)
    line(bob, size, comp_angle)
    line(bob, size/2, 180)
    line(bob, size/3, angle)

def draw_b(bob, size):
    angle = 90
    line(bob, size, angle)
    rt(bob, 90)
    arc(bob, size/4, 180)
    rt(bob, 165)
    arc(bob, size/4, 180)

def draw_c(bob, size):
    size = size / 2
    lt(bob, 180)
    arc(bob, size, 180)

def draw_d(bob, size):
    angle = 90
    line(bob, size, angle)
    rt(bob, 90)
    arc(bob, size/2, 180)

def draw_o(bob, size):
    lt(bob, 180)
    arc(bob, size/2, 360)

def draw_p(bob, size):
    angle = 90
    line(bob, size, angle)
    rt(bob, 90)
    arc(bob, size/4, 180)

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

#draw_a(bob, 70)
#draw_b(bob, 70)
line(bob, 70, 0)
draw_o(bob, 70)

#bob.die();

#world.canvas.dump()

wait_for_user()
