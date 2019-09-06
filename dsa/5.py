# How do you reverse an array in place in Java? 

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


def reverse_array(arr):
	i=0; j=len(arr)-1

	while(i <= j):
		temp = arr[i]
		arr[i] = arr[j]
		arr[j] = temp
		i+=1; j-=1

	return arr


if __name__=="__main__":
	arr = create_array_wt_duplicates(0,7,3)

	reverse = reverse_array(arr[:])
	
	print(arr, '\n', reverse)