# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1200, 600)
point = sd.get_point(500, 500)
radius = 50

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей

for _ in range(3):
    radius += 5
    sd.circle(center_position=point, radius=radius, width=1)

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг

def bubble(point, step):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, width=1)

point = sd.get_point(300, 500)
bubble(point=point, step=10)

# Нарисовать 10 пузырьков в ряд

for x in range(100, 1000, 90):
    radius2 = 45
    point2 = sd.get_point(x, 100)
    sd.circle(center_position=point2, radius=radius2, width=1)


# Нарисовать три ряда по 10 пузырьков

for x in range(100, 1000, 90):
    for y in range(100, 301, 90):
        point3 = sd.get_point(x, y)
        sd.circle(center_position=point3, radius=radius2, width=1)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами

for _ in range(100):
    point4 = sd.random_point()
    step2 = random.randint(15, 45)
    sd.circle(center_position=point4, radius=step2, width=1)


sd.pause()


