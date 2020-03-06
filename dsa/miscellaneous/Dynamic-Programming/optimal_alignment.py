
def compute_alignment_matrix(A, B):
	rows, cols = len(A) + 1, len(B) + 1
	D = [[0 for i in range(cols)] for j in range(rows)]

	for i in range(0, rows):
		D[i][0] = i
	for j in range(0, cols):
		D[0][j] = j

	for i in range(1, rows):
		for j in range(1, cols):
			insertion = D[i][j-1] + 1
			deletion = D[i-1][j] + 1
			mismatch = D[i-1][j-1] + 1
			match = D[i-1][j-1]

			if A[i-1] == B[j-1]:
				D[i][j] = min(insertion, deletion, match)
			else:
				D[i][j] = min(insertion, deletion, mismatch)

	print('Edit Distance is {}\n'.format(D[len(A)][len(B)]))
	return D


def find_optimal_alignent(D, A, B):
	rows, cols = len(A) + 1, len(B) + 1
	i = rows-1
	j = cols-1
	while i >= 0 and j >= 0:
		if i == 0 and j == 0:
			return

		if j > 0 and D[i][j] == D[i][j-1] + 1:		# insertion
			print('INSERT {}'.format(B[j-1]))
			j = j - 1
		elif i > 0 and D[i][j] == D[i-1][j] + 1:	# deletion
			print('DELETE {}\n'.format(A[i-1]))
			i = i - 1
		elif i > 0 and j > 0:
			if D[i][j] == D[i-1][j-1]:
				print('MATCH {}-{}\n'.format(A[i-1], B[j-1]))
			elif D[i][j] != D[i-1][j-1]:
				print('MISMATCH {}-{}\n'.format(A[i-1], B[j-1]))
			i = i - 1
			j = j - 1


if __name__=='__main__':
	A = 'EDITING'
	B = 'DISTANCE'

	# A = 'CAT'
	# B = 'CUT'

	D = compute_alignment_matrix(A, B)
	find_optimal_alignent(D, A, B)