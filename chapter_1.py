from time import sleep
from character import *
from classes import *
from game_over import game_over_loose
from write_function import *
from random_func import *

def choise_race():
    print(">Выберите рассу:\n"
          "нажмите 1 (человек)\n"
          "нажмите 2 (эльф)\n"
          "нажмите 3 (орк)\n"
          "нажмите 4 (гном)\n"
          "нажмите любую клавишу, если неважно (random)")
    data = input('enter: ')
    if data == "1":
        print('-' * 80)
        print('В отражении вы видите лицо человека.')
        print('-' * 80)
        return human_race()
    elif data == "2":
        print('-' * 80)
        print('В отражении вы видите лицо эльфа.')
        print('-' * 80)
        return elf_race()
    elif data == "3":
        print('-' * 80)
        print('В отражении вы видите лицо орка.')
        print('-' * 80)
        return orc_race()
    elif data == "4":
        print('-' * 80)
        print('В отражении вы видите лицо гнома.')
        print('-' * 80)
        return dwarf_race()
    else:
        print('-' * 80)
        print('Я не могу разобрать отражения...')
        return random_race()


def class_choise():  # метод выбор класса
    print(">Выберите класс:\n"
          "нажмите 1 (воин)\n"
          "нажмите 2 (маг)\n"
          "нажмите 3 (разбойник)\n"
          "нажмите 4 (клирик)\n"
          "нажмите любую клавишу, если неважно (random)")
    data = input('enter: ')
    if data == '1':
        print('-' * 80)
        print('Вы выбрали класс воин!')
        print('-' * 80)
        return warrior()
    elif data == '2':
        print('-' * 80)
        print('Вы выбрали класс маг!')
        print('-' * 80)
        return mage()
    elif data == '3':
        print('-' * 80)
        print('Вы выбрали класс разбойник!')
        print('-' * 80)
        return rouge()
    elif data == '4':
        print('-' * 80)
        print('Вы выбрали класс клирик!')
        print('-' * 80)
        return cleric()
    else:
        return random_class()


def choise_1(list): # начальное действие в пещере
    print('-'*80)
    print('Выберите действие:\n'
          '>вернуться назад к месту пробуждения (1)\n'
          '>пройти туда,откуда дует ветер (2)\n'
          '>подождать немного любуясь светом с потолка пещеры (3)')
    print()
    data = input('enter number: ')
    if data == "1":
        print('-'*80)
        print("Вы вернулись к месту, где вы очнулись.\n"
              "В темноте трудно что-то обнаружить без факела.\n"
              "Но вы все таки попытались проверить на ощупь.\n"
              "Вам удалось обнаружить что-то...")
        sleep(3)
        write_weapon(list)
        print('>Больше здесь делать нечего. Вы возвращаетесь к лучу света.')
        return choise_1(list)
    elif data == "2":
        print('>Вы медленно в темноте продвигаетесь вдоль стены пещеры.\n'
              '>Ваши глаза привыкли к темноте и уже легче воспринимать окружение.\n'
              '>Спустя пару минут Вы ощущаете свежий воздух и даже видно на повороте свет!\n'
              '>Вы очутились на выходе. Поздравляю!')
        return location_forest()
    elif data == "3":
        print('>Вы смотрите на свет исходящий с потолка пещеры. Он чарует и завораживает Вас.\n'
              '>Задумавшись Вы не заметили как к Вам подкрался пещерный паук...Вы не были готовы к такому.\n'
              '>Вас убили. Сожрали заживо.')
        sleep(3)
        print('>Задумавшись Вы не заметили как к Вам подкрался огромный пещерный паук...Вы не были готовы к такому.')
        sleep(4)
        print('>Вас убили. Сожрали заживо.')
        print()
        game_over_loose()
        sleep(5)
        return



def choise_2():
    print('-'*80)
    print('Выберите действие:\n'
          '>отправиться по следу на юг в лес(1)\n'
          '>направиться на запад в сторону дыма (2)\n'
          '>(не реализовано)двинуться на восток повинуясь жажде(3)\n'
          '>(не реализовано)(удача 6 или больше) осмотреться еще раз(4)\n'
          '>(не реализовано) пусть монетка решит мой путь.(рандом) (любая клавиша)\n')
    data = input('enter number: ')
    if data == '1':
        return 1
    elif data == '2':
        return 2
    elif data == '3':
        return 3
    elif data == '4':
        return 4
    else:
        return 5



def location_cave():

    # print('-' * 80)
    # print(
    #     '>Вы просыпаетесь с головной болью.\n'
    #     '>Одежда сырая. Ощущается холодный сквозняк, но он тихий и его не слышно.\n'
    #     '>Похоже,что Вы очнулись в пещере.')
    # sleep(4)
    # print('>Вы трогаете затылок: он мокрый и липкий. Похоже на кровь, но в темноте не понять.')
    # sleep(3)
    # print('>Вы пытаетесь подняться.')
    # sleep(2)
    # print('>Вам удается подняться и Вы оглядываетесь по сторонам.\n>Увидев луч света с потолка вы неспеша идете к нему.')
    # sleep(3)
    # print('>Добравшись до светлой части пещеры вы на полу находите лужу.\n>Вы пытаетесь наклониться к ней.')
    # sleep(3)
    # print('>В луже Вы можете увидеть свое отражение.')
    player_race = choise_race() # выбор рассы
    sleep(2)
    print('>Кажется вы понимаете,что на вас надето. Судя по экипировке Вы...')
    player_class = class_choise()# выбор класса
    sleep(2)
    create_char_string(player_class,player_race)
    print('>Однако оружия у вас не найдено...')
    sleep(3)
    print('>Наверное его потеряли при нападении...или что это было. Не понятно...')
    sleep(4)
    print()
    print('>Вокруг темнота. Только луч света проникает откуда то сквозь толщу земли или скал.\n'
          '>Вас начал пронизывать холод. Нужно что нибудь делать, что бы не замернуть.\n'
          '>Из-за яркого луча света глаза отвыкли от темноты.\n'
          'Вы вернулись в темноту,что бы глаза снова смогли видеть в пещере.')
    sleep(5)
    print(">В одном из направлений Вам кажется,что холод сильнее.\n"
          "Видимо сквозняк доносится оттуда.")
    choise_1(player_class)

def location_forest():
    print('-'*80)
    print('-'*30 + 'Глава I' + '-'*30)
    print('>На улице яркий свет. Слышно пение птиц и шелеств листвы на деревьях.')
    sleep(3)
    print('>Вы ощущаете жажду и голод. Вокруг Вас густой и зеленый лес')
    sleep(3)
    print('>Осмотревшись Вы обнаружили следы на мокрой земле вокруг пещеры. Они вели на юг в лес. ')
    sleep(3)
    print('>На западе в небе виден густой столб дыма. Кажется он далеко. Оттуда доносятся голоса.')
    sleep(3)
    print('>С востока дует ветер. Он принес влажный воздух. Похоже там находится река или озеро.')
    choise_2()
