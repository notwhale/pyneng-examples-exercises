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

ip_valid = False
ip_addr = input('Введите IP-адрес: ')
ip = ip_addr.split('.')
if len(ip) == 4:
    for octet in ip:
        if octet.isdigit():
            octet = int(octet)
            if 0 <= octet <= 255:
                ip_valid = True
            else:
                ip_valid = False
                print('Неправильный IP-адрес')
                break
        else:
            ip_valid = False
            print('Неправильный IP-адрес')
            break
else:
    print('Неправильный IP-адрес')

if ip_valid:
    ip_oct1 = int(ip[0])
    if 1 <= ip_oct1 <= 223:
        print('unicast')
    elif 224 <= ip_oct1 <= 239:
        print('multicast')
    elif ip_addr == '255.255.255.255':
        print('local broadcast')
    elif ip_addr == '0.0.0.0':
        print('unassigned')
    else:
        print('unused')
