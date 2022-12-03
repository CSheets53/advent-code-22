def part1() -> int:
    max_sum = -1
    current_sum = 0
    with open("./inputs/d1.txt") as f:
        for line in f:
            if line != "\n":
                current_sum += int(line)
            else:
                max_sum = max(max_sum, current_sum)
                current_sum = 0

    return max_sum

def part2() -> int:
    # keep the top 3 in a set
    max_sums = set()
    current_sum = 0
    with open("./inputs/d1.txt") as f:
        for line in f:
            if line != "\n":
                current_sum += int(line)
            else:
                # check if we need to add it to our top 3
                if len(max_sums) < 3:
                    max_sums.add(current_sum)
                else:
                    # always swap out the smallest
                    min_sum = min(max_sums)
                    if current_sum > min_sum:
                        max_sums.remove(min_sum)
                        max_sums.add(current_sum)
                
                current_sum = 0

    return sum(max_sums)

#print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")