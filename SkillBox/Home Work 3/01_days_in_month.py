# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом

user_input = int(input("Введите, пожалуйста, номер месяца: "))
#    '1': 31,
#    '2': 28,
#    '3': 31,
#    '4': 30,
#    '5': 31,
#    '6': 30,
#    '7': 31,
#    '8': 31,
#    '9': 30,
#    '10': 31,
#    '11': 30,
#    '12': 31
if user_input == 1 or user_input == 3:
    print('31')
elif user_input == 5 or user_input == 7:
    print('31')
elif user_input == 8 or user_input == 10:
    print('31')
elif user_input == 12:
    print("31")
elif user_input == 4 or user_input == 6:
    print("30")
elif user_input == 9 or user_input == 11:
    print("30")
elif user_input == 2:
    print("28")
else:
    print('Номер месяца введен не прапильно, попробуйте другое!')



