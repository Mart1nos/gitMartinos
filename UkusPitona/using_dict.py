# 'ab' - сокращение от 'a'ddress'b'ook

ab = {  'Swaroop'   : 'swaroop@swaroopch.com',
        'larry'     : 'larry@wall.org',
        'Matsumoto' : 'matz@ruby-lang.org',
        'Spammer'   : 'spammer@hotmail.com'
        }

print("Адресс Swaroop'а:", ab['Swaroop'])

# Удаление пары ключ-значение
del ab['Spammer']

print('\nВ адресной книге {0} контакта\n'.format(len(ab)))

for name, addres in ab.items():
        print('Контакт {0} с адресом {1}'.format(name, addres))

# Добавление пары ключ-значени
ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
        print("\nАдрес Guido:", ab['Guido'])