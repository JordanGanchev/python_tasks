from collections import deque

price_or_bullet = int(input())
size_gun = int(input())
bullets = deque([int(x) for x in input().split()])
locks = deque([int(x) for x in input().split()])
intelligence = int(input())
counter = 1
shoots = 0

while True:
    if len(bullets) == 0 or len(locks) == 0:
        break

    bullet_last = bullets.pop()
    lock_first = locks.popleft()

    if bullet_last <= lock_first:
        print('Bang!')
    else:
        print('Ping!')
        locks.appendleft(lock_first)
    if bullets:
        if counter == size_gun:
            print('Reloading!')
            counter = 0
    counter += 1
    shoots += 1

if not locks:
    bullets_cost = shoots * price_or_bullet
    earned = intelligence - bullets_cost
    print(f'{len(bullets)} bullets left. Earned ${earned}')
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")

