# -*- coding: utf-8 -*-
"""
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "Current configuration"]

# Решение
from sys import argv

config = argv[1]

with open(config,'r') as f, open('config_sw1_cleared.txt', 'w') as out:
    for line in f:
        line = line.strip()
        NotInIgnore = True
        for i in ignore:
            if i in line:
                NotInIgnore = False
        if NotInIgnore == True:
            out.write(line + '\n')
