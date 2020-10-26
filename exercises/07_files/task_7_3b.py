#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

#Решение

vlan = input('Введите номер VLAN: ')
vlans = []
with open('CAM_table.txt','r') as f:
    for line in f:
        line = line.strip().split()
        if line and line[0].isdigit():
            vlans.append([int(line[0]),line[1:]])
    for v in sorted(vlans):
        if vlan.isdigit() and int(vlan) == v[0]:
            print('{:>4} {:>18} {:>8}'.format(v[0],v[1][0],v[1][2]))
