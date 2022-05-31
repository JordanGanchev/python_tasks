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
#sys.stdin = StringIO(test_input1)
#sys.stdin = StringIO(test_input2)
# 80/100
n, m = [int(x) for x in input().split(', ')]

matrix = []

for _ in range(n):
    matrix.append(
        [int(x) for x in input().split(', ')]
    )
result = dict()
for row in range(n - 1):
    for col in range(m - 1):
        a = matrix[row][col]
        b = matrix[row][col + 1]
        c = matrix[row + 1][col]
        d = matrix[row + 1][col + 1]

        result[sum([a, b, c, d])] = [a, b, c, d]
key_value = 0
after_processing = 0
for key, value in result.items():
    if key > key_value:
        key_value = key
        after_processing = key, value

print(after_processing[1][0], after_processing[1][1])
print(after_processing[1][2], after_processing[1][3])
print(after_processing[0])
