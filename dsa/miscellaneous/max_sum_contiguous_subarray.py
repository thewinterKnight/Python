
def get_start_index(sum_map, curr_sum):
	new_start_indx = 0
	new_max_sum = curr_sum
	for k, v in sum_map.items():
		if curr_sum - v > new_max_sum:
			new_start_indx = k + 1
			new_max_sum = curr_sum - v

	return new_start_indx, new_max_sum


def fetch_max_subarray(arr):
	max_sum = -float("inf")		# keeps track of max subarray sum
	curr_sum = 0	# keeps track of sum from index 0
	curr_max_sum = 0	# keeps track of max running curr sum from index 0
	start_indx = 0	# keeps track of start index of subarray
	end_indx = 0	# keeps track of end index of array

	sum_map = {}	# dict to hold the index specific curr sum values

	for i in range(0, len(arr)):
		curr_sum += arr[i]

		if curr_sum > curr_max_sum:
			curr_max_sum = curr_sum
			end_indx = i
			new_start_indx, new_max_sum = get_start_index(sum_map, curr_sum)

		if new_max_sum > max_sum:
			max_sum = new_max_sum
			start_indx = new_start_indx

		sum_map[i] = curr_sum

	return max_sum, arr[start_indx:end_indx+1]


def main():
	print("Number of elements : ")
	n = int(input())

	arr = []
	print("Enter elements :")
	for i in range(0, n):
		arr.append(int(input()))

	max_subarray_sum, max_subarray = fetch_max_subarray(arr)
	print('Max subarray : {}\nSum : {}'.format(max_subarray_sum, max_subarray))


if __name__=="__main__":
	main()