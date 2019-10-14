import random


def count_min_refills(dist, filling_stations, max_gap):
    num_refills = 0
    curr_stop = 0
    refill_stations = []

    while curr_stop < dist:
        filling_station_residual_dist = 0

        if curr_stop + max_gap >= dist:
            print('\nJourney Completed !!')
            return num_refills, refill_stations

        refill_possibility = False
        while filling_station_residual_dist < max_gap:
            if curr_stop + max_gap - filling_station_residual_dist in filling_stations:
                num_refills += 1
                curr_stop += max_gap - filling_station_residual_dist
                refill_stations.append(curr_stop)
                refill_possibility = True
                break
            filling_station_residual_dist += 1

        if refill_possibility is False:
            print('\nIMPOSSIBLE to complete journey')
            break

    return num_refills, refill_stations


def main():
    total_dist = 950
    filling_stations = [0, 200, 375, 550, 785, 950]

    max_distance_until_next_refill = 400

    num_min_refills, refill_stations = count_min_refills(total_dist, filling_stations, max_distance_until_next_refill)
    print('Num refills : {}'.format(num_min_refills))
    print('Refills at : {}'.format(refill_stations))


if __name__=="__main__":
    main()
