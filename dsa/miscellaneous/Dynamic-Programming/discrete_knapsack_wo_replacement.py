
def dict2lists(w2v):
	keys, vals = [], []
	for k, v in w2v.items():
		keys.append(k)
		vals.append(v)

	return keys, vals


def optimal_knapsack(W, w2v):
	n = len(w2v)
	weights, values = dict2lists(w2v)

	rows, cols = n+1, W+1
	knapsack = [[0 for j in range(cols)] for i in range(rows)]

	for i in range(1, rows):
		w_i = weights[i-1]
		v_i = values[i-1]
		
		for w in range(1, cols):
			knapsack[i][w] = knapsack[i-1][w]
			if w >= w_i:
				knapsack[i][w] = max(v_i + knapsack[i-1][w-w_i], knapsack[i-1][w])

	return knapsack[n][W], knapsack


if __name__=='__main__':
	W = 10
	w2v = {6:30, 3:14, 4:16, 2:9}

	max_value, _ = optimal_knapsack(W, w2v)

	print('{}\n\n'.format(max_value))
	# print(knapsack)