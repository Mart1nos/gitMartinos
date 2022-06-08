x = 50

def func():
    global x

    print('x равно', x)
    x = 2
    print('заменяем глобальное значение x на', x)

func()
print('Значение х состовляет', x)