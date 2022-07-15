def numbers_searching(*args):
    min_number = min(args)
    max_number = max(args)
    list_last_number = []
    double_number = []
    list_result = []
    for num in range(min_number, max_number + 1, 1):
        if num not in args:
            list_last_number.append(num)
        count = 0
        for i in args:
            if i == num:
                count += 1
                if count > 1:
                    double_number.append(num)

    list_result = list_last_number + [double_number]
    return list_result

#print(numbers_searching(1, 2, 4, 2, 5, 4))

#print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))

print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))