import random


def sort(arr):
    index_0 = -1
    index_1 = -1
    index_2 = -1

    for item in arr:
        if item == 0:
            index_0 += 1
            index_1 += 1
        elif item == 1:
            index_1 += 1
        index_2 += 1

    for i in range(0, len(arr)):
        if i <= index_0:
            arr[i] = 0
        elif index_0 < i <= index_1:
            arr[i] = 1
        else:
            arr[i] = 2
    return arr


def create_array_wt_duplicates(m, M, num_duplicates):
    arr = list(range(m, M+1))
    arr.extend(generate_random_list(m, M, num_duplicates))
    random.shuffle(arr)
    return arr


def generate_random_list(m, M, num_elements):
    arr = []
    arr_len = len(arr)
    while arr_len < num_elements:
        arr.append(random.randint(m, M))
        arr_len = len(arr)

    return arr


def main():
    arr = create_array_wt_duplicates(0, 2, 8)
    print('Input : {}\n'.format(arr))

    print('Sorted Output : {}\n'.format(sort(arr)))


if __name__=="__main__":
    main()
