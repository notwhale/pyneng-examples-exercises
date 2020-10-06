#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 4.7

Преобразовать MAC-адрес в строке mac в двоичную строку такого вида:
'101010101010101010111011101110111100110011001100'

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

mac = "AAAA:BBBB:CCCC"

# Решение

print('mac = "AAAA:BBBB:CCCC"')
mac_hex = '0x'+''.join(mac.split(':'))
mac_bin = bin(int(mac_hex,16))[2:]
print('mac_bin = ' + mac_bin)
