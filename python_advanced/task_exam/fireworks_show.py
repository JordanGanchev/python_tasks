from collections import deque

firework_effects = deque(int(x) for x in input().split(', '))
explosive_power = [int(x) for x in input().split(', ')]

palm_fireworks = 0
willow_fireworks = 0
crossette_fireworks = 0
condition = False
while firework_effects and explosive_power:
    num_effects = firework_effects.popleft()
    num_power = explosive_power.pop()
    mixture = num_effects + num_power
    if num_effects <= 0 or num_power <= 0:
        if num_effects <= 0:
            if num_power > 0:
                explosive_power.append(num_power)
        if num_power <= 0:
            if num_effects > 0:
                firework_effects.appendleft(num_effects)
        continue

    if mixture % 3 == 0 and mixture % 5 != 0:
        palm_fireworks += 1
    elif mixture % 5 == 0 and mixture % 3 != 0:
        willow_fireworks += 1
    elif mixture % 3 == 0 and mixture % 5 == 0:
        crossette_fireworks += 1
    else:
        diff = num_effects - 1
        firework_effects.append(diff)
        explosive_power.append(num_power)

    if palm_fireworks >= 3 and willow_fireworks >= 3 and crossette_fireworks >= 3:
        condition = True
        break

if condition:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")
if firework_effects:
    print(f"Firework Effects left: {', '.join(str(x) for x in firework_effects)}")

if explosive_power:
    print(f"Explosive Power left: {', '.join(str(x) for x in explosive_power)}")

print(f'Palm Fireworks: {palm_fireworks}')
print(f'Willow Fireworks: {willow_fireworks}')
print(f'Crossette Fireworks: {crossette_fireworks}')