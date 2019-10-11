import math


def fetch_sum_pairs(arr, req_sum):
    sum_map = {}
    pairs = set()
    pair_count = 0

    for i in range(0, len(arr)):
        if req_sum - arr[i] in sum_map.keys():
            pair_count += 1
            pairs.add((arr[i], req_sum - arr[i]))
        else:
            sum_map[arr[i]] = 1

    return pair_count, pairs



if __name__=="__main__":
    print("Number of elements : ")
    n = int(input())

    arr = []
    print("Enter elements :")
    for i in range(0, n):
        arr.append(int(input()))

    print("Enter sum value : ")
    req_sum = int(input())

    pair_count, pairs = fetch_sum_pairs(arr, req_sum)
    print('{} pairs\n{}'.format(pair_count, pairs))