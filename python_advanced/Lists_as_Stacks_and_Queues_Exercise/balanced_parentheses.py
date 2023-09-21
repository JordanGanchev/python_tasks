

# series = deque(input())
# flag = False
#
# while series:
#
#     if len(series) % 2 == 0:
#         first_element = series.popleft()
#         last_element = series.pop()
#     else:
#         flag = False
#         break
#
#     if first_element in '),],}':
#         flag = False
#         break
#
#     if first_element == '{' and last_element == '}'\
#             or first_element == '[' and last_element == ']'\
#             or first_element == '(' and last_element == ')':
#         flag = True
#     else:
#         flag = False
#         break
#
# if flag:
#     print('YES')
# else:
#     print('NO')

from collections import deque
expression = deque(input())
opening_brackets = '([{'
closing_brackets = ')]}'
counter = 0
while expression and counter < len(expression) / 2:
    if expression[0] not in opening_brackets:
        break
    index = opening_brackets.index(expression[0])
    if expression[1] == closing_brackets[index]:
        expression.popleft()
        expression.popleft()
        expression.rotate(counter)
        counter = 0
    else:
        expression.rotate(-1)
        counter += 1

if expression:
    print('NO')
else:
    print('YES')