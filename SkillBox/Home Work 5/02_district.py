# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

from district.central_street.house1.room1 import folks as csh1r1
from district.central_street.house1.room2 import folks as csh1r2
from district.central_street.house2.room1 import folks as csh2r1
from district.central_street.house2.room2 import folks as csh2r2
from district.soviet_street.house1.room1 import folks as ssh1r1
from district.soviet_street.house1.room2 import folks as ssh1r2
from district.soviet_street.house2.room1 import folks as ssh2r1
from district.soviet_street.house2.room2 import folks as ssh2r2


print("На районе живут:", ",".join(csh1r1),",", ",".join(csh1r1),",", ",".join(csh1r2),",", ",".join(csh2r1), ",".join(csh2r2),",", ",".join(ssh1r1),
      ",", ",".join(ssh1r2),",", ",".join(ssh2r1),",", ",".join(ssh2r2))

