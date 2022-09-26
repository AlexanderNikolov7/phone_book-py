

def add_contact():
    str = input('Введите имя и номер телефона:')
    with open('file.txt', 'a') as data:  # записывает в файл в новую строку данные
        data.write(f'{str}\n')

# add_contact()        