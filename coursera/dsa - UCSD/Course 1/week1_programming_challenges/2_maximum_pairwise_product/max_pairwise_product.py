# python3

def max_pairwise_prd_fast(numbers):
    if len(numbers) < 2:
        return 0

    max_indx1 = -1
    max_indx2 = -2
    for index in range(0, len(numbers)):
        if (max_indx1 < 0 or numbers[index] > numbers[max_indx1]) and index != max_indx2:
            if max_indx1 >=0 and (max_indx2 < 0 or numbers[max_indx1] > numbers[max_indx2]):
                max_indx2 = max_indx1
            max_indx1 = index

        if (max_indx2 < 0 or numbers[index] > numbers[max_indx2]) and index != max_indx1:
            if max_indx2 >= 0 and (max_indx1 < 0 or numbers[max_indx2] > numbers[max_indx1]):
                max_indx1 = max_indx2
            max_indx2 = index

    print(numbers)
    print('{} & {}'.format(max_indx1, max_indx2))

    if max_indx1 >= 0 and max_indx2 >= 0:
        return numbers[max_indx1] * numbers[max_indx2]

    return 0;

def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product


def stress_test():
    import random

    num_tests = 100
    min_arr_len = 10
    max_arr_len = 50
    min_num = 10
    max_num = 20000000
    for t in range(0, num_tests):
        arr_len = random.randint(min_arr_len, max_arr_len)
        arr = []
        
        for i in range(arr_len):            
            arr.append(random.randint(min_num, max_num))

            if max_pairwise_product(arr) != max_pairwise_prd_fast(arr):
                print("Test failed at {}\n".format(i))
                print("max_pairwise_product = {},\tmax_pairwise_product_fast = {}\n".format(max_pairwise_product(arr), max_pairwise_prd_fast(arr)))
                return
        print("Stress Test passed !\n")



if __name__ == '__main__':
    # input_n = int(input())
    # input_numbers = [int(x) for x in input().split()]
    # print(max_pairwise_product(input_numbers))

    stress_test()
