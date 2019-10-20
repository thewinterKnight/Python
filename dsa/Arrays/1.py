# How do you find the missing number in a given integer array of 1 to 100?


import random

def create_input():
    arr = list(range(0,100))
    input_missing = input('Enter missing number : ')
    arr.remove(input_missing)
    random.shuffle(arr)
    return arr


def detect_missing(arr):
    hashlist = [0]*100

    for num in arr:
        hashlist[num] += 1

    output_missing = hashlist.index(0)
    
    print('The missing number in the array is {}\n'.format(output_missing))


if __name__ == "__main__":
    arr = create_input()
    detect_missing(arr)
