

def quicksort(values, start, end, weights, costs):
	if start < end:
		pivot_index = Partition(values, start, end, weights, costs)

		quicksort(values, start, pivot_index-1, weights, costs)
		quicksort(values, pivot_index+1, end, weights, costs)


def Partition(values, start, end, weights, costs):
	pivot_index = end
	pivot_element = values[pivot_index]
	i = start-1
	for j in range(start, end):
		if values[j] > pivot_element:
			i += 1
			Swap(values, i, j)
			Swap(weights, i, j)
			Swap(costs, i, j)

	Swap(values, i+1, pivot_index)
	Swap(weights, i+1, pivot_index)
	Swap(costs, i+1, pivot_index)

	return i+1


def Swap(arr, index1, index2):
	temp = arr[index1]
	arr[index1] = arr[index2]
	arr[index2] = temp


def pack_knapsack(weights, costs, capacity):
	values = []
	for i in range(len(weights)):
		values.append(costs[i] / weights[i])

	# print('values : {}'.format(values))
	quicksort(values, 0, len(values)-1, weights, costs)
	# print('{}\n{}\n{}'.format(values, weights, costs))

	knapsack_item_weights = []
	knapsack_total_cost = 0
	unused_item_index = 0
	while capacity > 0:
		weight_picked_item = min(capacity, weights[unused_item_index])
		knapsack_item_weights.append(weight_picked_item)
		knapsack_total_cost += weight_picked_item * costs[unused_item_index]
		capacity -= weight_picked_item
		unused_item_index += 1

	return knapsack_total_cost, knapsack_item_weights


def main():
	weights = [4, 3, 2]
	costs = [5, 6, 7]
	capacity = 7

	total_cost, packed_item_weights = pack_knapsack(weights, costs, capacity)

	print(total_cost, packed_item_weights)


if __name__=='__main__':
	main()