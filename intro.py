from time import *

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


start_intro()