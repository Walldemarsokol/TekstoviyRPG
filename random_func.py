from classes import *
from random import randint


def random_choice(a, b):
    result = randint(a,b)
    return result


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
