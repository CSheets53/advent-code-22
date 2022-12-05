from copy import deepcopy

# I think the stacks are small enough and too tricky that manually inputting would be easier than figuring out parsing
"""
                [M]     [V]     [L]
[G]             [V] [C] [G]     [D]
[J]             [Q] [W] [Z] [C] [J]
[W]         [W] [G] [V] [D] [G] [C]
[R]     [G] [N] [B] [D] [C] [M] [W]
[F] [M] [H] [C] [S] [T] [N] [N] [N]
[T] [W] [N] [R] [F] [R] [B] [J] [P]
[Z] [G] [J] [J] [W] [S] [H] [S] [G]
 1   2   3   4   5   6   7   8   9 
"""

stack1 = ['G', 'J', 'W', 'R', 'F', 'T', 'Z']
stack2 = ['M', 'W', 'G']
stack3 = ['G', 'H', 'N', 'J']
stack4 = ['W', 'N', 'C', 'R', 'J']
stack5 = ['M', 'V', 'Q', 'G', 'B', 'S', 'F', 'W']
stack6 = ['C', 'W', 'V', 'D', 'T', 'R', 'S']
stack7 = ['V', 'G', 'Z', 'D', 'C', 'N', 'B', 'H']
stack8 = ['C', 'G', 'M', 'N', 'J', 'S']
stack9 = ['L', 'D', 'J', 'C', 'W', 'N', 'P', 'G']
stacks = [stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9]

instructions = []
with open("./inputs/d5.txt") as f:
    for line in f:
        instructions.append(line[:-1]) # cut \n

def part1():
    p1_stacks = deepcopy(stacks)

    for instruction in instructions:
        split = instruction.split(" from ")
        
        # need to split again for double digit num
        num_to_move = int(split[0].split(' ')[1])

        # will be single digits
        origin = int(split[1][0]) - 1 # subtract one for indices
        destination = int(split[1][-1]) - 1

        for i in range(num_to_move):
            removed = p1_stacks[origin].pop(0)
            p1_stacks[destination].insert(0, removed)

    top_stacks = ''.join([stack[0] for stack in p1_stacks])
    return top_stacks

def part2():
    p2_stacks = deepcopy(stacks)

    for instruction in instructions:
        split = instruction.split(" from ")
        
        # need to split again for double digit num
        num_to_move = int(split[0].split(' ')[1])

        # will be single digits
        origin = int(split[1][0]) - 1 # subtract one for indices
        destination = int(split[1][-1]) - 1

        # move in chunks
        removed = []
        for i in range(num_to_move):
            removed.insert(0, p2_stacks[origin].pop(0))
            
        for item in removed:
            p2_stacks[destination].insert(0, item)

    #print([stack for stack in p2_stacks])
    top_stacks = ''.join([stack[0] for stack in p2_stacks])
    return top_stacks

#print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
