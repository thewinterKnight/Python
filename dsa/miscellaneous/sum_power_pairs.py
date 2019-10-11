
def Partition(arr, start_indx, end_indx):
    pivot_indx = end_indx
    pivot = arr[pivot_indx]
    partition_indx = start_indx
    
    for i in range(start_indx, end_indx):
        if arr[i] < pivot:
            Swap(arr, i, partition_indx)
            partition_indx += 1
    Swap(arr, partition_indx, pivot_indx)
    
    return partition_indx


def QuickSort(arr, start_indx, end_indx):
    if start_indx < end_indx:
        pivot_indx = Partition(arr, start_indx, end_indx)
        
        QuickSort(arr, start_indx, pivot_indx-1)
        QuickSort(arr, pivot_indx+1, end_indx)


def Swap(arr, indx1, indx2):
    temp = arr[indx1]
    arr[indx1] = arr[indx2]
    arr[indx2] = temp


def num_power_pairs_naive(arr1, arr2):
    pair_count = 0
    
    for x in arr1:
        for y in arr2:
            if pow(x, y) > pow(y, x):
                pair_count += 1
    print(pair_count)
    

def find_smallest_element_greater_than(Y, start_indx, end_indx, smallest):
    if start_indx > end_indx:
        return

    # print(Y[start_indx:end_indx+1])

    mid = int(start_indx + (end_indx - start_indx) / 2)

    # # for smallest element present in array...
    # if mid == Y.index(smallest) + 1:
    #     return Y[mid]

    if smallest < Y[mid] and (mid == 0 or Y[mid-1] <= smallest):
        return Y[mid]

    if smallest < Y[mid]:
        return find_smallest_element_greater_than(Y, start_indx, mid, smallest)
    else:
        return find_smallest_element_greater_than(Y, mid+1, end_indx, smallest)


def num_power_pairs_optimal(X, Y):
    QuickSort(Y, 0, len(Y) - 1)

    pair_count = 0
    for x in X:
        if x == 0:
            continue
        elif x == 1:
            pair_count += Y.count(0)
            continue

        if x > 1:
            pair_count += Y.count(1)

        if x == 3:
            pair_count += Y.count(2)

        y = find_smallest_element_greater_than(Y, 0, len(Y)-1, x)
        pair_count += len(Y) - Y.index(y)

        if x == 2:
            pair_count -= (Y.count(3) + Y.count(4))

    print(pair_count)
    

def main():
    # arrays = []
    # for i in range(0, 2):
    #     print("\nNumber of elements : ")
    #     n = int(input())

    #     arr = []
    #     print("Enter elements :")
    #     for i in range(0, n):
    #         arr.append(int(input()))

    #     arrays.append(arr)

    # arrays = [[2,1,8,9,5,7,9], [1,5,4,9,10,11,12,7,8,2,9]]

    arrays = [[2,1,5], [3,6,4]]

    num_power_pairs_naive(arrays[0], arrays[1])
    num_power_pairs_optimal(arrays[0], arrays[1])

    # print(arrays[1])
    # QuickSort(arrays[1], 0, len(arrays[1]) - 1)
    # print('SMALLEST : {}'.format(find_smallest_element_greater_than(arrays[1], 0, len(arrays[1]) - 1, 6)))


if __name__=="__main__":
    main()


# def format_input_arr():
#     return list(map(lambda x: int(x), input().split()))



# num_pairs = int(input())
# arrays = []
# for i in range(0, num_pairs):
#     arr_lengths = format_input_arr()
    
#     arr1 = format_input_arr()
#     arr2 = format_input_arr()

#     QuickSort(arr1, 0, len(arr1)-1)
#     QuickSort(arr2, 0, len(arr2)-1)
#     print(arr1, arr2)
    
#     num_power_pairs_naive(arr1, arr2)
#     num_power_pairs_optimal(arr1, arr2)