
def compute_edit_distance(A, B):
	rows, cols = (len(A) + 1, (len(B) + 1))

	D = [[0 for i in range(cols)] for j in range(rows)]

	for i in range(len(A)+1):
		D[i][0] = i

	# print_matrix(D)

	for j in range(len(B)+1):
		D[0][j] = j

	# print_matrix(D)

	for i in range(1, len(A)+1):
		for j in range(1, len(B)+1):
			insertion = D[i][j-1] + 1
			deletion = D[i-1][j] + 1
			mismatch = D[i-1][j-1] + 1
			match = D[i-1][j-1]

			if A[i-1] == B[j-1]:
				D[i][j] = min(insertion, deletion, match)
			else:
				D[i][j] = min(insertion, deletion, mismatch)

	# print_matrix(D)

	return D[len(A)][len(B)]


def print_matrix(D):
	for i in range(len(A)+1):
		for j in range(len(B)+1):
			print('{} '.format(D[i][j]))
		print('\n')


if __name__=='__main__':
	A = 'EDITING'
	B = 'DISTANCE'

	A = 'CAT'
	B = 'CUT'

	A = 'SUNDAY'
	B = 'SATURDAY'

	print(compute_edit_distance(A, B))
