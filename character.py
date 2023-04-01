from race import *
from classes import *


def create_race(data):
    if data == "Human":
        print('человека')
        return human_race()
    elif data == "Elf":
        print('эльфа')
        return elf_race()
    elif data == "Orc":
        print('орка')
        return orc_race()
    elif data == "Dwarf":
        print('гнома')
        return dwarf_race()
    else:
        return random_race()




