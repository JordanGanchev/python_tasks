def words_sorting(*args):
    my_dict = {}
    count = 0
    count_total = 0
    for name in args:
        count = 0
        for letter in name:
            count += ord(letter)
            count_total += count
        my_dict[name] = count
    if count_total % 2 == 0:
        result = sorted(my_dict.items())
    else:
        result = sorted(my_dict.items(), key=lambda p: p[1], reverse=True)

    return '\n'.join(f'{word} - {count}' for (word, count) in result)



