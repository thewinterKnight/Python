# Uses python3
import sys


def gcd_fast(a, b):
    if b == 0:
        return a

    return gcd_fast(b, a % b)


def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


if __name__ == "__main__":
    # input = sys.stdin.read()
    # a, b = map(int, input.split())

    a = int(input())
    b = int(input())

    print(gcd_naive(a, b))
    print(gcd_fast(a, b))
