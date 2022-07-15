def input_matrix():
    matrix = []
    for line in range(8):
        matrix.append([x for x in input().split()])
    return matrix


def check_symbol(matrix):
    for r in range(8):
        for c in range(8):
            if matrix[r][c] == 'K':
                return r, c


def up(r):
    return r - 1


def down(r):
    return r + 1


def right(c):
    return c + 1


def left(c):
    return c - 1


def up_right(r, c):
    return r - 1, c + 1


def down_right(r, c):
    return r + 1, c + 1


def up_left(r, c):
    return r - 1, c - 1


def down_left(r, c):
    return r + 1, c - 1


def check_movie(matrix, r, c):
    command_list = [
        'up',
        'down',
        'right',
        'left',
        'up_left',
        'up_right',
        'down_left',
        'down_right'
    ]

    list_out = []

    for command in command_list:
        if command == "up":
            r, c = check_symbol(matrix)
            if r == 0:
                continue
            while True:
                r = up(r)
                if matrix[r][c] == 'Q':
                    list_out.append([r, c])
                    break
                if r == 0:
                    break

        elif command == "down":
            r, c = check_symbol(matrix)
            if r == 7:
                continue
            while True:
                r = down(r)
                if matrix[r][c] == 'Q':
                    list_out.append([r, c])
                    break
                if r == 7:
                    break

        elif command == "right":
            r, c = check_symbol(matrix)
            if c == 7:
                continue
            while True:
                c = right(c)
                if matrix[r][c] == 'Q':
                    list_out.append([r, c])
                    break
                if c == 7:
                    break

        elif command == "left":
            r, c = check_symbol(matrix)
            if c == 0:
                continue
            while True:
                c = left(c)
                if matrix[r][c] == 'Q':
                    list_out.append([r, c])
                    break
                if c == 0:
                    break

        elif command == "up_left":
            r, c = check_symbol(matrix)
            if r == 0 or c == 0:
                continue
            while True:
                r, c = up_left(r, c)
                if matrix[r][c] == 'Q':
                    list_out.append([r, c])
                    break
                if c == 0 or r == 0:
                    break

        elif command == "up_right":
            r, c = check_symbol(matrix)
            if r == 0 or c == 7:
                continue
            while True:
                r, c = up_right(r, c)
                if matrix[r][c] == 'Q':
                    list_out.append([r, c])
                    break
                if r == 0 or c == 7:
                    break

        elif command == "down_left":
            r, c = check_symbol(matrix)
            if r == 7 or r == 0:
                continue
            while True:
                r, c = down_left(r, c)
                if matrix[r][c] == 'Q':
                    list_out.append([r, c])
                    break
                if c == 0 or r == 7:
                    break

        elif command == "down_right":
            r, c = check_symbol(matrix)
            if r == 7 or c == 7:
                continue
            while True:
                r, c = down_right(r, c)
                if matrix[r][c] == 'Q':
                    list_out.append([r, c])
                    break
                if c == 7 or r == 7:
                    break
    return list_out


matrix = input_matrix()
r, c = check_symbol(matrix)
result = check_movie(matrix, r, c)

if result:
    for coordinate in result:
        print(coordinate)
else:
    print('The king is safe!')