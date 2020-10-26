# -*- coding: utf-8 -*-
"""
Задание 7.2c

Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ignore = ["duplex", "alias", "Current configuration"]

# Решение
from sys import argv

config_in = argv[1]
config_out = argv[2]

with open(config_in,'r') as f, open(config_out, 'w') as out:
    for line in f:
        line = line.strip()
        NotInIgnore = True
        for i in ignore:
            if i in line:
                NotInIgnore = False
        if NotInIgnore == True:
            config_out.write(line + '\n')
