from load_game import load_game
from new_game import new_game




def main_menu():
    print('-' * 100)
    print('You are in main menu')
    print('-' * 100)
    data = input('Выберите действие: ')
    if data == "new":
        return new_game()
    elif data == "load":
        return load_game()
