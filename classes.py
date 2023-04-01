import random


def class_choise(data):  # метод выбор класса
    if data == 'warrior':
        return warrior()
    elif data == 'mage':
        return mage()
    elif data == 'rouge':
        return rouge()
    elif data == 'cleric':
        return cleric()
    else:
        return random_class()


def warrior():
    hp = 20  # множитель
    mp = 10  # множитель
    ap = 3  # множитель
    str = 10 # сила
    dex = 3 # ловкость
    endr = 5 #выносливость
    intel = 2 #интеллекс
    attack = 1 # множитель
    defence = 0.5 # множитель
    armor = 1
    status_list = ['warrior', hp * endr, mp * intel, ap * dex, str, dex, endr,
                   intel, attack * str,defence * endr + armor]  # class, HP,MP,AP strength,dexterity,endurance,intelligence
    return status_list


def mage():
    hp = 20  # множитель
    mp = 10  # множитель
    ap = 3  # множитель
    str = 10  # сила
    dex = 3  # ловкость
    endr = 5  # выносливость
    intel = 10  # интеллекс
    attack = 1 # множитель
    defence = 0.5 # множитель
    armor = 1
    status_list = ['mage', hp * endr, mp * intel, ap * dex, str, dex, endr,
                   intel,attack * str,defence * endr + armor]  # class, HP,MP,AP strength,dexterity,endurance,intelligence
    return status_list


def rouge():
    hp = 20  # множитель
    mp = 10  # множитель
    ap = 3  # множитель
    str = 3  # сила
    dex = 10  # ловкость
    endr = 3  # выносливость
    intel = 4  # интеллекс
    attack = 1 # множитель
    defence = 0.5 # множитель
    armor = 1
    status_list = ['rouge', hp * endr, mp * intel, ap * dex, str, dex, endr,
                   intel,attack * str,defence * endr + armor]  # class, HP,MP,AP strength,dexterity,endurance,intelligence
    return status_list


def cleric():
    hp = 20  # множитель
    mp = 10  # множитель
    ap = 3  # множитель
    str = 10  # сила
    dex = 3  # ловкость
    endr = 5  # выносливость
    intel = 2  # интеллекс
    status_list = ['warrior', hp * endr, mp * intel, ap * dex, str, dex, endr,
                   intel]  # class, HP,MP,AP strength,dexterity,endurance,intelligence
    return status_list


def random_class():  # создает рандомный класс
    rand = random.randint(1, 4)
    if rand == 1:
        print('-' * 80)
        print('<вам достался класс воин>')
        print('-' * 80)
        return warrior()
    elif rand == 2:
        print('-' * 80)
        print('<вам достался класс маг>')
        print('-' * 80)
        return mage()
    elif rand == 3:
        print('-' * 80)
        print('<вам достался класс разбойник>')
        print('-' * 80)
        return rouge()
    else:
        print('-' * 80)
        print('<вам достался класс клирик>')
        print('-' * 80)
        return cleric()
