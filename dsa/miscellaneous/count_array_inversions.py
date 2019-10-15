
def merge(larr, rarr):
	i=0
	j=0
	k=0
	merged_arr = []
	while i < len(larr) and j < len(rarr):
		if larr[i] <= rarr[j]:
			merged_arr.append(larr[i])
			i += 1
		else:
			merged_arr.append(rarr[j])
			j += 1

			global inversions
			inversions += (len(larr) - i)

	while i < len(larr):
		merged_arr.append(larr[i])
		i += 1
		# inversions += 1
	while j < len(rarr):
		merged_arr.append(rarr[j])
		j += 1

	return merged_arr


def merge_sort(arr):
	if len(arr) > 1:

		mid = int(len(arr)/2)

		larr = merge_sort(arr[:mid])
		rarr = merge_sort(arr[mid:])

		arr = merge(larr, rarr)

	return arr


def main():
    # print("Number of elements : ")
    # n = int(input())

    # arr = []
    # print("Enter elements :")
    # for i in range(0, n):
    #     arr.append(int(input()))

    arr = [2,6,4,9,5,8,4,1,3,5]
    # arr = [2,4,1,6,3,5]

    sorted_arr = merge_sort(arr)

    print('Input arr : {}\nSorted arr : {}\nNumber of inversions : {}'.format(arr, sorted_arr, inversions))
    # print('Input arr : {}\nSorted arr : {}'.format(arr, sorted_arr))


if __name__=="__main__":
	inversions = 0
	main()
