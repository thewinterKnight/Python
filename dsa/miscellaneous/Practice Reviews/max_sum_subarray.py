import math


def fetch_start_index(sum_map, curr_sum):
	new_max_sum = curr_sum
	new_start_index = 0
	for k, v in sum_map.items():
		if curr_sum - v > new_max_sum:
			new_max_sum = curr_sum - v
			new_start_index = k + 1

	return new_max_sum, new_start_index


def max_sum_subarray_method_1(arr):
	sum_map = {}

	curr_sum = 0
	curr_max_sum = 0
	start_index = 0
	end_index = 0
	max_sum = -math.inf
	fetched_max_sum = 0
	new_start_index = 0
	for i in range(0, len(arr)):
		curr_sum += arr[i]

		if curr_sum > curr_max_sum:
			curr_max_sum = curr_sum
			end_index = i
			fetched_max_sum, new_start_index = fetch_start_index(sum_map, curr_sum)

		if fetched_max_sum > max_sum:
			max_sum = fetched_max_sum
			start_index = new_start_index

		sum_map[i] = curr_sum

	return max_sum, arr[start_index:end_index+1]


def kadanes_max_sum_subarray(arr):
	max_sum = 0
	max_till_now = 0
	start_index = 0
	end_index = 0
	for i in range(0, len(arr)):
		if max_till_now == 0:
			start_index = i
		max_till_now += arr[i]
		if max_till_now < 0:
			max_till_now = 0
		elif max_till_now > max_sum:
			max_sum = max_till_now
			end_index = i

	return max_sum, arr[start_index:end_index+1]



def main():
	arr = [2,-3,1,-5,4,8,-3,-1,8,-7,10,1,6,-9]

	max_subarray_sum, max_subarray = max_sum_subarray_method_1(arr)
	print('Max subarray : {}\nSubArray : {}'.format(max_subarray_sum, max_subarray))

	max_subarray_sum, max_subarray = kadanes_max_sum_subarray(arr)
	print('\nKadane\'s Algorithm...\nMax Sum output : {}\nSubArray : {}'.format(max_subarray_sum, max_subarray))


if __name__=="__main__":
	main()
	