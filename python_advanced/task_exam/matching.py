from collections import deque
# 92/100
males = [int(x) for x in input().split()]
female = deque(int(x) for x in input().split())

matches = 0

while males and female:
    a_men = males.pop()
    a_woman = female.popleft()

    if a_men <= 0 and a_woman <= 0:
        continue
    if a_men <= 0:
        female.appendleft(a_woman)
        continue
    elif a_woman <= 0:
        males.append(a_men)
        continue

    if a_men % 25 == 0:
        males.pop(-1)
        female.append(a_woman)
        continue

    if a_woman % 25 == 0:
        female.popleft()
        males.append(a_men)
        continue

    if a_men == a_woman:
        matches += 1
    else:
        diff = a_men - 2
        males.append(diff)

print(f'Matches: {matches}')

if males:
    new = males[::-1]
    print(f"Males left: {', '. join([str(x) for x in new])}")
else:
    print('Males left: none')

if female:
    print(f"Females left: {', '. join([str(x) for x in female])}")
else:
    print('Females left: none')