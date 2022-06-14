from collections import deque
#58/100
vowels = deque(input().split())
consonants = input().split()

words = {"rose": 0, "tulip": 0, "lotus": 0, "daffodil": 0}
condition = False
while True:
    if condition:
        break
    if not vowels:
        print('Cannot find any word!')
        break
    if not consonants:
        print('Cannot find any word!')
        break

    letter_vowels = vowels.popleft()
    letter_consonants = consonants.pop()
    for key, value in words.items():
        for letter in key:
            if letter == letter_vowels:
                words[key] += 1
        for letter in key:
            if letter == letter_consonants:
                words[key] += 1

    for key, value in words.items():
        if len(key) == value:
            print(f'Word found: {key}')
            condition = True


if vowels:
    print(f"Vowels left: {' '.join(vowels)}")

if consonants:
    print(f"Consonants left: {' '.join(consonants)}")

