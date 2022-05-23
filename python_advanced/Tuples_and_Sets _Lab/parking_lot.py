number_car = int(input())

parking = set()

for _ in range(number_car):
    input_line = input().split(', ')
    command = input_line[0]
    number = input_line[1]
    if command == 'IN':
        parking.add(number)
    if command == 'OUT':
        parking.remove(number)

if parking:
    for num in parking:
        print(num)
else:
    print("Parking Lot is Empty")