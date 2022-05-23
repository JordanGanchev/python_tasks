n, m = [int(x) for x in input().split()]

set_of_n = set()
set_of_m = set()

for _ in range(n):
    num = int(input())
    set_of_n.add(num)

for _ in range(m):
    num = int(input())
    set_of_m.add(num)

result = set_of_n.intersection(set_of_m)
for i in result:
    print(i)