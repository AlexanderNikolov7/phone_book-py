



def show_menu():
    menu = f'Меню:' \
        f'\n1, Добавить контакт' \
        f'\n2, Удалить контакт' \
        f'\n3, Найти контакт' \
        f'\n4, Показать все контакты' \
        f'\n5, Выйти' \
        f'\n-->' 
    choice = input(menu)
    return choice