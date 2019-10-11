
def fetch_subarray_start_indx(sum_dict, rem):
    for k, v in sum_dict.items():
        if k == rem:
            return v
    return None


def fetch_subarray(arr, n):
    sum_dict = {}
    temp_sum = 0
    for i in range(0, len(arr)+1):
        if i < len(arr):
            temp_sum += arr[i]

        if temp_sum == n:
            print(arr[0:i+1])

        start_indx = fetch_subarray_start_indx(sum_dict, temp_sum-n)
        if start_indx is not None:
            print(arr[start_indx+1:i+1])

        sum_dict[temp_sum] = i



if __name__=="__main__":
    print("Number of elements : ")
    n = int(input())

    arr = []
    print("Enter elements :")
    for i in range(0, n):
        arr.append(int(input()))

    print("Enter sum value : ")
    sum = int(input())

    fetch_subarray(arr, sum)