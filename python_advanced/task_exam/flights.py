def flights(*args):
    list_args = []
    my_dict = {}
    for name in args:
        if name == 'Finish':
            break
        list_args.append(str(name))

    for i in range(0, len(list_args), 2):
        key = list_args[i]
        value = int(list_args[i + 1])
        if key not in my_dict:
            my_dict[key] = value
        else:
            my_dict[key] += value
    return my_dict

print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))