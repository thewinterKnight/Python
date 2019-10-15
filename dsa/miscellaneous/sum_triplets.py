

def fetch_sum_triplets(arr, req_sum):
	n = len(arr)

	s = {}
	# for i in range(0, n):
	# 	if arr[i] in s.keys():
	# 		s[arr[i]] += 1
	# 	else:
	# 		s[arr[i]] = 1

	triplets_count = 0
	triplets = set()
	for i in range(0, n-1):
		tertiary = arr[i]

		for j in range(i+1, n):
			residual = req_sum - (tertiary + arr[j])
			if residual in s.keys():
				triplets_count += 1
				triplets.add((tertiary, residual, arr[j]))
			else:
				s[arr[j]] = 1

	return triplets_count, list(triplets)


def fetch_sum_pairs(arr, req_sum):
	n = len(arr)
	s = {}

	pairs = set()
	pair_count = 0
	for i in range(0, n):
		if req_sum - arr[i] in s.keys():
			pair_count += 1
			pairs.add((arr[i], req_sum - arr[i]))
		else:
			s[arr[i]] = 1

	return pair_count, list(pairs)


if __name__=="__main__":
	print("Number of elements : ")
	n = int(input())

	arr = []
	print("Enter elements :")
	for i in range(0, n):
		arr.append(int(input()))

	print("Enter sum value : ")
	req_sum = int(input())

	pair_count, pairs = fetch_sum_pairs(arr, req_sum)
	print('{} pairs\n{}'.format(pair_count, pairs))