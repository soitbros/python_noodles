try:
    # see if Swampy is installed as a package
    from swampy.TurtleWorld import *
except ImportError:
    # otherwise see if the modules are on the PYTHONPATH
    from TurtleWorld import *


def koch(t, d):
    n = d / 3
    fd(t, n)
    lt(t, 60)
    fd(t, n)
    rt(t, 120)
    fd(t, n)
    lt(t, 60)
    fd(t, n)

def iteration_one(t, d):
    koch(t, d)
    lt(t, 60)
    koch(t, d)
    rt(t, 120)
    koch(t, d)
    lt(t, 60)
    koch(t, d)

def iteration_two(t, d):
    iteration_one(t, d)
    lt(t, 60)
    iteration_one(t, d)
    rt(t, 120)
    iteration_one(t, d)
    lt(t, 60)
    iteration_one(t, d)

def iteration_three(t, d):
    iteration_two(t, d)
    lt(t, 60)
    iteration_two(t, d)
    rt(t, 120)
    iteration_two(t, d)
    lt(t, 60)
    iteration_two(t, d)

def snowflake(t, d):
    iteration_three(t, d)
    rt(t, 120)
    iteration_three(t, d)
    rt(t, 120)
    iteration_three(t, d)

# create the world and bob
world = TurtleWorld()
bob = Turtle()
bob.delay = 0
snowflake(bob, 10)

bob.die()

wait_for_user()
