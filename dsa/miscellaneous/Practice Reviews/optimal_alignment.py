import sys

def compute_edit_distance(A, B):
	rows = len(A) + 1
	cols = len(B) + 1
	D = [[0 for i in range(cols)] for j in range(rows)]

	for i in range(rows):
		D[i][0] = i
	for j in range(cols):
		D[0][j] = j

	for i in range(1, rows):
		for j in range(1, cols):
			insertion = D[i][j-1] + 1
			deletion = D[i-1][j] + 1
			mismatch = D[i-1][j-1] + 1
			match = D[i-1][j-1]

			if A[i-1] == B[j-1]:
				D[i][j] = min((insertion, deletion, match))
			else:
				D[i][j] = min((insertion, deletion, mismatch))

	print('Edit Distance between strings : {}'.format(D[rows-1][cols-1]))
	return D


def find_optimal_alignment(A, B, D):
	i = len(A)
	j = len(B)

	while i >= 0:
		while j >= 0:
			if i == 0 and j == 0:
				return;

			if D[i][j] == 1 + D[i][j-1]:		# insertion
				print('INSERT {}'.format(B[j-1]))
				j -= 1
			elif D[i][j] == 1 + D[i-1][j]:		# deletion
				print('DELETE {}'.format(A[i-1]))
				i -= 1
			else:
				if D[i][j] == 1 + D[i-1][j-1]:	# mismatch
					print('MISMATCH {} {}'.format(A[i-1], B[j-1]))
				elif D[i][j] == D[i-1][j-1]:		# match
					print('MATCH {}'.format(A[i-1]))
				i -= 1
				j -= 1
			


if __name__=='__main__':
	# A = 'EDITING'
	# B = 'DISTANCE'

	A = 'CUT'
	B = 'CAT'

	D = compute_edit_distance(A, B)
	find_optimal_alignment(A, B, D)