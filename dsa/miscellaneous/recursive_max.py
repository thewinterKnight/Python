

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
	else:
		return fetch_max_2(arr[1:])


def main():
	array = [1,4,2,6,3,9,6,13,10,7,11,2]
	print(fetch_max_2(array))


if __name__=='__main__':
	main()