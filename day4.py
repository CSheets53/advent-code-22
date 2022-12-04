assignment_pairs = []

with open("./inputs/d4.txt") as f:
    for line in f:
        assignment_pairs.append(line[:-1]) # cut \n

# assignment_pairs = [
#     '2-4,6-8',
# '2-3,4-5',
# '5-7,7-9',
# '2-8,3-7',
# '6-6,4-6',
# '2-6,4-8',
# ]

def part1():
    fully_contained_count = 0

    for pair in assignment_pairs:
        first, second = pair.split(',')[0], pair.split(',')[1]
        first_min, first_max = int(first.split('-')[0]), int(first.split('-')[1])
        second_min, second_max = int(second.split('-')[0]), int(second.split('-')[1])

        if first_min <= second_min:
            # second in first
            if second_max <= first_max or (first_min == second_min and first_max <= second_max):
                fully_contained_count += 1
        else:
            # first in second -- second_min <= first_min
            if first_max <= second_max:
                fully_contained_count += 1

    return fully_contained_count

def part2():
    overlap_count = 0

    for pair in assignment_pairs:
        first, second = pair.split(',')[0], pair.split(',')[1]
        first_min, first_max = int(first.split('-')[0]), int(first.split('-')[1])
        second_min, second_max = int(second.split('-')[0]), int(second.split('-')[1])

        if first_min >= second_min and first_min <= second_max:
            overlap_count += 1
        elif first_max >= second_min and first_max <= second_max:
            overlap_count += 1

        # check containment again
        elif first_min <= second_min:
            if second_max <= first_max or (first_min == second_min and first_max <= second_max):
                overlap_count += 1
        elif second_min <= first_min:
            if first_max <= second_max:
                overlap_count += 1

    return overlap_count

#print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")