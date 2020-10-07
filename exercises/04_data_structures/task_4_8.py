#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 4.8

Преобразовать IP-адрес в двоичный формат и вывести на стандартный поток вывода вывод столбцами, таким образом:
- первой строкой должны идти десятичные значения байтов
- второй строкой двоичные значения

Вывод должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов

Пример вывода для адреса 10.1.1.1:
10        1         1         1
00001010  00000001  00000001  00000001

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ip = "192.168.3.1"

# Решение

print('ip = ' + ip)

ip_oct1 = int(ip.split('.')[0])
ip_oct2 = int(ip.split('.')[1])
ip_oct3 = int(ip.split('.')[2])
ip_oct4 = int(ip.split('.')[3])

ip_template = '''
{0:<10} {1:<10} {2:<10} {3:<10}
{0:010b} {1:010b} {2:010b} {3:010b}
'''

print(ip_template.format(ip_oct1,ip_oct2,ip_oct3,ip_oct4))
