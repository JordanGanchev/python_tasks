def stock_availability(*args):
    #54/100
    inventory = args[0]
    income_expense = args[1]
    move = []
    products_numbers = ''
    condition_str = False
    condition_int = False
    for i in args:
        if i == inventory or i == income_expense:
            continue
        else:
            move.append(i)

    products_numbers = [str(x) for x in move]

    for object in products_numbers:
        if object.isalpha():
            condition_str = True
        else:
            condition_int = True

    if income_expense == 'delivery':
        if products_numbers:
            for i in range(len(products_numbers)):
                inventory.append(products_numbers[0 + i])

    elif income_expense == 'sell':
        new_list = []
        if products_numbers and condition_str:
            for name in move:
                for name2 in inventory:
                    if name != name2:
                        new_list.append(name2)
            inventory = new_list

        elif products_numbers and condition_int:
            num = int(products_numbers[0])
            for i in range(num):
                inventory = inventory.pop(0)
                inventory = args[0]

        else:
            inventory = inventory.pop(0)
            inventory = args[0]

    return inventory


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))


