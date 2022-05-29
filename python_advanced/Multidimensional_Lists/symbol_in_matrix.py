import sys
from io import StringIO

test_input1 = '''3
ABC
DEF
X!@
!
'''
test_input2 = '''4
asdd
xczc
qwee
qefw
4
'''
#sys.stdin = StringIO(test_input1)
#sys.stdin = StringIO(test_input2)


def find_symbol(matrix, symbol):
    for row_index in range(n):
        for column_index in range(n):
            if matrix[row_index][column_index] == symbol:
                return row_index, column_index
    return None


n = int(input())

matrix = [list(input()) for _ in range(n)]
symbol = input()

result = find_symbol(matrix, symbol)

if result:
    row_index, column_index = result
    print(f'({row_index}, {column_index})')
else:
    print(f'{symbol} does not occur in the matrix')


# import sys
# from io import StringIO
#
# test_input1 = '''3
# ABC
# DEF
# X!@
# !
# '''
# test_input2 = '''4
# asdd
# xczc
# qwee
# qefw
# 4
# '''
# #sys.stdin = StringIO(test_input1)
# #sys.stdin = StringIO(test_input2)
#
# n = int(input())
#
# matrix = [list(input()) for _ in range(n)]
# symbol = input()
#
# is_found = False
#
# for row_index in range(n):
#     if is_found:
#         break
#     for column_index in range(n):
#         if matrix[row_index][column_index] == symbol:
#             is_found = True
#             print(f'({row_index}, {column_index})')
#             break
#
# if not is_found:
#     print(f'{symbol} does not occur in the matrix')