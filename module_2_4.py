numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
not_primes = []
primes = []
is_primes = True

for i in numbers:
    for j in range(2, i):
        if i % j == 0:
            not_primes.append(i)
            is_primes = False
            break

    if is_primes:
        primes.append(i)
        if i == 1:
            primes.remove(i)
    else:
        is_primes = True

print(primes)
print(not_primes)