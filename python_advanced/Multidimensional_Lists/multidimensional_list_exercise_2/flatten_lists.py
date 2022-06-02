number_list = input().split('|')[::-1]
sorted_list = []
for num in number_list:
    for number in num.split():
        sorted_list.append(number)

print(' '.join(sorted_list))