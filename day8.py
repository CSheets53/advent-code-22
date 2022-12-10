tree_grid = []

with open("./inputs/d8.txt") as f:
    for line in f:
        tree_grid.append([int(x) for x in line[:-1]]) # cut \n

num_rows = len(tree_grid)
num_cols = len(tree_grid[0])

def part1():
    # count all the border trees
    num_visible = (num_rows * 2) + ((num_cols - 2) * 2)

    # only look at inner set
    for i in range(1, num_rows - 1):
        for j in range(1, num_cols - 1):
            current_tree = tree_grid[i][j]
            is_visible = False

            if tree_grid[i][j - 1] < current_tree:
                # go all the way left
                current_j = j - 1
                seen_path = True
                while current_j >= 0:
                    if tree_grid[i][current_j] >= current_tree:
                        seen_path = False
                        break

                    current_j -= 1
                
                is_visible = seen_path

            # check not visibles to avoid double looking
            if not is_visible and tree_grid[i][j + 1] < current_tree:
                # go all the way right
                current_j = j + 1
                seen_path = True
                while current_j < num_cols:
                    if tree_grid[i][current_j] >= current_tree:
                        seen_path = False
                        break

                    current_j += 1

                is_visible = seen_path

            if not is_visible and tree_grid[i - 1][j] < current_tree:
                # go all the way up
                current_i = i - 1
                seen_path = True
                while current_i >= 0:
                    if tree_grid[current_i][j] >= current_tree:
                        seen_path = False
                        break

                    current_i -= 1

                is_visible = seen_path

            if not is_visible and tree_grid[i + 1][j] < current_tree:
                # go all the way down
                current_i = i + 1
                seen_path = True
                while current_i < num_rows:
                    if tree_grid[current_i][j] >= current_tree:
                        seen_path = False
                        break

                    current_i += 1

                is_visible = seen_path

            if is_visible: 
                num_visible += 1

    return num_visible

def part2():
    max_scenic_score = 0

    # only look at inner set
    for i in range(1, num_rows - 1):
        for j in range(1, num_cols - 1):
            current_tree = tree_grid[i][j]

            # start each view at 1 - it will always see the neighboring tree
            left_view = 1
            if tree_grid[i][j - 1] < current_tree:
                # go all the way left
                current_j = j - 2
                while current_j >= 0:
                    left_view += 1

                    if tree_grid[i][current_j] >= current_tree:
                        break

                    current_j -= 1

            right_view = 1
            if tree_grid[i][j + 1] < current_tree:
                # go all the way right
                current_j = j + 2
                while current_j < num_cols:
                    right_view += 1

                    if tree_grid[i][current_j] >= current_tree:
                        break

                    current_j += 1

            up_view = 1
            if tree_grid[i - 1][j] < current_tree:
                # go all the way up
                current_i = i - 2
                while current_i >= 0:
                    up_view += 1

                    if tree_grid[current_i][j] >= current_tree:
                        break

                    current_i -= 1

            down_view = 1
            if tree_grid[i + 1][j] < current_tree:
                # go all the way down
                current_i = i + 2
                while current_i < num_rows:
                    down_view += 1

                    if tree_grid[current_i][j] >= current_tree:
                        break

                    current_i += 1

            scenic_score = up_view * left_view * down_view * right_view
            max_scenic_score = max(max_scenic_score, scenic_score)

    return max_scenic_score

# print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
