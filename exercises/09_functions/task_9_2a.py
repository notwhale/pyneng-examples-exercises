# -*- coding: utf-8 -*-
"""
Задание 9.2a

Сделать копию функции generate_trunk_config из задания 9.2

Изменить функцию таким образом, чтобы она возвращала не список команд, а словарь:
    - ключи: имена интерфейсов, вида 'FastEthernet0/1'
    - значения: список команд, который надо выполнить на этом интерфейсе

Проверить работу функции на примере словаря trunk_config и шаблона trunk_mode_template.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""


trunk_mode_template = [
    "switchport mode trunk",
    "switchport trunk native vlan 999",
    "switchport trunk allowed vlan",
]

trunk_config = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17],
}

# Решение

def generate_trunk_config(intf_vlan_mapping, trunk_template):
    """
    trunk port config dict generator
    intf_vlan_mapping
    trunk_template
    """
    trunk_config= {}
    for intf, vlans in intf_vlan_mapping.items():
        trunk_config[intf] = {}
        command_list = []
        for command in trunk_template:
            if command.endswith('vlan'):
                vlan_str = []
                for vlan in vlans: vlan_str.append(str(vlan))
                command_list.append(f"{command} {','.join(vlan_str)}")
            else:
                command_list.append(f"{command}")
        trunk_config[intf] = command_list
    return trunk_config

print('\n' + '-[ trunk_config_dict ]-' + '-' * 50 + '\n')

test = generate_trunk_config(trunk_config, trunk_mode_template)
for line in test.items():
    print(line)
