import random
import string


def generate_random_string(length):
    letters = string.ascii_uppercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string


S = generate_random_string(10 ** 6)
Q = generate_random_string(10 ** 6)

import time
start_time = time.time()

D = {} # Словарь. Значение - символ строки: ключ - сколько раз символ встречается в строке.
       # Использую словарь как счетчик использованных символов.

for i in range(len(S)):
    if S[i] in D:
        D[S[i]] += 1
    elif S[i] not in D and Q[i] == S[i]:
        continue
    elif S[i] not in D:
        D[S[i]] = 1

with open ('D:\output.txt', 'w') as ouf:
    for i in range(len(S)): # Цикл длиной в последовательность количества символов в строке.
        if Q[i] == S[i]:
            ouf.write('correct' + '\n')
        if Q[i] != S[i]: # Условие. Если i-тые символы двух строк не ранвы, то:
            if Q[i] in D and D[Q[i]] != 0: # Условие. Если символ есть в ключах словаря и значение по этому ключу не равно 0.
                ouf.write('present' + '\n')
                D[Q[i]] -= 1 # уменьшаем значение в словаре по ключу.
            else: # В остальных случаях.
                ouf.write('absent' + '\n')

print("--- %s seconds ---" % (time.time() - start_time))
