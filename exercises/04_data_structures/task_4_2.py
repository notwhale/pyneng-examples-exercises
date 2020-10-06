#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 4.2

Преобразовать строку mac из формата XXXX:XXXX:XXXX в формат XXXX.XXXX.XXXX

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

mac = "AAAA:BBBB:CCCC"

#Решение 
print('mac = "AAAA:BBBB:CCCC"')
mac_replace = mac.replace(':','.')
print('mac_replace = ' + mac_replace)
