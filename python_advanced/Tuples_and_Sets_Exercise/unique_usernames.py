number = int(input())

set_name = set()

for _ in range(number):
    name = input()
    set_name.add(name)

for name in set_name:
    print(name)

