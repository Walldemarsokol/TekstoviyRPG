from load_game import load_game
from new_game import new_game


def main_menu(data):
    if data == "new":
        return new_game()
    elif data == "load":
        return load_game()
