def collate_columns(arr):
	num_rows = len(arr)
	num_cols = len(arr[0])

	cols = []
	for col_index in range(num_cols):
		col = []
		for row in arr:
			col.append(row[col_index])
		cols.append(col)

	return cols


def max_goldmines(arr):
	cols = collate_columns(arr)

	max_path = []
	max_mines = 0
	max_mines += max(cols[0])
	prev_row = cols[0].index(max(cols[0]))
	max_path.append((prev_row, 0))

	for i in range(1, len(cols)):
		right_up_index = max(0, prev_row-1)
		right_down_index = min(len(arr), prev_row+2)

		max_mines += max(cols[i][right_up_index:right_down_index])
		max_row = cols[i].index(max(cols[i][right_up_index:right_down_index]))

		prev_row = max_row
		max_path.append((max_row, i))

	return max_mines, max_path




def main():
	goldmine_arr = [[1, 3, 9],
					[2, 1, 4],
					[0, 6, 4],
					[5, 2, 3]]

	# goldmine_arr = [[10, 33, 13, 15],
 #                  	[22, 21, 4, 1],
 #                  	[5, 0, 2, 3],
 #                  	[0, 6, 14, 2]]

	for row in goldmine_arr:
		print('{}'.format(row))		

	max_mines, max_path = max_goldmines(goldmine_arr)
	print('\nMax mines : {}\nMiner\'s path : {}'.format(max_mines, max_path))


if __name__=='__main__':
	main()