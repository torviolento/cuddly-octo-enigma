import random


def distance(x1, y1, x2, y2):
    dx = abs(x2-x1)
    dy = abs(y2-y1)
    return (dx+dy+max(dx,dy))/2


def roll(a, b, c=0):
    # Roll AdB+C
    return sum(random.randrange(1, b+1) for i in range(a))+c


def describe_roll(a, b, c):
    return "{:}d{:}+{:}".format(a, b, c)


def random_by_level(level, items):
    pass


# def in_map(x, y):
#     return 0 <= x < map_height and 0 <= y < map_width
