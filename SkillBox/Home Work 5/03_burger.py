# -*- coding: utf-8 -*-

# Создать модуль my_burger. В нем определить функции добавления инградиентов:
#  - булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

# В этом модуле создать рецепт двойного чизбургера (https://goo.gl/zA3goZ)
# с помощью фукций из my_burger и вывести на консоль.

# Создать рецепт своего бургера, по вашему вкусу.
# Если не хватает инградиентов - создать соответствующие функции в модуле my_burger
from my_burger.bread import bread
from my_burger.cutlet import cutlet
from my_burger.cheese import cheese
from my_burger.tomato import tomato
from my_burger.cucumber import cucumber
from my_burger.mayonnaise import mayonnaise

print("Рецепт создания вкуснейшего бургера")
bread()
cutlet()
cheese()
tomato()
cucumber()
mayonnaise()

