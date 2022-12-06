buffer = ""

with open("./inputs/d6.txt") as f:
    buffer = f.readline()[:-1] # cut \n

def part1():
    start = 0
    # start at fourth char
    for last in range(4, len(buffer)):
        packet = buffer[start:last]

        seen = set()
        # check uniqueness
        for char in packet:
            if char in seen: 
                break
            else:
                seen.add(char)

        if len(seen) == 4:
            return last
        
        start += 1

    return -1

def part2():
    start = 0
    # start at fourteenth char
    for last in range(14, len(buffer)):
        packet = buffer[start:last]

        seen = set()
        # check uniqueness
        for char in packet:
            if char in seen: 
                break
            else:
                seen.add(char)

        if len(seen) == 14:
            return last
        
        start += 1

    return -1

#print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
