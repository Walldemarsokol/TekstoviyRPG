import random

def human_race():
    human = 'Human'
    return human

def orc_race():
    orc = 'Orc'
    return orc

def elf_race():
    elf = 'elf'
    return elf

def dwarf_race():
    dwarf = 'Dwarf'
    return dwarf

def random_race(): # рандомный выбор рассы
    rand = random.randint(1,4)
    if rand == 1:
        print('-'*80)
        print('<Вам досталась расса человек>')
        print('-' * 80)
        return human_race()
    elif rand == 2:
        print('-' * 80)
        print('<Вам досталась расса эльф>')
        print('-' * 80)
        return elf_race()
    elif rand == 3:
        print('-' * 80)
        print('<Вам досталась расса орк>')
        print('-' * 80)
        return orc_race()
    else:
        print('-' * 80)
        print('<Вам досталась расса гном>')
        print('-' * 80)
        return dwarf_race()