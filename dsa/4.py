# How do you find duplicates from an array in place?
# How do you remove duplicates from an array (O(n) extra space)?

import random


def create_array(m, M, num_duplicates):
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


def find_duplicates_inplace1(arr):
	repeats = set([])

	for i in range(0, len(arr)):
		if arr[abs(arr[i])] > 0:
			arr[abs(arr[i])] = -arr[abs(arr[i])]
		elif arr[abs(arr[i])] < 0:
			repeats.add(abs(arr[i]))

	return repeats


def find_duplicates_inplace2(arr):
	repeats = []

	n = len(arr)
	for i in range(0, n):
		indx = arr[i] % n
		arr[indx] += n

	for i in range(0,n):
		if arr[i] / n > 2:
			repeats.append(i)

	return repeats


def remove_duplicates(arr):
	# list(filter(lambda a: a!= 2, arr))
	hash_mp = {i : 0 for i in arr}

	sifted_arr = []
	for item in arr:
		if hash_mp[item] == 0:
			hash_mp[item] += 1
			sifted_arr.append(item)

	return sifted_arr


if __name__ == "__main__":
	arr = create_array(0,7,4)
	print(arr)

	copy_arr = arr[:]
	# copy_arr = arr.copy()

	repeats = find_duplicates_inplace2(copy_arr)
	print('Repeats : ', repeats)

	sifted_arr = remove_duplicates(arr)
	print('Sifted array : ', sifted_arr)