# get input
strategy_guide = []

with open("./inputs/d2.txt") as f:
    for line in f:
        strategy_guide.append(line[:-1]) # cut off \n

def part1():
    total_score = 0

    for play in strategy_guide:
        play_split = play.split(' ')
        opponent_move, player_move = play_split[0], play_split[1]

        if opponent_move == 'A' and player_move == 'X':
            # rock, rock
            total_score += 4 # 1 + 3
        elif opponent_move == 'A' and player_move == 'Y':
            # rock, paper
            total_score += 8 # 2 + 6
        elif opponent_move == 'A' and player_move == 'Z':
            # rock, scissors
            total_score += 3 # 3 + 0
        elif opponent_move == 'B' and player_move == 'X':
            # paper, rock
            total_score += 1 # 1 + 0
        elif opponent_move == 'B' and player_move == 'Y':
            # paper, paper
            total_score += 5 # 2 + 3
        elif opponent_move == 'B' and player_move == 'Z':
            # paper, scissors
            total_score += 9 # 3 + 6
        elif opponent_move == 'C' and player_move == 'X':
            # scissors, rock
            total_score += 7 # 1 + 6
        elif opponent_move == 'C' and player_move == 'Y':
            # scissors, paper
            total_score += 2 # 2 + 0
        elif opponent_move == 'C' and player_move == 'Z':
            # scissors, scissors
            total_score += 6 # 3 + 3

    return total_score

def part2():
    total_score = 0

    for play in strategy_guide:
        play_split = play.split(' ')
        opponent_move, player_move = play_split[0], play_split[1]

        if opponent_move == 'A' and player_move == 'X':
            # rock, scissors
            total_score += 3 # 3 + 0
        elif opponent_move == 'A' and player_move == 'Y':
            # rock, rock
            total_score += 4 # 1 + 3
        elif opponent_move == 'A' and player_move == 'Z':
            # rock, paper
            total_score += 8 # 2 + 6
        elif opponent_move == 'B' and player_move == 'X':
            # paper, rock
            total_score += 1 # 1 + 0
        elif opponent_move == 'B' and player_move == 'Y':
            # paper, paper
            total_score += 5 # 2 + 3
        elif opponent_move == 'B' and player_move == 'Z':
            # paper, scissors
            total_score += 9 # 3 + 6
        elif opponent_move == 'C' and player_move == 'X':
            # scissors, paper
            total_score += 2 # 2 + 0
        elif opponent_move == 'C' and player_move == 'Y':
            # scissors, scissors
            total_score += 6 # 3 + 3
        elif opponent_move == 'C' and player_move == 'Z':
            # scissors, rock
            total_score += 7 # 1 + 6

    return total_score

#print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
