from collections import deque
import sys
from io import StringIO

test_input1 = '''3, 6
7, 1, 3, 3, 2, 1
1, 3, 9, 8, 5, 6
4, 6, 7, 9, 1, 0
'''
test_input2 = '''2, 4
10, 11, 12, 13
14, 15, 16, 17
'''
sys.stdin = StringIO(test_input1)
#sys.stdin = StringIO(test_input2)


n, m = [int(x) for x in input().split(', ')]

matrix = []


for _ in range(n):
    matrix.append(
        deque([int(x) for x in input().split(', ')])
    )
result = []
count = 0
for row in matrix:
    for num in row:
        result.append(num)
        count += 1
        if count == 2:
            continue


column_sums = [0] * 2

for row_index in range(n):
    for column_index in range(m):
        column_sums[column_index] += matrix[row_index][column_index]


max_matrix_2_2 = []
for element in matrix_input:
    max_element = max(element)
    max_matrix_2_2.append(max_element)


# def read_matrix():
#     (row_count, col_count) = map(int, input().split(" "))
#     return [list(map(int, input().split(" "))) for _ in range(row_count)]
#
#
# def find_best_sum(matrix):
#     rows_count = len(matrix)
#     cols_count = len(matrix[0])
#
#     best_sum = None
#     best_start = None
#
#     for row in range(rows_count - 2):
#         for col in range(cols_count - 2):
#             current_sum = matrix[row][col] + matrix[row][col + 1] + matrix[row][col + 2] + \
#                           matrix[row + 1][col] + matrix[row + 1][col + 1] + matrix[row + 1][col + 2] + \
#                           matrix[row + 2][col] + matrix[row + 2][col + 1] + matrix[row + 2][col + 2]
#
#             if best_sum:
#                 if best_sum < current_sum:
#                     best_sum = current_sum
#                     best_start = (row, col)
#             else:
#                 best_sum = current_sum
#                 best_start = (row, col)
#     if best_start:
#         (row, col) = best_start
#         best_submatrix = [[matrix[row][col], matrix[row][col + 1], matrix[row][col + 2]],
#                           [matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2]],
#                           [matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]]]
#     else:
#         best_submatrix = matrix
#
#     return (best_sum, best_submatrix)
#
#
# matrix = read_matrix()
# best_sum, best_matrix = find_best_sum(matrix)
#
# print(f"Sum = {best_sum}")
# [print(" ".join(map(str, row))) for row in best_matrix]