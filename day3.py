all_rucksacks = []

with open("./inputs/d3.txt") as f:
    for line in f:
        all_rucksacks.append(line[:-1]) # cut \n

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def part1():
    priority_sum = 0

    for sack in all_rucksacks:
        mid = len(sack) // 2

        # make the compartments sets to find intersection
        compartment1, compartment2 = set(sack[:mid]), set(sack[mid:])
        shared_item = compartment1.intersection(compartment2).pop()
        priority_sum += alphabet.index(shared_item) + 1 # add 1 to offset 0-start

    return priority_sum

def part2():
    priority_sum = 0
    for i in range(0, len(all_rucksacks), 3):
        shared_item = set(all_rucksacks[i]).intersection(set(all_rucksacks[i + 1]), set(all_rucksacks[i + 2])).pop()
        priority_sum += alphabet.index(shared_item) + 1
    
    return priority_sum

#print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
