import sys
from io import StringIO

test_input1 = '''Ivan, Peter
12 21 18 4 20 7 11
9 D D D D D 10
15 D T T T D 3
2 D T B T D 19
17 D T T T D 6
22 D D D D D 14
5 8 23 13 16 1 24
(3, 3)
'''
test_input2 = '''George, Hristo
17 8 21 6 13 3 24
16 D D D D D 14
7 D T T T D 15
23 D T B T D 2
9 D T T T D 22
19 D D D D D 10
12 18 4 20 5 11 1
(1, 0)
(2, 3)
(0, 0)
(4, 2)
(5, 1)
(3, 1)
(0, 0)
(2, 3)
'''
#sys.stdin = StringIO(test_input1)
#sys.stdin = StringIO(test_input2)

players = input().split(', ')
player_1, player_2 = players
matrix = []
size = 7
for row in range(size):
    matrix.append(input().split())

count_move_1 = 0
count_move_2 = 0
point = 0
score_player_1 = 501
score_player_2 = 501

while True:
    current_player = players[0]
    r, c = (int(x) for x in input().strip('()').split(', '))
    if r < 0 or r >= size or c < 0 or c >= size:
        if current_player == player_1:
            score_player_1 -= point
            count_move_1 += 1
        else:
            score_player_2 -= point
            count_move_2 += 1
        players[0], players[1] = players[1], players[0]
        continue

    if matrix[r][c].isdigit():
        point = int(matrix[r][c])

    if matrix[r][c] == 'D':
        num_1 = int(matrix[r][0])
        num_2 = int(matrix[r][6])
        num_3 = int(matrix[0][c])
        num_4 = int(matrix[6][c])
        point = (num_1 + num_2 + num_3 + num_4) * 2

    if matrix[r][c] == 'T':
        num_1 = int(matrix[r][0])
        num_2 = int(matrix[r][6])
        num_3 = int(matrix[0][c])
        num_4 = int(matrix[6][c])
        point = (num_1 + num_2 + num_3 + num_4) * 3

    if current_player == player_1:
        score_player_1 -= point
        count_move_1 += 1
    else:
        score_player_2 -= point
        count_move_2 += 1

    if matrix[r][c] == 'B':
        if current_player == player_1:
            print(f'{current_player} won the game with {count_move_1} throws!')
            break
        else:
            print(f'{current_player} won the game with {count_move_2} throws!')
            break

    if score_player_1 <= 0:
        print(f'{current_player} won the game with {count_move_1} throws!')
        break

    if score_player_2 <= 0:
        print(f'{current_player} won the game with {count_move_2} throws!')
        break

    players[0], players[1] = players[1], players[0]

#------------------------------------------------------------------------------------------other

# def valid_coordinates(row_index, col_index, size):
#     return 0 <= row_index < size and 0 <= col_index < size
#
#
# def calculate_score(row, col, size, multiplier):
#     sum_score = int(board[0][col]) + int(board[size - 1][col]) + int(board[row][0]) + int(board[row][size - 1])
#     if multiplier == "D":
#         return sum_score * 2
#     elif multiplier == "T":
#         return sum_score * 3
#     elif multiplier == "B":
#         return 501
#
#
# size = 7
# player_1, player_2 = input().split(", ")
# board = [input().split() for _ in range(size)]
#
# players_scores = {player_1: 501, player_2: 501}
# players_throws = {player_1: 0, player_2: 0}
#
# current_player, next_player = player_1, player_2
# winner = ""
#
# while True:
#
#     throw_row, throw_col = eval(input())
#     players_throws[current_player] += 1
#
#     if valid_coordinates(throw_row, throw_col, size):
#
#         if board[throw_row][throw_col].isdigit():
#             players_scores[current_player] -= int(board[throw_row][throw_col])
#
#         else:
#             multiplier = board[throw_row][throw_col]
#             score = calculate_score(throw_row, throw_col, size, multiplier)
#             players_scores[current_player] -= score
#
#         if players_scores[current_player] <= 0:
#             winner = current_player
#             break
#
#     current_player, next_player = next_player, current_player
#
# print(f"{winner} won the game with {players_throws[winner]} throws!")

#----------------------------------------------------------------------------------------------------other

#
# def position_value(r, c):
#     row_value = int(matrix[r][0]) + int(matrix[r][size - 1])
#     col_value = int(matrix[0][c]) + int(matrix[size - 1][c])
#     return row_value + col_value
#
#
# size = 7
# player_one, player_two = input().split(', ')
# players = {player_one: 501, player_two: 501}
#
# matrix = []
# for _ in range(size):
#     elements = input().split(' ')
#     matrix.append(elements)
#
# current_player, other_player = player_one, player_two
# throws = 0
# while True:
#     if current_player == player_one:
#         throws += 1
#     result = players[current_player]
#     row, col = (int(x) for x in input().strip('()').split(', '))
#     if row < 0 or row >= size or col < 0 or col >= size:
#         current_player, other_player = other_player, current_player
#         continue
#
#     value = matrix[row][col]
#     if value == 'B':
#         result -= result
#     elif value == "D":
#         result -= position_value(row, col) * 2
#     elif value == "T":
#         result -= position_value(row, col) * 3
#     else:
#         result -= int(value)
#     players[current_player] = result
#     if result <= 0:
#         break
#     current_player, other_player = other_player, current_player
#
# print(f'{current_player} won the game with {throws} throws!')