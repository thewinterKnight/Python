import random


def QuickSelect(arr, start, end, k):
	
	pivot_index = Partition(arr, start, end)

	if pivot_index >= 0:
		if pivot_index == k:
			print('{} smallest element in array is {}'.format(k+1, arr[pivot_index]))
			return
		elif pivot_index < k:
			return QuickSelect(arr, pivot_index+1, end, k)

		return QuickSelect(arr, start, pivot_index-1, k)


def Partition(arr, start, end):
	pivot_index = end
	pivot_element = arr[pivot_index]
	i = start-1
	for j in range(start, end):
		if arr[j] < pivot_element:
			i += 1
			Swap(arr, i, j)

	Swap(arr, i+1, pivot_index)
	return i+1



def Swap(arr, index1, index2):
	temp = arr[index1]
	arr[index1] = arr[index2]
	arr[index2] = temp



def main():
    # print("Number of elements : ")
    # n = int(input())

    # arr = []
    # print("Enter elements :")
    # for i in range(0, n):
    #     arr.append(int(input()))

    # print("Enter k value : ")
    # k = int(input())

    arr = [17, 10, 24, 3, 20, 15, 13, 31, 6, 4, 9]

    for k in range(1, len(arr)+1):
    	QuickSelect(arr, 0, len(arr)-1, k-1)
    	

    # arr = create_array_wt_duplicates(11,19,0)
    # print(arr)



if __name__=="__main__":
	main()