motions = []

with open("./inputs/d9.txt") as f:
    for line in f:
        motions.append(line[:-1])

def part1():
    # start at 0, 0 and track all unique locations visited
    # go based off of standard coordinate system
    head_pos = [0, 0]
    tail_pos = [0, 0]
    unique_tail_visits = set([(tail_pos[0], tail_pos[1])])

    for motion in motions:
        direction, amt = motion.split()[0], int(motion.split()[1])

        for _ in range(amt):
            if direction == 'R':
                head_pos[0] += 1
            elif direction == 'U':
                head_pos[1] += 1
            elif direction == 'D':
                head_pos[1] -= 1
            else:
                head_pos[0] -= 1

            if abs(head_pos[0] - tail_pos[0]) + abs(head_pos[1] - tail_pos[1]) >= 3:
                # need to move one step diagonally
                if head_pos[0] > tail_pos[0] and head_pos[1] > tail_pos[1]:
                    tail_pos[0] += 1
                    tail_pos[1] += 1
                elif head_pos[0] < tail_pos[0] and head_pos[1] > tail_pos[1]:
                    tail_pos[0] -= 1
                    tail_pos[1] += 1
                elif head_pos[0] > tail_pos[0] and head_pos[1] < tail_pos[1]:
                    tail_pos[0] += 1
                    tail_pos[1] -= 1
                else:
                    tail_pos[0] -= 1
                    tail_pos[1] -= 1

            elif abs(head_pos[0] - tail_pos[0]) > 1 or abs(head_pos[1] - tail_pos[1]) > 1:
                # head is moving away normally
                if direction == 'R':
                    # TH
                    tail_pos[0] = head_pos[0] - 1
                    tail_pos[1] = head_pos[1]
                elif direction == 'U':
                    # H
                    # T
                    tail_pos[0] = head_pos[0]
                    tail_pos[1] = head_pos[1] - 1
                elif direction == 'D':
                    # T
                    # H
                    tail_pos[0] = head_pos[0]
                    tail_pos[1] = head_pos[1] + 1
                else:
                    # HT
                    tail_pos[0] = head_pos[0] + 1
                    tail_pos[1] = head_pos[1]

            unique_tail_visits.add((tail_pos[0], tail_pos[1]))

    return len(unique_tail_visits)

def part2():
    head_pos = [0, 0]
    # the final tail will be tail_pos[-1]
    all_tail_pos = [[0, 0] for _ in range(9)]
    unique_tail_visits = set([(all_tail_pos[-1][0], all_tail_pos[-1][1])])

    for motion in motions:
        direction, amt = motion.split()[0], int(motion.split()[1])

        for _ in range(amt):
            if direction == 'R':
                head_pos[0] += 1
            elif direction == 'U':
                head_pos[1] += 1
            elif direction == 'D':
                head_pos[1] -= 1
            else:
                head_pos[0] -= 1

            # update every segment
            current_head_pos = head_pos.copy()
            for segment_pos in all_tail_pos:
                if abs(current_head_pos[0] - segment_pos[0]) + abs(current_head_pos[1] - segment_pos[1]) >= 3:
                    # need to move one step diagonally
                    if current_head_pos[0] > segment_pos[0] and current_head_pos[1] > segment_pos[1]:
                        segment_pos[0] += 1
                        segment_pos[1] += 1
                    elif current_head_pos[0] < segment_pos[0] and current_head_pos[1] > segment_pos[1]:
                        segment_pos[0] -= 1
                        segment_pos[1] += 1
                    elif current_head_pos[0] > segment_pos[0] and current_head_pos[1] < segment_pos[1]:
                        segment_pos[0] += 1
                        segment_pos[1] -= 1
                    else:
                        segment_pos[0] -= 1
                        segment_pos[1] -= 1

                elif abs(current_head_pos[0] - segment_pos[0]) > 1 or abs(current_head_pos[1] - segment_pos[1]) > 1:
                    # move normally
                    if current_head_pos[0] > segment_pos[0] + 1:
                        segment_pos[0] = current_head_pos[0] - 1
                        segment_pos[1] = current_head_pos[1]
                    elif current_head_pos[1] > segment_pos[1] + 1:
                        segment_pos[0] = current_head_pos[0]
                        segment_pos[1] = current_head_pos[1] - 1
                    elif current_head_pos[1] < segment_pos[1] - 1:
                        segment_pos[0] = current_head_pos[0]
                        segment_pos[1] = current_head_pos[1] + 1
                    else:
                        segment_pos[0] = current_head_pos[0] + 1
                        segment_pos[1] = current_head_pos[1]
                
                current_head_pos = segment_pos.copy()

            unique_tail_visits.add((all_tail_pos[-1][0], all_tail_pos[-1][1]))

    return len(unique_tail_visits)

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
