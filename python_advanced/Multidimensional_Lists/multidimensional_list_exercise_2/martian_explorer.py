from collections import deque


def move(r, c, direction, size):
    if direction == 'up':
        current_row, current_col = r - 1, c
        if current_row < 0:
            return current_row + size, current_col
        return current_row, current_col

    elif direction == 'down':
        current_row, current_col = r + 1, c
        if current_row == size:
            return current_row - size, current_col
        return current_row, current_col
    elif direction == 'right':
        current_row, current_col = r, c + 1
        if current_col == size:
            return current_row, current_col - size
        return current_row, current_col
    elif direction == 'left':
        current_row, current_col = r, c - 1
        if current_col < 0:
            return current_row, current_col + size
        return current_row, current_col


size = 6

matrix = []
row_idx = 0
col_idx = 0
for row in range(size):
    row_element = input().split()
    for col in range(size):
        if row_element[col] == 'E':
            row_idx = row
            col_idx = col
    matrix.append(row_element)
count_w = 0
count_c = 0
count_m = 0
direction = deque(input().split(', '))

while direction:
    matrix[row_idx][col_idx] = '-'

    command = direction.popleft()

    move_r, move_c = move(row_idx, col_idx, command, size)
    if matrix[move_r][move_c] == 'W':
        print(f'Water deposit found at {move_r, move_c}')
        matrix[move_r][move_c] = '-'
        count_w += 1
    elif matrix[move_r][move_c] == 'C':
        print(f'Concrete deposit found at {move_r, move_c}')
        matrix[move_r][move_c] = '-'
        count_c += 1
    elif matrix[move_r][move_c] == 'M':
        print(f'Metal deposit found at {move_r, move_c}')
        matrix[move_r][move_c] = '-'
        count_m += 1
    elif matrix[move_r][move_c] == 'R':
        print(f'Rover got broken at {move_r, move_c}')
        break
    row_idx, col_idx = move_r, move_c


if count_w >= 1 and count_c >= 1 and count_m >= 1:
    print('Area suitable to start the colony.')
else:
    print('Area not suitable to start the colony.')