from collections import deque

number_orders = deque([int(x) for x in input().split(', ')])
number_capacity = [int(x) for x in input().split(', ')]
counter_on_pizza = 0
while number_orders and number_capacity:
    order = number_orders.popleft()
    capacity = number_capacity.pop()

    if order > 10 or order <= 0:
        number_capacity.append(capacity)
        continue

    if order <= capacity:
        counter_on_pizza += order

    if order > capacity:
        diff = abs(capacity - order)
        number_orders.appendleft(diff)
        counter_on_pizza += capacity

if number_capacity:
    print('All orders are successfully completed!')
    print(f'Total pizzas made: {counter_on_pizza}')
    if number_capacity:
        print(f"Employees: {', '.join([str(x) for x in number_capacity])}")

else:
    print('Not all orders are completed.')
    print(f"Orders left: {', '. join([str(x) for x in number_orders])}")