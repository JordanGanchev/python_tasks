number_of_name = int(input())
set_names = set()
for _ in range(number_of_name):
    input_names = input()
    set_names.add(input_names)

for name in set_names:
    print(name)