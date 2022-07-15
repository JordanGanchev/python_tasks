from collections import deque

customer_list = deque([int(x) for x in input().split(', ')])
taxi_list = [int(x) for x in input().split(', ')]

time = 0

while customer_list and taxi_list:
    customer = customer_list.popleft()
    taxi = taxi_list.pop()

    if taxi >= customer:
        time += customer

    if taxi < customer:
        customer_list.appendleft(customer)


if customer_list:
    print('Not all customers were driven to their destinations')
    print(f"Customers left: {', '.join(str(x) for x in customer_list)}")
else:
    print('All customers were driven to their destinations')
    print(f"Total time: {time} minutes")