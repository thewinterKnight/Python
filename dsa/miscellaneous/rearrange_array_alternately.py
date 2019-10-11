import queue

def Partition(arr, start_indx, end_indx):
	initial_pivot_indx = end_indx
	pivot = arr[initial_pivot_indx]
	partition_indx = start_indx

	for i in range(start_indx, end_indx):
		if arr[i] < pivot:
			Swap(arr, i, partition_indx)
			partition_indx += 1

	Swap(arr, partition_indx, initial_pivot_indx)

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


def rearrange_alternately(arr):
	rearranged_arr = queue.LifoQueue()

	mid = int(len(arr)/2)

	print_directions = [0, 1] 
	if len(arr) % 2 == 0:
		mid -= 1
		curr_print_direction = print_directions[0]
	else:
		curr_print_direction = print_directions[1]

	jump_length = 0
	for i in range(0, len(arr)):
		if curr_print_direction == 0:	# direction = left
			rearranged_arr.put(arr[mid - jump_length])
		else:							# direction = right
			rearranged_arr.put(arr[mid + jump_length])

		curr_print_direction = (curr_print_direction + 1) % len(print_directions)

		if i % 2 == 0:
			jump_length += 1

	return rearranged_arr



def main():
	print("Number of elements : ")
	n = int(input())

	arr = []
	print("Enter elements :")
	for i in range(0, n):
		arr.append(int(input()))

	print("Enter sum value : ")
	sum = int(input())

	# arr = [10,20,30,40,50,60,70,80,90,100,110]
	QuickSort(arr, 0, len(arr)-1)

	print('\nSorted array : {}'.format(arr))

	rearranged_arr = rearrange_alternately(arr)

	while rearranged_arr.empty() is False:
		print(rearranged_arr.get())

if __name__=="__main__":
	main()