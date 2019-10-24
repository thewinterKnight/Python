def find_number_pair(arr, req_sum):
	remainder_map = [0] * (max(arr) - min(arr) + 1)

	pair = set()
	base_index = min(arr)
	for i in range(0, len(arr)):
		remainder_index = remainder_map[base_index + req_sum - arr[i]]
		
		if remainder_index != 0:
			pair.add((arr[i], req_sum - arr[i]))
		else:
			remainder_map[base_index + arr[i]] = 1

	return pair


def main():
	arr = [3,1,-5,8,-3,6,7,11,2,-14]
	print(find_number_pair(arr, 13))


if __name__=='__main__':
	main()