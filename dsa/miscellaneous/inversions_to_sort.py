
# def merge(larr, rarr, arr):
# 	global inversion_count

# 	i = 0
# 	j = 0
# 	while i < len(larr) and j < len(rarr):
# 		if larr[i] <= rarr[j]:
# 			arr.append(larr[i])
# 			i += 1

# 			if i > j:
# 				inversion_count += 1 
# 		else:
# 			arr.append(rarr[j])
# 			j += 1

# 			if j > i:
# 				inversion_count += 1

# 	while i < len(larr):
# 		arr.append(larr[i])
# 		i += 1

# 	while j < len(rarr):
# 		arr.append(rarr[j])
# 		j += 1


# def merge_sort(arr):
# 	if len(arr) < 2:
# 		return

# 	mid = int(len(arr)/2)
# 	larr = arr[:mid]
# 	rarr = arr[mid+1:]

# 	merge_sort(larr)
# 	merge_sort(rarr)

# 	merge(larr, rarr, arr)

def merge(arr, l, m, r):
    global inversion_count

    n1 = m - l + 1
    n2 = r- m 
  
    # create temp arrays 
    L = [0] * (n1) 
    R = [0] * (n2) 
  
    # Copy data to temp arrays L[] and R[] 
    for i in range(0 , n1): 
        L[i] = arr[l + i] 
  
    for j in range(0 , n2): 
        R[j] = arr[m + 1 + j] 
  
    # Merge the temp arrays back into arr[l..r] 
    i = 0     # Initial index of first subarray 
    j = 0     # Initial index of second subarray 
    k = l     # Initial index of merged subarray 
  
    while i < n1 and j < n2 : 
        if L[i] <= R[j]: 
            arr[k] = L[i] 
            i += 1
        else: 
            arr[k] = R[j] 
            j += 1

            inversion_count += n1 - i
        k += 1
  
    # Copy the remaining elements of L[], if there 
    # are any 
    while i < n1: 
        arr[k] = L[i] 
        i += 1
        k += 1
  
    # Copy the remaining elements of R[], if there 
    # are any 
    while j < n2: 
        arr[k] = R[j] 
        j += 1
        k += 1
  
# l is for left index and r is right index of the 
# sub-array of arr to be sorted 
def mergeSort(arr,l,r): 
    if l < r: 
  
        # Same as (l+r)/2, but avoids overflow for 
        # large l and h 
        m = int((l+(r-1))/2)
  
        # Sort first and second halves 
        mergeSort(arr, l, m) 
        mergeSort(arr, m+1, r) 
        merge(arr, l, m, r) 
  
  
# Driver code to test above 
inversion_count = 0

# arr = [2,6,4,9,5,8,4,1,3,5]
arr = [2,4,1,6,3,5]
n = len(arr) 
print ("Given array is") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
mergeSort(arr,0,n-1) 
print ("\n\nSorted array is") 
for i in range(n): 
    print ("%d" %arr[i])


print('Inversion Count to sort : {}'.format(inversion_count))



# def main():
#     # print("Number of elements : ")
#     # n = int(input())

#     # arr = []
#     # print("Enter elements :")
#     # for i in range(0, n):
#     #     arr.append(int(input()))

#     input_arr = [2,6,4,9,5,8,4,1,3,5]
#     import copy
#     arr = copy.deepcopy(input_arr)     # 1->3, 2->0, 3->4, 4->2, 5->5, 6->1
#     # arr = [2,4,1,3,5]       # 1->2, 2->0, 3->3, 4->1, 5->4

#     merge_sort(arr)

#     print("Input arr : {}\nNum inversions to sort : {}\nSorted arr : {}".format(input_arr, inversion_count, arr))


# if __name__=="__main__":
# 	sorted_arr = []
# 	inversion_count = 0
# 	main()