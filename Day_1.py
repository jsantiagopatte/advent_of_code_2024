
# Two lists with location IDs.
# Sort the lists in ascending order and take the difference at each element.
# Add all distances to get solution.

if __name__ == '__main__':
    # Import txt file
    file = open('input_day1_part1.txt', 'r')
    # Save all lines into a list
    loc_list1 = []
    loc_list2 = []
    for line in file:
        locs = line.split()
        loc_list1.append(int(locs[0]))
        loc_list2.append(int(locs[1]))
    loc_list1_sorted = sorted(loc_list1)
    loc_list2_sorted = sorted(loc_list2)
    distance = 0
    for loc1, loc2 in zip(loc_list1_sorted, loc_list2_sorted):
        distance += abs(loc1 - loc2 )

    # Part 2
    sim_score = 0
    for loc1 in loc_list1:
        multiplier = 0
        for loc2 in loc_list2:
            if loc1 == loc2:
                multiplier += 1
        sim_score += loc1 * multiplier
    print(sim_score)
