player = input().split(', ')
#57/100
matrix = []
for row in range(6):
    matrix.append(input().split())

while True:
    current_player = player[0]
    coordinate = [int(num) for num in input() if num.isdigit()]
    r, c = coordinate

    if matrix[r][c] == 'E':
        print(f"{current_player} found the Exit and wins the game!")
        break

    if matrix[r][c] == 'T':
        print(f"{current_player} is out of the game! The winner is {player[1]}." )
        break

    if matrix[r][c] == 'W':
        print(f'{current_player} hits a wall and needs to rest.')
        continue

    player[0], player[1] = player[1], player[0]


