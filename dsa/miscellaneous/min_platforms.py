

def Swap(arr, indx1, indx2):
	temp = arr[indx1]
	arr[indx1] = arr[indx2]
	arr[indx2] = temp


def Partition(arr, start, end):
	pivot_index = end
	pivot_element = arr[pivot_index]

	i = start-1
	for j in range(start, end):
		if arr[j] < pivot_element:
			i += 1
			Swap(arr, i, j)

	Swap(arr, i+1, pivot_index)
	return i+1


def quicksort(arr, start, end):
	if start < end:
		pivot_index = Partition(arr, start, end)
		quicksort(arr, start, pivot_index-1)
		quicksort(arr, pivot_index+1, end)


def find_min_platforms_hash(arrivals, departures):
	clash_map = [0] * ((max(departures) - min(arrivals))/10 + 1)
	start_time = min(arrivals)
	max_clash_start = 0
	max_clash_end = 0
	max_clash = 0
	for train_index in range(0, len(arrivals)):
		for time_index in range(arrivals[train_index], departures[train_index] + 10, 10):
			map_slot = (time_index - start_time)/10 
			clash_map[map_slot]	+= 1

			if clash_map[map_slot] > max_clash:
				max_clash = clash_map[map_slot]
				max_clash_start = map_slot * 10 + start_time
			elif clash_map[map_slot] == max_clash:
				max_clash_end = map_slot * 10 + start_time


	return max(clash_map), (max_clash_start, max_clash_end)


def find_min_platforms_optimal(arrivals, departures):
	arrival_index = 0
	departure_index = 0
	trains_at_platform = 0
	max_trains_at_platform = 0
	max_start_time = 0
	max_end_time = 0
	for time_index in range(min(arrivals), max(departures) + 1):
		if arrival_index < len(arrivals) and time_index == arrivals[arrival_index]:
			trains_at_platform += 1
			# print('Arrival : {},{},{}'.format(arrival_index, arrivals[arrival_index], trains_at_platform))
			arrival_index += 1
		elif departure_index < len(departures) and time_index == departures[departure_index]:
			trains_at_platform -= 1
			# print('Departure : {},{},{}'.format(departure_index, departures[departure_index], trains_at_platform))
			departure_index += 1

		if trains_at_platform > max_trains_at_platform:
			max_trains_at_platform = trains_at_platform
			max_start_time = time_index
		elif trains_at_platform == max_trains_at_platform:
			max_end_time = time_index

	return max_trains_at_platform, (max_start_time, max_end_time)



def main():
	# print('Enter number of trains : ')
	# num_trains = int(input())

	# arrivals = []
	# departures = []
	# for i in range(0, num_trains):
	# 	print('Enter Arrival of train {}'.format(i+1))
	# 	arrivals.append(int(input()))

	# 	print('Enter Departure of train {}'.format(i+1))
	# 	departures.append(int(input()))

	# min_platforms, busiest_timings = find_min_platforms_optimal(arrivals, departures)

	arrivals = [900, 940, 950, 1100, 1500, 1800]
	departures = [910, 1200, 1120, 1130, 1900, 2000]

	print('\nHASHING solution...')
	min_platforms, busiest_timings = find_min_platforms_hash(arrivals, departures)
	print('\nMinimum number of platforms required : {}\nBusiest Timings : {}'.format(min_platforms, busiest_timings))

	print('\nOPTIMAL solution...')
	quicksort(arrivals, 0, len(arrivals)-1)
	quicksort(departures, 0, len(departures)-1)
	min_platforms, busiest_timings = find_min_platforms_optimal(arrivals, departures)
	print('Minimum number of platforms required : {}\nBusiest Timings : {}'.format(min_platforms, busiest_timings))


if __name__=="__main__":
	main()