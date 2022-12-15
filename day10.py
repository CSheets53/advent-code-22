program = open("./inputs/d10.txt", 'r').read().splitlines()

def part1():
    program_copy = program.copy()
    X = 1
    valid_cycles = [20, 60, 100, 140, 180, 220]

    cycle = 1
    signal_strength_sum = 0
    wait_cycle = False
    while cycle <= 220:
        # during cycle
        if cycle in valid_cycles:
            signal_strength_sum += cycle * X

        # after cycle
        if wait_cycle:
            # we waited a cycle
            X += int(program_copy[0].split()[1])
            program_copy.pop(0)
            wait_cycle = False
        else:
            if program_copy[0] != "noop":
                wait_cycle = True
            else:
                program_copy.pop(0)

        cycle += 1

    return signal_strength_sum

def part2():
    program_copy = program.copy()
    X = 1 # also the middle of the sprite
    display = ""

    wrap_cycles = [40, 80, 120, 160, 200, 240]
    cycle = 1
    crt_pos = 0
    wait_cycle = False
    while cycle <= 240:
        # during cycle - draw pixel
        if crt_pos > 39:
            crt_pos %= 40

        if X - 1 == crt_pos or X == crt_pos or X + 1 == crt_pos:
            display += '#'
        else:
            display += '.'

        # after cycle
        if wait_cycle:
            X += int(program_copy[0].split()[1])
            program_copy.pop(0)
            wait_cycle = False
        else:
            if program_copy[0] != "noop":
                wait_cycle = True
            else:
                program_copy.pop(0)

        if cycle in wrap_cycles:
            display += '\n'

        cycle += 1
        crt_pos += 1

    return display

print(f"Part 1: {part1()}")
print(f"Part 2:\n{part2()}")
