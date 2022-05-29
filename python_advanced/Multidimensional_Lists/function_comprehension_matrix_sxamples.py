# def remove_odd(ll):
#     return [x for x in ll if x % 2 == 0]
#
# print(
#     [remove_odd(row) for row im matrix]
# )

def matrix_sum(matrix):
    n = len(matrix)
    m = len(matrix[0])
    result = 0
    for row_index in range(n):
        for column_index in range(m):
            result += matrix[row_index][column_index]
    return result


import sys
from io import StringIO

test_input1 = '''3, 6
7 1 3 3 2 1
1 3 9 8 5 6
4 6 7 9 1 0
'''
test_input2 = '''3, 3
1 2 3
4 5 6
7 8 9
'''
sys.stdin = StringIO(test_input1)
sys.stdin = StringIO(test_input2)

