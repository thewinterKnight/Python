# Uses python3
import sys

<<<<<<< HEAD

def hcf(a, b):
	if b == 0:
		return a

	return hcf(b, a % b)


def lcm(a, b):
	return (a * b) / hcf(a, b)

=======
def gcd(a, b):
	if b == 0:
		return a

	return gcd(b, a % b)

def lcm_fast(a, b):
	return(a*b / gcd(a,b))
>>>>>>> 67d35a226509f1c80278b66a78c6cc9ce74c125a

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b


if __name__ == '__main__':
    # input = sys.stdin.read()
    # a, b = map(int, input.split())
    # print(lcm_naive(a, b))
<<<<<<< HEAD
=======

    a = int(input())
    b = int(input())
    print(lcm_fast(a,b))
>>>>>>> 67d35a226509f1c80278b66a78c6cc9ce74c125a

    a = int(input())
    b = int(input())
    print(lcm(a, b))
