from collections import deque
quantity_food = int(input())
queue = deque([int(x) for x in input().split()])

print(max(queue))

while queue:
    if quantity_food >= queue[0]:
        quantity_food -= queue[0]
        queue.popleft()
    else:
        break


if not queue:
    print('Orders complete')
else:
    result = ''
    for i in queue:
        result += str(i)
        result += chr(32)
    print(f"Orders left: {result}")


