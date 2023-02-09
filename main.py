import random
# import abc
# import numpy


import simple_draw as sd

sd.resolution = (600, 600)


def bubble(point, step):
    radius = 50
    for _ in range(3):
        sd.circle(point, radius, width=3)
        assert isinstance(step, object)
        radius += step


for _ in range(100):
    point = sd.random_point()
    step = random.randint(3, 10)
    bubble(point, step)

sd.pause()
