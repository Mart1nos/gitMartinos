# -*- coding: utf-8 -*-
import simple_draw as sd

sd.resolution = (1200, 600)

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg


def triangle(point, length, colors, angle=0):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw(color=colors)

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=length, width=3)
    v2.draw(color=colors)

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=length, width=3)
    v3.draw(color=colors)


angle = 30
point = sd.get_point(100, 100)
triangle(point=point, angle=angle, length=150, colors=colors)



def square(point, length, colors, angle=0):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw(color=colors)

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 90, length=length, width=3)
    v2.draw(dcolor=colors)

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 180, length=length, width=3)
    v3.draw(color=colors)

    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 270, length=length, width=3)
    v4.draw(color=colors)


angle = 30
point_0 = sd.get_point(500, 100)
square(point=point_0, angle=angle, length=150, colors=colors)



def pentagon(point, length, colors, angle=0):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw(color=colors)

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 70, length=length, width=3)
    v2.draw(color=colors)

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 145, length=length, width=3)
    v3.draw(color=colors)

    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 215, length=length, width=3)
    v4.draw(color=colors)

    v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 290, length=length, width=3)
    v5.draw(color=colors)


angle = 30
point_1 = sd.get_point(150, 300)
pentagon(point=point_1, angle=angle, length=100, colors=colors)



def hexagon(point, length, colors, angle=0):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw(color=colors)

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 60, length=length, width=3)
    v2.draw(color=colors)

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 120, length=length, width=3)
    v3.draw(color=colors)

    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 180, length=length, width=3)
    v4.draw(color=colors)

    v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 240, length=length, width=3)
    v5.draw(color=colors)

    v6 = sd.get_vector(start_point=v5.end_point, angle=angle + 300, length=length, width=3)
    v6.draw(color=colors)


angle = 30
point_2 = sd.get_point(600, 350)
hexagon(point=point_2, angle=angle, length=100, colors=colors)

colors = {'1': {'Название цвета': 'Красный', 'Цвет': sd.COLOR_RED},
          '2': {'Название цвета': 'Оранжевый', 'Цвет': sd.COLOR_ORANGE},
          '3': {'Название цвета': 'Жёлтый', 'Цвет': sd.COLOR_YELLOW},
          '4': {'Название цвета': 'Зелёный', 'Цвет': sd.COLOR_GREEN},
          '5': {'Название цвета': 'Циан', 'Цвет': sd.COLOR_CYAN},
          '6': {'Название цвета': 'Синий', 'Цвет': sd.COLOR_BLUE},
          '7': {'Название цвета': 'Фиолетовый', 'Цвет': sd.COLOR_PURPLE}}

for number, color in colors.items():
    print(number, ' - ', color['Название цвета'])

x = input("Введите свой номер: ")

if x in colors:
    triangle(colors[x]['Цвет'], point)
    square(colors[x]['Цвет'], point_0)
    pentagon(colors[x]['Цвет'], point_1)
    hexagon(colors[x]['Цвет'], point_2)
else:
    print('Вы ввели неправильное значение. Повторите попытку!')





sd.pause()
