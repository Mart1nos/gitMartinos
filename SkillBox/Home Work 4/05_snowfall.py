# -*- coding: utf-8 -*-
from random import randint

import simple_draw as sd
sd.resolution = (1200, 600)

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

snowflakes = [[i*36, randint(540,600), randint(2,5)] for i in range(20) ]
# snowflakes списко из снежинок. Снежинка тоже список, где первый индекс х, второй y, а третий скорость падения.
while True:
    sd.clear_screen()
    for snow_item in snowflakes:
        snow_item[1] = snow_item[1] - snow_item[2]
        point_0=sd.get_point(snow_item[0], snow_item[1])
        sd.snowflake(center=point_0, length=30, color=sd.COLOR_WHITE)
        if snow_item[1] < 30:
            break
        snow_item[0] = snow_item[0] + 5
    sd.sleep(0.05)
    if sd.user_want_exit():
        break

sd.pause()
# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg


