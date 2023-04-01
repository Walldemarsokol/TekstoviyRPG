

def path_on_road(data):
    if data =='8':
        return walk_up()
    elif data == '4':
        return walk_left()
    elif data == '2':
        return walk_down()
    elif data == '6':
        return walk_right()
    else:
        new_data = input('Пожалуйста,выберите действие: ')
        return path_on_road(new_data)


def walk_up():
    return 1

def walk_down():
    return 1

def walk_left():
    return 1

def walk_right():
    return 1