data_input = [int(x) for x in input().split(' ')]
target = int(input())
targets = set()
values_map = {}

for value in data_input:
    if value in targets:
        p1 = value
        p2 = values_map[value]
        print(f'{p1} + {p2} = {target}')
    else:
        targets.add(target - value)
        values_map[target - value] = value