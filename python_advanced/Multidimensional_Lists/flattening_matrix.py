n = int(input())

result = []

for _ in range(n):
    row = [int(x) for x in input().split(', ')]
    for num in row:
        result.append(num)

print(result)