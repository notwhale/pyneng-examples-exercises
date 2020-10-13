#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 5.2a

Всё, как в задании 5.2, но, если пользователь ввел адрес хоста, а не адрес сети,
надо преобразовать адрес хоста в адрес сети и вывести адрес сети и маску, как в задании 5.2.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.195/28 - хост из сети 10.0.5.192/28

Если пользователь ввел адрес 10.0.1.1/24,
вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях хост/маска, например:
    10.0.5.195/28, 10.0.1.1/24

Подсказка:
Есть адрес хоста в двоичном формате и маска сети 28. Адрес сети это первые 28 бит адреса хоста + 4 ноля.
То есть, например, адрес хоста 10.1.1.195/28  в двоичном формате будет
bin_ip = "00001010000000010000000111000011"

А адрес сети будет первых 28 символов из bin_ip + 0000 (4 потому что всего в адресе может быть 32 бита, а 32 - 28 = 4)
00001010000000010000000111000000

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

#Решение

ip_cidr = input('Введите адрес IP-сети (10.1.1.0/24): ')
ip_addr = ip_cidr.split('/')[0]
ip_mask = ip_cidr.split('/')[1]

ip_addr1 = int(ip_addr.split('.')[0])
ip_addr2 = int(ip_addr.split('.')[1])
ip_addr3 = int(ip_addr.split('.')[2])
ip_addr4 = int(ip_addr.split('.')[3])

ip_addrbin1 = '0' * (8 - len(bin(ip_addr1)[2:])) + bin(ip_addr1)[2:]
ip_addrbin2 = '0' * (8 - len(bin(ip_addr2)[2:])) + bin(ip_addr2)[2:]
ip_addrbin3 = '0' * (8 - len(bin(ip_addr3)[2:])) + bin(ip_addr3)[2:]
ip_addrbin4 = '0' * (8 - len(bin(ip_addr4)[2:])) + bin(ip_addr4)[2:]

ip_addrbin = ip_addrbin1 + ip_addrbin2 + ip_addrbin3 + ip_addrbin4

ip_netbin = ip_addrbin[:int(ip_mask)] + '0' * (32 - int(ip_mask))

ip_netbin1 = ip_netbin[:8]
ip_netbin2 = ip_netbin[8:16]
ip_netbin3 = ip_netbin[16:24]
ip_netbin4 = ip_netbin[24:]

ip_net1 = int(ip_netbin1,2)
ip_net2 = int(ip_netbin2,2)
ip_net3 = int(ip_netbin3,2)
ip_net4 = int(ip_netbin4,2)

ip_maskbin = '1' * int(ip_mask) + '0' * (32 - int(ip_mask))

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
{ip_netbin1:<8} {ip_netbin2:<8} {ip_netbin3:<8} {ip_netbin4:<8}

Mask:
/{ip_mask}
{ip_mask1:<8} {ip_mask2:<8} {ip_mask3:<8} {ip_mask4:<8}
{ip_maskbin1:<8} {ip_maskbin2:<8} {ip_maskbin3:<8} {ip_maskbin4:<8}
'''

print(ip_template)
