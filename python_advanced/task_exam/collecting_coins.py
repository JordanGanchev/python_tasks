from math import floor
import sys
from io import StringIO



def matrix_created(n):
    matrix = []
    for row in range(n):
        matrix.append(input().split())
    return matrix


def search_symbol(matrix, n):
    for row in range(n):
        for col in range(n):
            if matrix[row][col] == 'P':
                return row, col


def reviev(matrix, r, c, n):
    count_coins = 0
    movies = []
    condition = False
    while True:
        movies.append([r, c])
        command = input()

        if command == 'left':
            if c == 0:
                if matrix[r][c + n - 1] not in 'X':
                    matrix[r][c] = '0'
                    c = n - 1
                    count_coins += int(matrix[r][c])
                    matrix[r][c] = '0'
                else:
                    c = c - 1
                    movies.append([r, c])
                    return count_coins, movies, condition

            elif matrix[r][c - 1] not in 'X':
                matrix[r][c] = '0'
                c = c - 1
                count_coins += int(matrix[r][c])
                matrix[r][c] = '0'
            else:
                c = c - 1
                movies.append([r, c])
                return count_coins, movies, condition

        elif command == 'right':
            if c == n - 1:
                if matrix[r][0] not in 'X':
                    matrix[r][c] = '0'
                    c = 0
                    count_coins += int(matrix[r][c])
                    matrix[r][c] = '0'
                else:
                    c = 0
                    movies.append([r, c])
                    return count_coins, movies, condition

            elif matrix[r][c + 1] not in 'X':
                    matrix[r][c] = '0'
                    c = c + 1
                    count_coins += int(matrix[r][c])
                    matrix[r][c] = '0'
            else:
                c = 0
                movies.append([r, c])
                return count_coins, movies, condition

        elif command == 'up':
            if r == 0:
                if matrix[r + n - 1][c] not in 'PX':
                    matrix[r][c] = '0'
                    r = n - 1
                    count_coins += int(matrix[r][c])
                    matrix[r][c] = '0'
                else:
                    c = n - 1
                    movies.append([r, c])
                    return count_coins, movies, condition
            elif matrix[r - 1][c] not in 'PX*':
                matrix[r][c] = '0'
                r = r - 1
                count_coins += int(matrix[r][c])
                matrix[r][c] = '0'
            else:
                c = n - 1
                movies.append([r, c])
                return count_coins, movies, condition
        elif command == 'down':
            if r == n - 1:
                if matrix[0][c] not in 'PX':
                    matrix[r][c] = '0'
                    r = 0
                    count_coins += int(matrix[r][c])
                    matrix[r][c] = '0'
                else:
                    r = 0
                    movies.append([r, c])
                    return count_coins, movies, condition

            elif matrix[r][c + 1] not in 'PX':
                matrix[r][c] = '0'
                r = r + 1
                count_coins += int(matrix[r][c])
                matrix[r][c] = '0'
            else:
                r = 0
                movies.append([r, c])
                return count_coins, movies, condition
        if count_coins >= 100:
            movies.append([r, c])
            condition = True
            return count_coins,movies, condition


test_input_1 = '''5
1 X 7 9 11
X 14 46 62 0
15 33 21 95 X
P 14 3 4 18
9 20 33 X 0
left
right
right
up
up
right
'''

test_input_2 = '''8
13 18 9 7 24 41 52 11
54 21 19 X 6 4 75 6
76 5 7 1 76 27 2 37
92 3 25 37 52 X 56 72
15 X 1 45 45 X 7 63
1 63 P 2 X 43 5 1
48 19 35 20 100 27 42 80
73 88 78 33 37 52 X 22
up
down
up
left
'''

# sys.stdin = StringIO(test_input_1)
# sys.stdin = StringIO(test_input_2)

n = int(input())
matrix = matrix_created(n)
r, c = search_symbol(matrix, n)
coins, movies, condition = reviev(matrix, r, c, n)

if condition:
    print(f"You won! You've collected {coins} coins.")
    print('Your path:')
else:
    coins = floor(coins / 2)
    print(f"Game over! You've collected {coins} coins.")
    print('Your path:')

for i in movies:
    print(i)