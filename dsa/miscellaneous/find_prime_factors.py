import math


def find_prime_factors(n):
	if n < 2:
		return None

	prime_factors = []
	while n % 2 == 0:
		prime_factors.append(2)
		n = n / 2

	for i in range(3, int(math.sqrt(n)) + 1, 2):
		while n % i == 0:
			prime_factors.append(i)
			n = n / i

	if n > 2:
		prime_factors.append(n)

	return prime_factors
	


if __name__=="__main__":
	n = int(input())
	print(find_prime_factors(n))