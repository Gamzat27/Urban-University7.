# Задача: "Все не так уж просто."

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []


for i in numbers:             # Главный цикл
    if i < 2:             # Условие
        continue
    is_primes = True
    for j in range(2, i):       #Вложенный цикл
        if i % j == 0:        # Условие внутри цикла
            not_primes.append(i)
            is_primes = False
            break
    if is_primes:
        primes.append(i)
print(primes)
print(not_primes)


