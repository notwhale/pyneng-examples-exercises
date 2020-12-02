# -*- coding: utf-8 -*-
"""
Задание 9.1a

Сделать копию функции generate_access_config из задания 9.1.

Дополнить скрипт:
* ввести дополнительный параметр, который контролирует будет ли настроен port-security
 * имя параметра 'psecurity'
 * значение по умолчанию None
 * для настройки port-security, как значение надо передать список команд port-security (находятся в списке port_security_template)

Функция должна возвращать список всех портов в режиме access
с конфигурацией на основе шаблона access_mode_template и шаблона port_security_template, если он был передан.
В конце строк в списке не должно быть символа перевода строки.


Проверить работу функции на примере словаря access_config,
с генерацией конфигурации port-security и без.

Пример вызова функции:
print(generate_access_config(access_mode_template, access_config))
print(generate_access_config(access_mode_template, access_config, port_security_template))

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

access_mode_template = [
    "switchport mode access",
    "switchport access vlan",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

port_security_template = [
    "switchport port-security maximum 2",
    "switchport port-security violation restrict",
    "switchport port-security",
]

access_config = {"FastEthernet0/12": 10, "FastEthernet0/14": 11, "FastEthernet0/16": 17}

# Решение

def generate_access_config(intf_vlan_mapping, access_template, psecurity=None):
    """
    intf_vlan_mapping - словарь с соответствием интерфейс-VLAN такого вида:
        {'FastEthernet0/12':10,
         'FastEthernet0/14':11,
         'FastEthernet0/16':17}
    access_template - список команд для порта в режиме access

    Возвращает список всех портов в режиме access с конфигурацией на основе шаблона
    """
    config_list = []
    for intf, vlan in intf_vlan_mapping.items():
        config_list.append(f'interface {intf}')
        for command in access_template:
            if command.endswith('vlan'):
                config_list.append(f'{command} {vlan}')
            else:
                config_list.append(f'{command}')
        if psecurity:
            for command in psecurity:
                config_list.append(f'{command}')
    return config_list

print('\n' + '-[ access_config ]-' + '-' * 50 + '\n')

test1 = generate_access_config(access_config, access_mode_template)
for line in test1:
    print(line)

print('\n' + '-[ port_security_template ]-' + '-' * 50 + '\n')

test2 = generate_access_config(access_config, access_mode_template, psecurity=port_security_template)
for line in test2:
    print(line)
