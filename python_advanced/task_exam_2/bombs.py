from collections import deque
#90/100
bomb_effects = deque([int(x) for x in input().split(', ')])
bomb_casings =[int(x) for x in input().split(', ')]
condition = False
datura_bombs = 0
cherry_bombs = 0
smoke_decoy_bombs = 0

while bomb_casings and bomb_casings:
    effect = bomb_effects.popleft()
    casing = bomb_casings.pop()

    mix_bomb = effect + casing

    if mix_bomb == 40:
        datura_bombs += 1
    elif mix_bomb == 60:
        cherry_bombs += 1
    elif mix_bomb == 120:
        smoke_decoy_bombs += 1

    else:
        bomb_effects.appendleft(effect)
        bomb_casings.append(casing - 5)

    if datura_bombs >= 3 and cherry_bombs >= 3 and smoke_decoy_bombs >= 3:
        condition = True
        break

if condition:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f"Bomb Effects: {', '.join([str(x) for x in bomb_effects])}")
else:
    print('Bomb Effects: empty')

if bomb_casings:
    print(f"Bomb Casings: {', '.join([str(x) for x in bomb_casings])}")
else:
    print('Bomb Casings: empty')


print(f'Cherry Bombs: {cherry_bombs}')
print(f'Datura Bombs: {datura_bombs}')
print(f'Smoke Decoy Bombs: {smoke_decoy_bombs}')
