# Quick Sort

import random

def create_array(m, M):
	arr = list(range(m, M+1))
	random.shuffle(arr)
	return arr


def create_array_wt_duplicates(m, M, num_duplicates):
	arr = list(range(m, M+1))

	# print(arr)

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

def quicksort(arr, start, end):
	if start < end:
		pivot_index = partition(arr, start, end)

		quicksort(arr, start, pivot_index-1)
		quicksort(arr, pivot_index+1, end)


def partition(arr, start, end):
	pivot = arr[end]

	i = start - 1

	for j in range(start, end):
		if arr[j] < pivot:
			i+=1
			swap(arr, i, j)

	swap(arr, i+1, end)
	return i+1 


def swap(arr, i1, i2):
	temp = arr[i1]
	arr[i1] = arr[i2]
	arr[i2] = temp


if __name__=="__main__":
	arr = create_array_wt_duplicates(0,7,3)

	print(arr)

	quicksort(arr, 0, len(arr)-1)

	print('sorting...\n', arr)