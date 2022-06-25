n = int(input())
#44/100
matrix = []

current_row = 0
current_col = 0
count_tea = 0

for row in range(n):
    row_elements = input().split()
    for col in range(n):
        if row_elements[col] == 'A':
            current_row = row
            current_col = col
    matrix.append(row_elements)

while True:
    command = input()

    if command == 'up':
        if current_row <= 0:
            break
        if matrix[current_row - 1][current_col] == 'R':
            matrix[current_row - 1][current_col] = '*'
            break
        if matrix[current_row - 1][current_col] in '.*':
            matrix[current_row][current_col] = '*'
            matrix[current_row - 1][current_col] = '*'
            current_row -= 1
        else:
            count_tea += int(matrix[current_row - 1][current_col])
            matrix[current_row][current_col] = '*'
            matrix[current_row - 1][current_col] = '*'
            current_row -= 1

    elif command == 'down':
        if current_row >= n - 1:
            break
        if matrix[current_row + 1][current_col] == 'R':
            matrix[current_row + 1][current_col] = '*'
            break
        if matrix[current_row + 1][current_col] in '.*':
            matrix[current_row][current_col] = '*'
            matrix[current_row + 1][current_col] = '*'
            current_row += 1
        else:
            count_tea += int(matrix[current_row + 1][current_col])
            matrix[current_row][current_col] = '*'
            matrix[current_row + 1][current_col] = '*'
            current_row += 1

    elif command == 'right':
        if current_col >= n - 1:
            break
        if matrix[current_row][current_col + 1] == 'R':
            matrix[current_row][current_col + 1] = '*'
            break
        if matrix[current_row][current_col + 1] in '.*':
            matrix[current_row][current_col] = '*'
            matrix[current_row][current_col + 1] = '*'
            current_col += 1
        else:
            count_tea += int(matrix[current_row][current_col + 1])
            matrix[current_row][current_col] = '*'
            matrix[current_row][current_col + 1] = '*'
            current_col += 1

    elif command == 'left':
        if current_col <= 0:
            break
        if matrix[current_row][current_col - 1] == 'R':
            matrix[current_row][current_col - 1] = '*'
            break
        if matrix[current_row][current_col - 1] in '.*':
            matrix[current_row][current_col] = '*'
            matrix[current_row][current_col - 1] = '*'
            current_col -= 1
        else:
            count_tea += int(matrix[current_row][current_col - 1])
            matrix[current_row][current_col] = '*'
            matrix[current_row][current_col - 1] = '*'
            current_col -= 1

    if count_tea >= 10:
        break
if count_tea >= 10:
    print('She did it! She went to the party.')
else:
    print("Alice didn't make it to the tea party.")

for line in matrix:
    print(' '.join(line))
