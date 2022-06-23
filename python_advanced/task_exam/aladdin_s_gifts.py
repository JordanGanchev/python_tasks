from collections import deque
#83/100
materials = [int(x) for x in input().split(' ')]
magics = deque([int(x) for x in input().split()])
gemstone = False
porcelain_sculpture = False
gold = False
diamond = False
result = {'Diamond Jewellery': 0, 'Gemstone': 0, 'Gold': 0, 'Porcelain Sculpture': 0}
while materials and magics:
    material = materials.pop()
    magic = magics.popleft()
    sum_number = material + magic
    if sum_number < 100:
        if sum_number % 2 == 0:
            sum_number = (material * 2) + (magic * 3)
        else:
            sum_number = (material + magic) * 2
    if sum_number > 499:
        sum_number = (material + magic) / 2

    if 100 <= sum_number <= 199:
        result['Gemstone'] += 1
        gemstone = True
    if 200 <= sum_number <= 299:
        result['Porcelain Sculpture'] += 1
        porcelain_sculpture = True
    if 300 <= sum_number <= 399:
        result['Gold'] += 1
        gold = True
    if 400 <= sum_number <= 499:
        result['Diamond Jewellery'] += 1
        diamond = True

if gemstone and porcelain_sculpture or gold and diamond:
    print('The wedding presents are made!')
else:
    print('Aladdin does not have enough wedding presents.')

if materials:
    mat = map(str, materials)
    print(f"Materials left: {''.join(mat)}")


if magics:
    mag = map(str, magics)
    print(f"Magic left: {', '.join(mag)}")

for key, value in result.items():
    if value != 0:
        print(f"{key}: {value}")

