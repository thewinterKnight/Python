# How do you find the largest and smallest number in an unsorted integer array? 

import random


def create_array(m, M):
    arr = list(range(m,M+1))

    inpt = input('Enter element to repeat(Enter N/n to skip) : ')
    while inpt not in ['n', 'N']:
        if int(inpt) >=m and int(inpt) <= M:
            arr.append(int(inpt))
        else:
            print('Number out of range !')
        inpt = input('Enter element to repeat(Enter N/n to skip) : ')

    random.shuffle(arr)
    return arr


def findminMax(arr):
    m = float("inf")
    M = -float("inf")

    for num in arr:
        if num < m:
            m = num
        elif num > M:
            M = num

    print(m, M)


if __name__ == '__main__':
    arr = create_array(7, 51)
    findminMax(arr)
