def hello_n(name:str, n:int): # Заголовок функции
    for i in range(n): # Тело функции (range - диапазон)
        print("Привет", name)

hello_n("Вася", 5)
hello_n("Петя", 3)