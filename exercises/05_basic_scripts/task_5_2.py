#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

#Решение
ip_cidr = input('Введите адрес IP-сети (10.1.1.0/24): ')
ip_net = ip_cidr.split('/')[0]
ip_mask = ip_cidr.split('/')[1]

ip_net1 = int(ip_net.split('.')[0])
ip_net2 = int(ip_net.split('.')[1])
ip_net3 = int(ip_net.split('.')[2])
ip_net4 = int(ip_net.split('.')[3])

ip_maskbin = '1' * int(ip_mask) + '0' * (32-int(ip_mask))

ip_maskbin1 = ip_maskbin[:8]
ip_maskbin2 = ip_maskbin[8:16]
ip_maskbin3 = ip_maskbin[16:24]
ip_maskbin4 = ip_maskbin[24:]

ip_mask1 = int(ip_maskbin1,2)
ip_mask2 = int(ip_maskbin2,2)
ip_mask3 = int(ip_maskbin3,2)
ip_mask4 = int(ip_maskbin4,2)

ip_template = f'''
Network:
{ip_net1:<8} {ip_net2:<8} {ip_net3:<8} {ip_net4:<8}
{ip_net1:08b} {ip_net2:08b} {ip_net3:08b} {ip_net4:08b}

Mask:
/{ip_mask}
{ip_mask1:<8} {ip_mask2:<8} {ip_mask3:<8} {ip_mask4:<8}
{ip_maskbin1:8} {ip_maskbin2:8} {ip_maskbin3:8} {ip_maskbin4:8}
'''

print(ip_template)
