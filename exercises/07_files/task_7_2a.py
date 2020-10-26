# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "Current configuration"]

# Решение
from sys import argv

config = argv[1]

with open(config,'r') as f:
    for line in f:
        line = line.strip()
        NotInIgnore = True
        if not line.startswith('!'):
            for i in ignore:
                if i in line:
                    NotInIgnore = False
            if NotInIgnore == True:
                print(line)
