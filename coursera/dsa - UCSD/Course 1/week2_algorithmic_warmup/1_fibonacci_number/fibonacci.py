# Uses python3

def calculate_fibonacci(n):
    n1 = 0
    n2 = 1
    while n1 <= n:
        print(str(n1))
        temp = n2
        n2 = n1 + n2
        n1 = temp


def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

n = int(input())
# print(calc_fib(n))

calculate_fibonacci(n)
