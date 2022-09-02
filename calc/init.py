x = 0
y = 0
operation = ''

#  '12 - 3' -> ['12', '3', '-']

def init_data(exp):
    global x
    global y
    global operation
    options_operstion = ['-', '+', '*', '/']
    for letter in exp:
        if letter in options_operstion:
            exp = exp.split(letter)
            exp.append(letter)
            break
    x = int(exp[0])
    y = int(exp[1])
    operation = exp[2]


def set_data():
    global x
    global y
    global operation
    return x, y, operation

