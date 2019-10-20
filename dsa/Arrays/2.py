# How do you find the duplicate number on a given integer array? 


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


def find_duplicate(arr):
    m = min(arr)
    M = max(arr)
    
    hashlist = [0]*(M-m+1)
    start_indx = m

    for num in arr:
        hashlist[num - start_indx] += 1

#    print(hashlist)
    repetetions = []
    for indx, num in enumerate(hashlist):
        if num > 1:
            repetetions.append(indx + start_indx)
    
    print('Repeated elements : ', repetetions)


if __name__ == '__main__':
    arr = create_array(3, 10)
    find_duplicate(arr)
