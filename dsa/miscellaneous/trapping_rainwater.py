

def find_trapped_rainwater(arr):
	trapped_water = 0
	left_wall = arr[0]

	for index, wall_height in enumerate(arr[1:]):
		if index == len(arr[1:])-1:
			right_wall = wall_height
			if right_wall < left_wall:
				trapped_water -= (left_wall - right_wall) * (len(arr) - 2)
			break

		trapped_water += (left_wall - wall_height)

	return trapped_water


def main():
	tank_wall_arr = [4,0,0,2,0,3]

	print(find_trapped_rainwater(tank_wall_arr))



if __name__=="__main__":
	main()
