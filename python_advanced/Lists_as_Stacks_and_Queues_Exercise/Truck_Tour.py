from collections import deque

pumps_count = int(input())
pumps = deque()
for _ in range(pumps_count):
    pumps.append([int(x) for x in input().split()])

for attempt in range(pumps_count):
    truck = 0
    failed = False
    for petrol, distance in pumps:
        truck = truck + petrol - distance
        if truck < 0:
            failed = True
            break
    if failed:
        pumps.append(pumps.popleft())

    else:
        print(attempt)
        break