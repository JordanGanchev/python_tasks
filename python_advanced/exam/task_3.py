def shopping_cart(*args):
# 69/100
    def check_product(my_dict, command):
        for value in my_dict.values():
            for name in value:
                if command[1] == name:
                    return True

    number_soup = 0
    number_pizza = 0
    number_dessert = 0
    result = ''
    condition = False

    my_dict = {'Soup': [], 'Pizza': [], 'Dessert': []}
    for command in args:
        if command == 'Stop':
            break

        if check_product(my_dict, command):
            continue

        if command[0] == 'Soup':
            number_soup += 1
            if number_soup > 3:
                continue

        if command[0] == 'Pizza':
            number_pizza += 1
            if number_pizza > 4:
                continue

        if command[0] == 'Dessert':
            number_dessert += 1
            if number_dessert > 2:
                continue

        my_dict[command[0]] += [command[1]]

    my_dict_sorted = sorted(my_dict.items(), key=lambda x: (-len(x[1]), x[0]))
    for names in my_dict_sorted:
        name = names[0]
        products = names[1]
        sorted_products = sorted(products)
        result += f'{name}:\n'
        for product in sorted_products:
            result += f' - {product}\n'
            condition = True

    if condition:
        return result
    else:
        return 'No products in the cart!'

print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))
