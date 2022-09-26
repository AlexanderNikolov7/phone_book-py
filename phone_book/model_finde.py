
# word = '2'

def finde_contact():
    word = input('Введите имя человека номер которого нужно показать:')
    with open('file.txt') as f:  # Найти строку в файле по слову
        for line in f:
            if word in line:
                print(line)

# finde_contact()
