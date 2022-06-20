#91/100
def input_data():
    m, n = [int(x) for x in input().split(',')]
    count = 0
    matrix = []
    for _ in range(m):
        matrix.append([x for x in input().split()])
    for i in range(m):
        for j in range(n):
            if matrix[i][j] in 'DCG':
                count += 1
    return matrix, m, n, count


def search_position(field, m, n):
    for row in range(m):
        for col in range(n):
            if field[row][col] == 'Y':
                return field, row, col


def move_symbol(field, row, col, m, n, count):
    number = 0
    collected = {
        'D': 0,
        'G': 0,
        'C': 0
    }

    while True:

        input_data = input()

        if input_data == 'End':
            break
        command, num = input_data.split('-')
        value = int(num)

        if command == 'up':

            for _ in range(1, value + 1):
                if row == 0:
                    if field[row + (m - 1)][col] in 'DGC':
                        symbol = field[row + (m - 1)][col]
                        collected[symbol] += 1
                        number += 1
                        field[row][col] = 'x'
                        field[row + (m - 1)][col] = 'Y'
                        row = row + (m - 1)
                    else:
                        field[row][col] = 'x'
                        field[row - 1][col] = 'Y'
                        row = row - 1
                    if count == number:
                        return field, collected
                else:
                    if field[row - 1][col] in 'DGC':
                        symbol = field[row - 1][col]
                        collected[symbol] += 1
                        number += 1
                        field[row][col] = 'x'
                        field[row - 1][col] = 'Y'
                    else:
                        field[row][col] = 'x'
                        field[row - 1][col] = 'Y'
                        row = row - 1
                    if count == number:
                        return field, collected

        elif command == 'down':

            for _ in range(1, value + 1):

                if row == (m - 1):
                    if field[row - (m - 1)][col] in 'DGC':
                        symbol = field[row - (m - 1)][col]
                        collected[symbol] += 1
                        number += 1
                        field[row][col] = 'x'
                        field[row - (m - 1)][col] = 'Y'
                        row = row - (m - 1)
                    else:
                        field[row][col] = 'x'
                        field[row - (m - 1)][col] = 'Y'
                        row = row - (m - 1)
                    if count == number:
                        return field, collected
                else:
                    if field[row + 1][col] in 'DGC':
                        symbol = field[row + 1][col]
                        collected[symbol] += 1
                        number += 1
                        field[row][col] = 'x'
                        field[row + 1][col] = 'Y'
                        row = row + 1
                    else:
                        field[row][col] = 'x'
                        field[row + 1][col] = 'Y'
                        row = row + 1
                    if count == number:
                        return field, collected

        elif command == 'right':

            for _ in range(1, value + 1):
                if col == (n - 1):
                    if field[row][col - (n - 1)] in 'DGC':
                        symbol = field[row][col - (n - 1)]
                        collected[symbol] += 1
                        number += 1
                        field[row][col] = 'x'
                        field[row][col - (n - 1)] = 'Y'
                        col = col - (n - 1)
                    if count == number:
                        return field, collected

                    else:
                        field[row][col] = 'x'
                        field[row][col - (n - 1)] = 'Y'
                        col = col - (n - 1)
                    if count == number:
                        return field, collected
                else:
                    if field[row][col + 1] in 'DGC':
                        symbol = field[row][col + 1]
                        collected[symbol] += 1
                        number += 1
                        field[row][col] = 'x'
                        field[row][col + 1] = 'Y'
                        col = col + 1
                    else:
                        field[row][col] = 'x'
                        field[row][col + 1] = 'Y'
                        col = col + 1
                    if count == number:
                        return field, collected

        elif command == 'left':

            for _ in range(1, value + 1):
                if col == 0:
                    if field[row][col + (n - 1)] in 'DGC':
                        symbol = field[row][col + (n - 1)]
                        collected[symbol] += 1
                        number += 1
                        field[row][col] = 'x'
                        field[row][col + (n - 1)] = 'Y'
                        col = col + (n - 1)
                    else:
                        field[row][col] = 'x'
                        field[row][col + (n - 1)] = 'Y'
                        col = col + (n - 1)
                    if count == number:
                        return field, collected

                else:
                    if field[row][col - 1] in 'DGC':
                        symbol = field[row][col - 1]
                        collected[symbol] += 1
                        number += 1
                        field[row][col] = 'x'
                        field[row][col - 1] = 'Y'
                        col = col - 1
                    else:
                        field[row][col] = 'x'
                        field[row][col - 1] = 'Y'
                        col = col - 1
                    if count == number:
                        return field, collected
    return field, collected


def print_func(field, count):
    total_sum = 0
    matrix, collection = field
    for key, value in collection.items():
        total_sum += value
    if count == total_sum:
        print('Merry Christmas!')
    print("You've collected:")
    for key, value in collection.items():
        if key == 'D':
            word = 'Christmas decorations'
        elif key == 'G':
            word = 'Gifts'
        elif key == 'C':
            word = 'Cookies'
        print(f'- {value} {word}')

    for line in matrix:
        print(' '.join(line))


field, m, n, count = input_data()
field, row, col = search_position(field, m, n)
collection = move_symbol(field, row, col, m, n, count)
print_func(collection, count)
