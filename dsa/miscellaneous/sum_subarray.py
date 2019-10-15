

def fetch_subarray(arr, n):
	temp_sum = arr[0]
	start_indx = 0

	for i in range(1, len(arr) + 1):
		if i < len(arr):
			temp_sum += arr[i]

		if temp_sum == n:
			print(arr[start_indx:i+1])

		while temp_sum > n:
			temp_sum -= arr[start_indx]
			start_indx += 1



if __name__=="__main__":
	print("Number of elements : ")
	n = int(input())

	arr = []
	print("Enter elements :")
	for i in range(0, n):
		arr.append(int(input()))

	print("Enter sum value : ")
	sum = int(input())

	fetch_subarray(arr, sum)