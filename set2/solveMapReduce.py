# sieve of eratosthenis
def primes(n):
    if n <= 2:
        return []
    sieve = [True]*(n+1)
    for x in range(3, int(n**0.5)+1, 2):
        for y in range(3, (n//x)+1, 2):
            sieve[(x*y)] = False

    return [2]+[i for i in range(3, n, 2) if sieve[i]]


def divisors(numbers, primes):
    for number in numbers:
        for prime in primes:
            if number >= prime and number % prime == 0:
                primes[prime].append(number)
    return primes

numbers = (15, 21, 24, 30, 49)

primeFactors = primes(49)
dictFactor = {}
for prime in primeFactors:
    dictFactor.setdefault(prime, [])

primeDivisors = divisors(numbers, dictFactor)
print primeDivisors
reduced = {}
for key, value in dictFactor.iteritems():
    reduced[key] = sum(value)

print reduced
