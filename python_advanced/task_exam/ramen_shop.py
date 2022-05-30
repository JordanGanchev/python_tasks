from collections import deque
bowls = [int(x) for x in input().split(', ')]
customers = deque([int(x) for x in input().split(', ')])

while bowls and customers:
    num_bowls = bowls.pop()
    num_customers = customers.popleft()
    if num_bowls < num_customers:
        diff = num_customers - num_bowls
        customers.appendleft(diff)
    elif num_bowls > num_customers:
        diff = num_bowls - num_customers
        bowls.append(diff)
    elif num_bowls == num_customers:
        if bowls or customers:
            continue
        else:
            break
if bowls:
    print('Great job! You served all the customers.')
    ch = [str(x) for x in bowls]
    print(f'Bowls of ramen left: {", ".join(ch)}')
elif customers:
    print("Out of ramen! You didn't manage to serve all customers.")
    ch = [str(x) for x in customers]
    print(f'Customers left: {", ".join(ch)}')
else:
    print('Great job! You served all the customers.')