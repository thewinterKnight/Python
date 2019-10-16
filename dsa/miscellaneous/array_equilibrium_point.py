
def fetch_start_indx(sum_map, residual_sum):
	for k, v in sum_map.items():
		if k == residual_sum:
			return v
	return None


def find_sum_subarrays(arr, req_sum):
	sum_map = {}

	sum_subarrays = []
	curr_sum = 0
	for i in range(0, len(arr)):
		curr_sum += arr[i]

		if curr_sum == req_sum:
			sum_subarrays.append(arr[0:i+1])

		start_indx = fetch_start_indx(sum_map, curr_sum-req_sum)
		if start_indx is not None:
			sum_subarrays.append(arr[start_indx+1:i+1])

		sum_map[curr_sum] = i

	return sum_subarrays


def find_quilibrium_subarray(arr):
	sum_map = {}

	req_sum = 0
	curr_sum = 0
	running_sum = 0
	eq_arrays = []
	for i in range(0, len(arr)):
		curr_sum += arr[i]

		start_residual_sum = 0
		for j in range(0, i-1):
			start_residual_sum += arr[j]

			curr_subarray_sum = curr_sum - start_residual_sum
			if curr_subarray_sum % 2 == 0:
				req_sum = curr_subarray_sum / 2

				equilibrium_index = fetch_start_indx(sum_map, req_sum + start_residual_sum)
				if equilibrium_index is not None:
					eq_arrays.append((arr[j+1:i+1], equilibrium_index))

		sum_map[curr_sum] = i

	return eq_arrays



def main():
	# print("Number of elements : ")
	# n = int(input())

	# arr = []
	# print("Enter elements :")
	# for i in range(0, n):
	# 	arr.append(int(input()))

	# print("Enter sum value : ")
	# sum = int(input())
	# print('\nInput array : {}'.format(arr))

	arr = [6,2,6,-4,12,1,-6,9]
	subarray_sum = 4

	eq_arrays = find_quilibrium_subarray(arr)
	print(eq_arrays)



if __name__=="__main__":
	main()