# How do you find all pairs of an integer array whose sum is equal to a given number?
# How do you remove duplicates from an array in place?

import random

def create_array(m, M):
	arr = list(range(m, M+1))
	random.shuffle(arr)
	return arr


def create_array_wt_duplicates(m, M, num_duplicates):
	arr = list(range(m, M+1))

	print(arr)

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


def merge(larr, rarr):
	sorted_arr = []

	i = 0; j = 0
	while i < len(larr) and j < len(rarr):
		if larr[i] <= rarr[j]:
			sorted_arr.append(larr[i])
			i+=1
		else:
			sorted_arr.append(rarr[j])
			j+=1

	while i < len(larr):
		sorted_arr.append(larr[i])
		i+=1

	while j < len(rarr):
		sorted_arr.append(rarr[j])
		j+=1

	return sorted_arr


def merge_sort(arr):
	if len(arr) < 2:
		return arr

	mid = int((len(arr) + 1)/ 2)
	larr = arr[:mid]
	rarr = arr[mid:]

	larr = merge_sort(larr)
	rarr = merge_sort(rarr)

	sorted_arr = merge(larr, rarr)

	return sorted_arr


def remove_duplicates_sorted_inplace(arr):
	if len(arr) < 1:
		return arr

	j=0

	for i in range(0, len(arr)-1):
		if arr[i] != arr[i+1]:
			arr[j] = arr[i]
			j += 1

	arr[j] = arr[len(arr)-1]

	return arr[:j+1]


def find_sum_pairs(arr, num):
	sorted_arr = merge_sort(arr)

	i = 0; j = len(arr)-1

	sum_pairs = []
	while j >= i:
		if sorted_arr[i] + sorted_arr[j] == num:
			sum_pairs.append((sorted_arr[i], sorted_arr[j]))
			i+=1;j-=1
		elif sorted_arr[i] + sorted_arr[j] < num:
			i+=1
		else:
			j-=1

	return sum_pairs


if __name__ == "__main__":
	# arr = create_array(5,23)
	arr = create_array_wt_duplicates(0,7,3)
	print(arr)

	sorted_arr = merge_sort(arr)
	print('Sorted Array : ', sorted_arr)

	sum_pairs = find_sum_pairs(arr, 12)
	print('Sum pairs : ', sum_pairs)

	sifted_arr = remove_duplicates_sorted_inplace(sorted_arr)
	print('Sifted Array : ', sifted_arr)