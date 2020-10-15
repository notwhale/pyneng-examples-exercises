#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

Сообщение должно выводиться только один раз.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

# Решение

ip_addr = input('Введите IP-адрес: ')

ip = ip_addr.split('.')

ip_valid = True

if len(ip) != 4:
    ip_valid = False
else:
    for i in ip:
        if not i.isdigit():
            ip_valid = False
        else:
            if int(i) < 0 or int(i) > 255:
                ip_valid = False

if not ip_valid:
    print('Неправильный IP-адрес')
else:
    ip_oct1 = int(ip[0])
    if 1 < ip_oct1 < 224:
        print('unicast')
    elif 223 < ip_oct1 < 240:
        print('multicast')
    elif ip_addr == '255.255.255.255':
        print('local broadcast')
    elif ip_addr == '0.0.0.0':
        print('unassigned')
    else:
        print('unused')
