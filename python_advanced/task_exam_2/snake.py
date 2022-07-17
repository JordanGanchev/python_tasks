def check_movie(matrix, command, r, c, b):
    movie = {
        'up': [r - 1, c],
        'down': [r + 1, c],
        'left': [r, c - 1],
        'right': [r, c + 1]
    }

    count = 0
    condition = False
    if b:
        [a, b], [d, f] = b
    for key, value in movie.items():
        r, c = value
        if command == key:
            if r < 0 or r > len(matrix) - 1 or c < 0 or c > len(matrix) - 1:
                condition = True
                return matrix, r, c, count, condition

            if matrix[r][c] == '*':
                count += 1
                matrix[r][c] = '.'
                return matrix, r, c, count, condition

            if matrix[r][c] == '-':
                matrix[r][c] = '.'
                return matrix, r, c, count, condition

            if matrix[r][c] == 'B':
                if [a, b] == [r, c]:
                    matrix[r][c] = '.'
                    r, c = d, f
                    matrix[r][c] = '.'
                    return matrix, r, c, count, condition
                elif [d, f] == [r, c]:
                    matrix[r][c] = '.'
                    r, c = a, b
                    matrix[r][c] = '.'
                    return matrix, r, c, count, condition


n = int(input())

matrix = []
r = 0
c = 0
b = []
count_number = 0
condition = False
food_eaten = 0
for line in range(n):
    matrix.append([x for x in input()])

for row in range(n):
    for col in range(n):
        if matrix[row][col] == 'S':
            r = row
            c = col
            matrix[r][c] = '.'
        if matrix[row][col] == 'B':
            b.append([row, col])

while True:
    command = input()

    if command == 'up':
        matrix, r, c, count, condition = check_movie(matrix, command, r, c, b)
        count_number += count

    if command == 'down':
        matrix, r, c, count, condition = check_movie(matrix, command, r, c, b)
        count_number += count

    if command == 'left':
        matrix, r, c, count, condition = check_movie(matrix, command, r, c, b)
        count_number += count

    if command == 'right':
        matrix, r, c, count, condition = check_movie(matrix, command, r, c, b)
        count_number += count

    if condition:
        break
    if count_number >= 10:
        matrix[r][c] = 'S'
        break

if condition:
    print('Game over!')
else:
    print('You won! You fed the snake.')
print(f'Food eaten: {count_number}')

for line in matrix:
    print(''.join([x for x in line]))