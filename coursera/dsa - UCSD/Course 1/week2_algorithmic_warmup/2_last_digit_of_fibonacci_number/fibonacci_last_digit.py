# Uses python3
import sys

def get_fibonacci_last_digit_dp(n):
    if n <= 1:
        return n

    Fbn = []
    Fbn.append(0)
    Fbn.append(1)
    i = 2
    while Fbn[-1] is None or Fbn[-1] < n:
        if Fbn[i-1] + Fbn[i-2] > n:
            break
        Fbn.append(Fbn[i-1] + Fbn[i-2])
        i += 1

    print(Fbn[-1])



def get_fibonacci_last_digit_opt(n):
    if n <= 1:
        return n

    n1 = 0
    n2 = 1
    while n1 <= n:
        temp = n2
        n2 = n1 + n2
        n1 = temp
        if n2 > n:
            break

    print(n1)



def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10

if __name__ == '__main__':
    # input = sys.stdin.read()
    n = int(input())

    # print(get_fibonacci_last_digit_naive(n))
    get_fibonacci_last_digit_opt(n)
    get_fibonacci_last_digit_dp(n)