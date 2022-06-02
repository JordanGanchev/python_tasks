import sys
from io import StringIO

test_input1 = '''3
1 2 3
4 5 6
7 8 9
Add 0 0 5
Subtract 1 1 2
END
'''
test_input2 = '''4
1 2 3 4
5 6 7 8
8 7 6 5
4 3 2 1
Add 4 4 100
Add 3 3 100
Subtract -1 -1 42
Subtract 0 0 42
END
'''
#sys.stdin = StringIO(test_input1)
#sys.stdin = StringIO(test_input2)
n = int(input())

matrix = []

for _ in range(n):
    matrix.append(
        [int(x) for x in input().split()]
    )
while True:
    second_line = input().split()
    if second_line[0] == 'END':
        break
    command = second_line[0]
    index_x = int(second_line[1])
    index_y = int(second_line[2])
    value = int(second_line[3])
    m = len(matrix) - 1
    if index_y < 0 or index_y > m or index_x < 0 or index_y > m:
        print("Invalid coordinates")
        continue
    if command == 'Add':
        matrix[index_x][index_y] += value

    if command == 'Subtract':
        matrix[index_x][index_y] -= value

for num in matrix:
    number = [str(x) for x in num]
    print(' '.join(number))