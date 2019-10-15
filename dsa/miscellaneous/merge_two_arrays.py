


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


def main():
	arrays = []
	for i in range(0, 2):
		print("\nNumber of elements : ")
		n = int(input())

		arr = []
		print("Enter elements :")
		for i in range(0, n):
			arr.append(int(input()))

		arrays.append(arr)

	# arrays = [[6,1,15,12,9,14,17,3], [10,8,21,19,5,4,16]]

	arrays[0].extend(arrays[1])
	QuickSort(arrays[0], 0, len(arrays[0])-1)

	print('\nThe merged and sorted array is :\n{}'.format(arrays[0]))

if __name__=="__main__":
	main()