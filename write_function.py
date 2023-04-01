


def write_weapon(char_class):
    weapon = ''
    if char_class == 'warrior':
        weapon = 'Меч'
    elif char_class == 'mage':
        weapon = 'Палочка мага'
    elif char_class == 'rouge':
        weapon = 'Кинжал'
    else:
        weapon = 'Жезл'

    with open('weapon.txt','w',encoding= 'utf8') as text_weapon:
        text_weapon.write(weapon)