import math


def Area(shape, base=0, width=0, height=0, radius=0):
    # shape: t=triangle, r=rectangle, c=circle
    if shape == "T":
        area = base * height / 2
    elif shape == "R":
        area = width * height
    else:
        area = (radius ** 2) * math.pi
    return area
