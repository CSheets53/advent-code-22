terminal_output = []
with open("./inputs/d7.txt") as f:
    for line in f:
        terminal_output.append(line[:-1]) # cut \n

terminal_output = ["$ cd /",
"$ ls",
"dir a",
"14848514 b.txt",
"8504156 c.dat",
"dir d",
"$ cd a",
"$ ls",
"dir e",
"29116 f",
"2557 g",
"62596 h.lst",
"$ cd e",
"$ ls",
"584 i",
"$ cd ..",
"$ cd ..",
"$ cd d",
"$ ls",
"4060174 j",
"8033020 d.log",
"5626152 d.ext",
"7214296 k"]

def part1():
    return -1

def part2():
    return -1

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
