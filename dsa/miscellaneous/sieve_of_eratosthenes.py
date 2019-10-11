import math


def sieve_of_eratosthenes(n):
    if n < 2:
        return None

    primes_indices = [1] * (n+1)
    primes_indices[0] = 0
    primes_indices[1] = 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if primes_indices[i] == 1:
            j = 2
            while i*j <= n:
                primes_indices[i*j] = 0
                j += 1

    # print(primes_indices)
    prime_numbers = []
    for prime, indx in enumerate(primes_indices):
        if indx == 1:
            prime_numbers.append(prime)

    return prime_numbers


if __name__ == "__main__":
    n = int(input())
    print(sieve_of_eratosthenes(n))