#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"


# Решение

print('ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"')

ospf_list = ospf_route.split()
ospf_template = '''
Prefix:                 {}
AD/Metric:              {}
Next-Hop:               {}
Last update:            {}
Outbound Interface:     {}
'''

print(ospf_template.format(ospf_list[0], ospf_list[1].strip('[]'), ospf_list[3].strip(','), ospf_list[4].strip(','), ospf_list[5]))
