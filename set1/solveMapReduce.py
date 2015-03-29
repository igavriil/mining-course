from collections import defaultdict


# sieve of eratosthenis
def primes_to(n):
    if n <= 2:
        return []
    sieve = [True]*(n+1)
    for x in range(3, int(n**0.5)+1, 2):
        for y in range(3, (n//x)+1, 2):
            sieve[(x*y)] = False

    return [2]+[i for i in range(3, n, 2) if sieve[i]]


def prime_divisors(number, primes):
    result = []
    for prime in primes:
        if prime <= number and number % prime == 0:
            result.append(prime)
    return result


def map_function(number, primes):
    pairs = {}
    for prime_divisor in prime_divisors(number, primes):
        pairs[prime_divisor] = number
    return pairs


def reduce(numbers):
    dictionary = defaultdict(list)
    primes_divisors = primes_to(max(numbers))
    for number in numbers:
        for prime_divisor in map_function(number, primes_divisors):
            dictionary[prime_divisor].append(number)

    result = {}
    for prime_divisor, numbers in dictionary.iteritems():
        result[prime_divisor] = sum(numbers)
    return dictionary, result

numbers = [15, 21, 24, 30, 49]
print reduce(numbers)