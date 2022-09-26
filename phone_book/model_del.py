

import re

def del_contact():
    with open('file.txt') as f:      # удалит строку с указаннм словом
        lines = f.readlines()

    str = input('Ведите имя человека номер которого нужно удалить:')
    pattern = re.compile(re.escape(str))
    with open('file.txt', 'w') as f:
        for line in lines:
            result = pattern.search(line)
            if result is None:
                f.write(line)

# del_contact()
