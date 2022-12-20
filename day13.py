import json

all_packet_strs = open("./inputs/d13.txt", 'r').read().splitlines()

all_packets = []
for packet in all_packet_strs:
    if packet != '':
        all_packets.append(json.loads(packet))

def is_right_order(left, right) -> int:
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return 1
        elif right < left:
            return 0
        else:
            return 2 # keep going
    elif isinstance(left, list) and isinstance(right, list):
        # loop over each item in both lists
        i = 0
        while i < max(len(left), len(right)):
            if i >= len(left):
                return 1
            elif i >= len(right):
                return 0

            result = is_right_order(left[i], right[i])
            if result != 2 or (i == len(left) - 1 and i == len(right) - 1):
                return result

            i += 1

        return 0
    else:
        # only one value is an int
        if isinstance(left, int):
            return is_right_order([left], right)
    
        return is_right_order(left, [right])

def part1():
    index_sum = 0

    pair_ix = 1
    for i in range(0, len(all_packets), 2):
        left = all_packets[i]
        right = all_packets[i + 1]

        if is_right_order(left, right):
            index_sum += pair_ix

        pair_ix += 1

    return index_sum

def part2():
    all_packets.append([[2]])
    all_packets.append([[6]])

    # use a bubble sort
    n = len(all_packets)
    swapped = False

    for i in range(n - 1):
        for j in range(n - i - 1):
            # check if j is not less than j + 1
            if not is_right_order(all_packets[j], all_packets[j + 1]):
                swapped = True
                all_packets[j], all_packets[j + 1] = all_packets[j + 1], all_packets[j]

        if not swapped:
            break

    return (all_packets.index([[2]]) + 1) * (all_packets.index([[6]]) + 1)

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
