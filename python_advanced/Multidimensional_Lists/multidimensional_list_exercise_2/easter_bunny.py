import sys
from io import StringIO
#50/100

def input_data():
    n = int(input())

    matrix = []

    for line in range(n):
        matrix.append(
            [x for x in input().split()]
        )
    for row in range(n):
        for col in range(n):
            if matrix[row][col] == 'B':
                return matrix, row, col, n


def move_in_matrix(field, row, col, n):
    def up(field, row, col, n):
        direction_up = {'up': []}
        count_up = 0
        while True:
            if 0 < row < n - 1 and field[row - 1][col] != 'X':
                direction_up['up'] += [[row - 1, col]]
                count_up += int(field[row - 1][col])
                row = row - 1
            else:
                return direction_up, count_up

    def down(field, row , col, n):
        direction_down = {'down': []}
        count_down = 0
        while True:
            if 0 < row < n - 1 and field[row + 1][col] != 'X':
                direction_down['down'] += [[row + 1, col]]
                count_down += int(field[row + 1][col])
                row = row + 1
            else:
                return direction_down, count_down

    def right(field, row, col, n):
        direction_right = {'right': []}
        count_right = 0
        while True:
            if 0 <= col < n - 1 and field[row][col + 1] != 'X':
                direction_right['right'] += [[row, col + 1]]
                count_right += int(field[row][col + 1])
                col = col + 1
            else:
                return direction_right, count_right

    def left(field, row, col, n):
        direction_left = {'left': []}
        count_left = 0
        while True:
            if 0 < col < n - 1 and field[row][col - 1] != 'X':
                direction_left['left'] += [[row, col - 1]]
                count_left += int(field[row][col - 1])
                col = col - 1
            else:
                return direction_left, count_left
    result_up, count_up = up(field, row, col, n)
    result_down, count_down = down(field, row, col, n)
    result_right, count_right = right(field, row, col, n)
    result_left, count_left = left(field, row, col, n)
    sun_count = max(count_left, count_right, count_down, count_up)
    if sun_count == count_up:
        return result_up, count_up
    elif sun_count == count_down:
        return result_down, count_down
    elif sun_count == count_right:
        return result_right, count_right
    elif sun_count == count_left:
        return  result_left, count_left


test_input1 = '''5
1 3 7 9 11
X 5 4 X 63
7 3 21 95 1
B 1 73 4 9
9 2 33 2 0
'''
test_input2 = '''8
4 18 9 7 24 41 52 11
54 21 19 X 6 34 75 57
76 67 7 44 76 27 56 37
92 35 25 37 52 34 56 72
35 X 1 45 4 X 37 63
105 X B 2 12 43 5 19
48 19 35 20 32 27 42 4
73 88 78 32 37 52 X 22
'''
#sys.stdin = StringIO(test_input1)
#sys.stdin = StringIO(test_input2)


field, row, col, n = input_data()
my_dict, count = move_in_matrix(field, row, col, n)
for key, value in my_dict.items():
    print(key)
    for num in value:
        print(num)
print(count)
