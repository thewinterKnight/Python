import sys

def optimal_knapsack(W, w2v):
	knapsack = {}
	knapsack[0] = 0
	
	for partial_weight in range(1, W+1):
		knapsack[partial_weight] = -sys.maxsize - 1

		for w, v in w2v.items():
			if partial_weight >= w:
				value = v + knapsack[partial_weight - w]

				if value > knapsack[partial_weight]:
					knapsack[partial_weight] = value

	return knapsack[W]


if __name__=='__main__':
	W = 10
	w2v = {6:30, 3:14, 4:16, 2:9}

	print(optimal_knapsack(W, w2v))