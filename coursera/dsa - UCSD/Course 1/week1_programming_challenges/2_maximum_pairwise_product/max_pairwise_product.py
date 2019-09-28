# python3

def max_pairwise_product_fast(numbers):
    if len(numbers) == 1:
        return 0

    max_num1 = -1
    max_num2 = -1
    for num in numbers:
        if num > max_num2:
            if max_num2 > max_num1:
                max_num1 = max_num2
            max_num2 = num
    return max_num1 * max_num2

def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product


if __name__ == '__main__':
    input_n = int(input())
    # input_numbers = [int(x) for x in input().split()]

    input_numbers = []
    for i in range(0, input_n):
        input_numbers.append(int(input()))

    print(input_numbers)
    print(max_pairwise_product(input_numbers))
    print(max_pairwise_product_fast(input_numbers))
