import re

monkey_input = open("./inputs/d11.txt", 'r').read().split("\n\n")

class Monkey:
    def __init__(self, monkey_info: str):
        lines = monkey_info.splitlines()
        self.index = int(re.search(r"\d+", lines[0]).group())
        self.items = [int(x) for x in re.findall(r"\d+", lines[1])]
        self.operation = self.__setOperation(lines[2])
        self.test_divisor = int(re.search(r"\d+", lines[3]).group())
        self.true_throw = int(re.search(r"\d+", lines[4]).group())
        self.false_throw = int(re.search(r"\d+", lines[5]).group())
        self.num_inspected = 0

    def __setOperation(self, line: str):
        operator = ''
        start_ix = -1

        if '*' in line:
            start_ix = line.find('*')
            operator = '*'
        else:
            start_ix = line.find('+')
            operator = '+'

        relevant_info = line[start_ix:]
        if "old" in relevant_info:
            if operator == '*':
                return lambda old: int(old * old)
            
            return lambda old: old + old
        else:
            end_num = int(re.search(r"\d+", relevant_info).group())
            if operator == '*':
                return lambda old: int(old * end_num)
            
            return lambda old: old + end_num

def part1():
    monkeys = []
    for m in monkey_input:
        monkeys.append(Monkey(m))

    # 20 rounds
    for _ in range(20):
        for monkey in monkeys:
            while len(monkey.items) != 0:
                # inspect item
                current_item = monkey.items.pop(0)
                monkey.num_inspected += 1
                
                # increase worry level
                current_item = monkey.operation(current_item)

                # monkey gets bored
                current_item //= 3

                # test if divisible
                if current_item % monkey.test_divisor == 0:
                    monkeys[monkey.true_throw].items.append(current_item)
                else:
                    monkeys[monkey.false_throw].items.append(current_item)

    # find two most active monkeys
    active = sorted(monkeys, key=lambda x: x.num_inspected, reverse=True)[:2]

    return active[0].num_inspected * active[1].num_inspected

def part2():
    monkeys = []
    lcm_mod = 1
    for m in monkey_input:
        monkey = Monkey(m)
        monkeys.append(monkey)
        lcm_mod *= monkey.test_divisor

    # 10_000 rounds
    for _ in range(10000):
        for monkey in monkeys:
            while len(monkey.items) != 0:
                # inspect item
                current_item = monkey.items.pop(0)
                monkey.num_inspected += 1
                
                # increase worry level
                current_item = monkey.operation(current_item)

                # monkey gets bored
                current_item %= lcm_mod

                # test if divisible
                if current_item % monkey.test_divisor == 0:
                    monkeys[monkey.true_throw].items.append(current_item)
                else:
                    monkeys[monkey.false_throw].items.append(current_item)

    # find two most active monkeys
    active = sorted(monkeys, key=lambda x: x.num_inspected, reverse=True)[:2]

    return active[0].num_inspected * active[1].num_inspected

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
