# with open('./text.txt', 'r') as file:
#     index = 0
#     for line in file:
#         if index % 2 == 0:
#             print(line.strip())
#         index += 1
targets_symbols = ["-", ",", ".", "!", "?"]
with open('./text.txt', 'r') as file:
    for index, line in enumerate(file):
        if index % 2 == 0:
            result = ' '.join(line.strip().split()[::-1])
            for symbol in targets_symbols:
                result = result.replace(symbol, '@')
            print(result)
