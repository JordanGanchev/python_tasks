# 76/100
def input_data():
    matrix = []
    for _ in range(6):
        matrix.append([x for x in input().split()])
    return matrix


def command():
    commands = input().split(', ')
    return commands


def search_symbol(field):
    for a in range(6):
        for b in range(6):
            if field[a][b] == 'E':
                return a, b


def check_resource_and_print(letter, row, col):
    if letter == 'M':
        return f'Metal deposit found at ({row}, {col})'
    elif letter == 'C':
        return f'Concrete deposit found at ({row}, {col})'
    elif letter == 'W':
        return f'Water deposit found at ({row}, {col})'
    elif letter == 'R':
        return f'Rover got broken at ({row}, {col})'


def move_symbol(field, a, b, command):
    number_symbol = []
    for com in command:
        if com == 'down':
            letter = field[a + 1][b]
            field[a][b] = '-'
            field[a + 1][b] = 'E'
            a = a + 1
            if a > 5:
                a = 0
            if letter in 'WCRM':
                print(check_resource_and_print(letter, a, b))
                number_symbol.append(letter)
                if letter == 'R':
                    break
        elif com == 'up':
            letter = field[a - 1][b]
            field[a][b] = '-'
            field[a - 1][b] = 'E'
            a = a - 1
            if a < 0:
                a = 5
            if letter in 'WCRM':
                print(check_resource_and_print(letter, a, b))
                number_symbol.append(letter)
                if letter == 'R':
                    break
        elif com == 'right':
            letter = field[a][b + 1]
            field[a][b] = '-'
            field[a][b + 1] = 'E'
            b = b + 1
            if b > 5:
                b = 0
            if letter in 'WCRM':
                print(check_resource_and_print(letter, a, b))
                number_symbol.append(letter)
                if letter == 'R':
                    break
        elif com == 'left':
            letter = field[a][b - 1]
            field[a][b] = '-'
            field[a][b - 1] = 'E'
            b = b - 1
            if b < 0:
                b = 5
            if letter in 'WCRM':
                print(check_resource_and_print(letter, a, b))
                number_symbol.append(letter)
                if letter == 'R':
                    break
    if 'M' in number_symbol and 'C' in number_symbol and 'W' in number_symbol:
        print('Area suitable to start the colony.')
    elif 'M' or 'C' or 'W' not in number_symbol:
        print('Area not suitable to start the colony.')


field = input_data()
command = command()
a, b = search_symbol(field)
move_symbol(field, a, b, command)
