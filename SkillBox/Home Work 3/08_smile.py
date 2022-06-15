# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

sd.resolution = (700, 700)

def smile(x, y, color):
    start_point = sd.get_point(x, y)
    start_point_2 = sd.get_point(x-15, y+20)
    start_point_3 = sd.get_point(x+15, y+20)
    sd.circle(start_point, 50, color, width=4)
    sd.line(sd.get_point(x - 25, y - 5), sd.get_point(x - 10, y - 20), color, 2)
    sd.line(sd.get_point(x - 10, y - 20), sd.get_point(x + 10, y - 20), color, 2)
    sd.line(sd.get_point(x + 10, y - 20), sd.get_point(x + 24, y - 5), color, 2)
    sd.circle(start_point_2, 5, color, width=1)
    sd.circle(start_point_3, 5, color, width=1)


for i in range(10):
    point = sd.random_point()
    x = point.x
    y = point.y
    color = sd.random_color()
    smile(x, y, color)

sd.pause()
