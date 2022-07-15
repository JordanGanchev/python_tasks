def check_bombs(matrix, r, c):
    if matrix[r][c] == '*':
        return 'X'

    movies = [
        [r - 1, c],
        [r + 1, c],
        [r, c + 1],
        [r, c - 1],
        [r - 1, c - 1],
        [r + 1, c + 1],
        [r + 1, c - 1],
        [r - 1, c + 1]
    ]

    count = 0
    for r, c in movies:
        if r < 0 or r > len(matrix) - 1 or c < 0 or c > len(matrix) - 1:
            continue

        else:
            if matrix[r][c] == '*':
                count += 1
    return count


n = int(input())
number_bombs = int(input())

matrix = []

for _ in range(n):
    matrix.append(['.' for x in range(n)])

for _ in range(number_bombs):
    r, c = eval(input())
    matrix[r][c] = '*'

for r in range(n):
    for c in range(n):
        num = check_bombs(matrix, r, c)
        if num == "X":
            continue
        else:
            matrix[r][c] = num

for line in matrix:
    print(f"{' '.join(str(x) for x in line)}")