def group_children(ages_arr, max_gap):
    min_indx = 0
    age_min = ages_arr[min_indx]
    all_groups = []

    while min_indx < len(ages_arr):
        age_max = min(age_min + max_gap, ages_arr[-1])
        min_indx = ages_arr.index(age_min)

        group = []
        while age_min <= age_max:
            if ages_arr[min_indx] == age_min:
                group.append(age_min)
                min_indx += 1
            age_min += 1

        all_groups.append(group)

        if min_indx >= len(ages_arr):
            return all_groups

        while age_min != ages_arr[min_indx]:
            age_min += 1


def main():
    children_ages = [5, 7, 8, 9, 11, 12]
    max_age_gap = 1
    print('Children ages : {}'.format(children_ages))

    groups = group_children(children_ages, max_age_gap)

    print('\nMinimum number of groups with age difference {} = {}'.format(max_age_gap, len(groups)))
    print('Groups : {}'.format(groups))


if __name__ == "__main__":
    main()
