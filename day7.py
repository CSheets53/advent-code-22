from collections import defaultdict
import re
import sys

terminal_output = []
with open("./inputs/d7.txt") as f:
    for line in f:
        terminal_output.append(line[:-1]) # cut \n

# build filesystem
dir_sizes = defaultdict(int)
current_path = []

for line in terminal_output:
    if line.startswith("$ cd"):
        # grab dir name
        dir = line.split()[-1]
        if dir == "..":
            # move back up
            current_path.pop()
        else:
            # move dirs
            if dir == '/':
                current_path.append("root")
            else:
                # move down
                current_path.append(dir)
    # check if line starts with a num
    elif re.match(r"^\d+", line):
        current_file_size = int(line.split()[0])
        
        # update the size for each contained dir
        for i in range(len(current_path)):
            dir_sizes['/'.join(current_path[:i+1])] += int(current_file_size)

def part1():
    # find all dirs with a total size <= 100,000
    total_sum = 0
    for dir, size in dir_sizes.items():
        if size <= 100_000:
            total_sum += size

    return total_sum

def part2():
    unused_space = 70_000_000 - dir_sizes["root"]
    space_to_delete = 30_000_000 - unused_space

    smallest_dir_size = sys.maxsize
    for dir, size in dir_sizes.items():
        if size >= space_to_delete and size < smallest_dir_size:
            smallest_dir_size = size

    return smallest_dir_size

#print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
