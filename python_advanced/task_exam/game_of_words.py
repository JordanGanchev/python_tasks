def negative_direction(command, r, c, n):
    if command == 'up' and r == 0:
        return True
    if command == 'down' and r == n - 1:
        return True
    if command == 'right' and c == n - 1:
        return True
    if command == 'left' and c == 0:
        return True


word = input()
n = int(input())

matrix = []
r = 0
c = 0
for _ in range(n):
    matrix.append([x for x in input()])

for row in range(n):
    for col in range(n):
        if matrix[row][col] == 'P':
            r = row
            c = col

number_of_direction = int(input())
for _ in range(number_of_direction):
    command = input()

    if negative_direction(command, r, c, n):
        if word:
           word = word[:-1]
        continue

    if command == 'up':
        if matrix[r - 1][c].isalpha():
            word += matrix[r - 1][c]
            matrix[r][c] = '-'
            matrix[r - 1][c] = 'P'
            r = r - 1
        else:
            matrix[r][c] = '-'
            matrix[r - 1][c] = 'P'
            r = r - 1

    elif command == 'down':
        if matrix[r + 1][c].isalpha():
            word += matrix[r + 1][c]
            matrix[r][c] = '-'
            matrix[r + 1][c] = 'P'
            r = r + 1
        else:
            matrix[r][c] = '-'
            matrix[r + 1][c] = 'P'
            r = r + 1

    elif command == 'right':
        if matrix[r][c + 1].isalpha():
            word += matrix[r][c + 1]
            matrix[r][c] = '-'
            matrix[r][c + 1] = 'P'
            c = c + 1
        else:
            matrix[r][c] = '-'
            matrix[r][c + 1] = 'P'
            c = c + 1

    elif command == 'left':
        if matrix[r][c - 1].isalpha():
            word += matrix[r][c - 1]
            matrix[r][c] = '-'
            matrix[r][c - 1] = 'P'
            c = c - 1
        else:
            matrix[r][c] = '-'
            matrix[r][c - 1] = 'P'
            c = c - 1

print(word)
for line in matrix:
    print(f"{''.join(line)}")
