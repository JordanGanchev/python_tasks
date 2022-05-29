rows, cols =[int(x) for x in input().split()]

matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

while True:
    line = input()
    if line == 'END':
        break
    line_parts = line.split()

    if len(line_parts) != 5 or line_parts[0] != 'swap':
        print('Invalid input')
        continue

    row1, col1, row2, col2 = [int(x) for x in line_parts[1:]]
    