import simple_draw as sd
from random import randint

def creating_snowflake(quantity):
    """Создаем N снежинок"""
    snowflakes = [[i * 36, randint(540, 600), randint(2, 5)] for i in range(20)]



def decorate_snowflake(color):
    """Нарисовать снежинку цветом color"""
    sd.snowflake(center=point_0, length=30, color=color)
    point_0 = sd.get_point(snow_item[0], snow_item[1])

def move_the_snowflake():
    """Сдвинуть снежинку на один шаг"""
    for snow_item in snowflakes:
        snow_item[1] = snow_item[1] - snow_item[2]
        point_0 = sd.get_point(snow_item[0], snow_item[1])


def screen_bottom_number():
    """Выдает список номеров снежинок, которые вышли за границу экрана"""
    pass


def delete_snowflake(number):
    """Удаляет снежинки с номерами из списка"""
    pass