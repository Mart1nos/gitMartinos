def total(inicial=5, *numbers, extra_number):
    count = initial
    for number in numbers:
        count +=number
    count += extra_number
    print(count)

total(10, 1, 2, 3, extra_number=50)
total(10, 1, 2, 3)
# Вызовет ошибку, поскольку мы не указали значение
# аргумента по умолчанию для 'extra_number'.
#  вместо x = x + y просто написать x += y