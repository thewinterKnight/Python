

def fetch_max_1(arr):
	if len(arr) == 1:
		return arr[-1]

	if arr[0] > arr[-1]:
		arr[-1] = arr[0]

	return fetch_max_1(arr[1:])


def fetch_max_2(arr):
	if len(arr) == 1:
		return arr[0]

	if arr[0] > arr[-1]:
		return fetch_max_2(arr[:-1])
	return fetch_max_2(arr[1:])


def fetch_max_3(arr):
	if len(arr) == 1:
		return arr[0]

	max_val = fetch_max_3(arr[1:])

	if arr[0] > max_val:
		return arr[0]
	return max_val	


def main():
	array = [1,4,2,6,3,9,6,13,10,7,11,2]
	print(fetch_max_3(array))


if __name__=='__main__':
	main()