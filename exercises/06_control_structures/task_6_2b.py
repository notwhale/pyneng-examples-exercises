#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

# Решение

ip_valid = False
while not ip_valid:
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
else:
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
