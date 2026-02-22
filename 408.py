def Primes(n):
    for i in range(n + 1):
        isPrime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))
        if isPrime(i) == True:
            yield i


n = int(input())

for i in Primes(n):
    print(i, end = " ")