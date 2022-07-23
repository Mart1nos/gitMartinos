from random import shuffle



def make_number():
    """Загадать число"""
    num = list('0123456789')
    shuffle(num)
    comparison = num[3:7] if num[3] != '0' else num[4:8]





def check_number(position):
    """Проверить число, возвращает словарь {'bulls': N, 'cows': N}"""
    pass
