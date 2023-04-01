from time import *
from character import *
from time import *


def greetings():
    sleep(2)
    print('-' * 80)
    print('Добро пожаловать в текстовое РПГ по мотивам фентези миров.')
    sleep(2)
    print('Данная игра находится в стадии разработки.')
    sleep(2)
    print('Проект является тестовой работой на языке python3.')
    sleep(2)
    print('Приятной игры.')




def start_intro():
    text_list = ["Добро пожаловать в проект. Данная игра является вымышленной. Персонажи вымышлены. Все сходства с реальными людьми случайны."]
    text_print = []
    for elements in text_list:
        for element in elements:
            elem = element.split()
            text_print.append(elem)
            sleep(0.1)
            print(text_print)


    #print("Добро пожаловать в проект. Данная игра является вымышленной. Персонажи вымышлены. Все сходства с реальными людьми случайны.")


