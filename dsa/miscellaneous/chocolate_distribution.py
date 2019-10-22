

def quicksort(arr, start, end):
	if start < end:
		pivot_index = Partition(arr, start, end)

		quicksort(arr, start, pivot_index-1)
		quicksort(arr, pivot_index+1, end)


def Partition(arr, start, end):
	pivot_index = end
	pivot_element = arr[pivot_index]
	i = start - 1
	for j in range(start, end):
		if arr[j] < pivot_element:
			i += 1
			Swap(arr, j, i)

	Swap(arr, i+1, pivot_index)
	return i + 1


def Swap(arr, index1, index2):
	temp = arr[index1]
	arr[index1] = arr[index2]
	arr[index2] = temp



def chocolate_distribution(arr, num_children):
	quicksort(arr, 0, len(arr)-1)

	import math
	min_diff = math.inf

	for i in range(len(arr)-num_children+1):
		if arr[i+num_children-1] - arr[i] < min_diff:
			min_diff = arr[i+num_children-1] - arr[i]

	print('Min difference : {}'.format(min_diff))


def main():
	# chocolate_array = [12, 4, 7, 9, 2, 23, 25, 41,
						# 30, 40, 28, 42, 30, 44, 48, 43, 50]

	# num_children = 7

	# chocolate_array= [3, 4, 1, 9, 56, 7, 9, 12]
	# num_children = 5

	chocolate_array= [7, 3, 2, 4, 9, 12, 56]
	num_children = 3

	chocolate_distribution(chocolate_array, num_children)


if __name__=="__main__":
	main()