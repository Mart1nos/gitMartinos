# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

sd.resolution = (601, 601)

for y in range(0, 600, 100):
    x = 0
    for x in range(x, 600, 100):
        start_poin = sd.get_point(x, y)
        end_point = sd.get_point(x + 100, y + 50)
        sd.rectangle(start_poin, end_point, width=1)
for y in range(50, 600, 100):
    x = -50
    for x in range(x, 600, 100):
        start_poin = sd.get_point(x, y)
        end_point = sd.get_point(x + 100, y + 50)
        sd.rectangle(start_poin, end_point, width=1)
sd.pause()
